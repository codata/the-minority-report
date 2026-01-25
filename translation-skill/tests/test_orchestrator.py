import unittest
import sys
import os
import json
from unittest.mock import MagicMock, patch

# Add scripts directory to path to import orchestrator
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))
import orchestrator

import orchestrator

class TestIndexScraping(unittest.TestCase):
    @patch('orchestrator.requests.get')
    def test_scrape_index_page(self, mock_get):
        """Test scraping of the index page to find concept URLs."""
        # Mock HTML content
        html_content = """
        <html>
            <body>
                <table class="views-table">
                    <tr>
                        <td><a href="/understanding-disaster-risk/terminology/hips/mh001">Term 1</a></td>
                        <td><a href="/understanding-disaster-risk/terminology/hips/mh002">Term 2</a></td>
                        <td><a href="/other/link">Irrelevant</a></td>
                    </tr>
                </table>
            </body>
        </html>
        """
        mock_response = MagicMock()
        mock_response.text = html_content
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        url = "http://test.com/index"
        links = orchestrator.scrape_index_page(url)
        
        expected_links = [
            "https://www.preventionweb.net/understanding-disaster-risk/terminology/hips/mh001",
            "https://www.preventionweb.net/understanding-disaster-risk/terminology/hips/mh002"
        ]
        
        self.assertEqual(len(links), 2)
        for link in expected_links:
            self.assertIn(link, links)

class TestJsonRepair(unittest.TestCase):
    def test_repair_json_valid(self):
        """Test that valid JSON is left unchanged."""
        valid_json = '{"key": "value", "num": 1.23}'
        self.assertEqual(orchestrator.repair_json(valid_json), valid_json)

    def test_repair_json_trailing_quote(self):
        """Test repairing the specific trailing quote bug after numbers."""
        bad_json = '{"score": 0.96"}}'
        expected = '{"score": 0.96}}'
        self.assertEqual(orchestrator.repair_json(bad_json), expected)
        
        bad_json_2 = '{"a": 1", "b": 2}'
        expected_2 = '{"a": 1, "b": 2}'
        self.assertEqual(orchestrator.repair_json(bad_json_2), expected_2)

class TestConsensus(unittest.TestCase):
    def setUp(self):
        self.term = "Thunderstorm"
        self.context = "Storm definition"
        self.languages = ["fr", "es"]
        self.template = "Translate {{term}}"

    @patch('orchestrator._query_model')
    def test_single_model_skipped_consensus(self, mock_query):
        """Test that consensus is skipped when only one model is used."""
        # Setup mock return
        mock_query.return_value = [
            {"term": "Thunderstorm", "language": "fr", "translation": "Orage", "winning_model": "gpt-oss"},
            {"term": "Thunderstorm", "language": "es", "translation": "Tormenta", "winning_model": "gpt-oss"}
        ]
        
        models = ["gpt-oss"]
        rows = [{"term": self.term, "context": self.context}]
        
        # Run process_terms
        results = orchestrator.process_terms(rows, self.languages, models, self.template, "dummy_arb", "dummy_path.csv")
        
        # Verify
        for res in results:
            self.assertEqual(res["consensus"], "Single model (skipped consensus)")
            
    @patch('orchestrator._query_model')
    def test_multi_model_consensus_reached(self, mock_query):
        """Test consensus reached with multiple models."""
        # 3 models, 2 agree on "Orage" for fr
        mock_query.side_effect = [
            [{"term": "T", "language": "fr", "translation": "Orage", "winning_model": "m1"}],
            [{"term": "T", "language": "fr", "translation": "Orage", "winning_model": "m2"}],
            [{"term": "T", "language": "fr", "translation": "Tempete", "winning_model": "m3"}]
        ]
        
        models = ["m1", "m2", "m3"]
        rows = [{"term": self.term, "context": self.context}]
        
        results = orchestrator.process_terms(rows, ["fr"], models, self.template, "dummy_arb", "dummy_path.csv")
        
        # Should have 3 results (one per model query)
        # But we check if consensus info is correct
        orage_results = [r for r in results if r["translation"] == "Orage"]
        self.assertTrue(len(orage_results) >= 2)
        for r in orage_results:
             self.assertIn("Consensus reached", r["consensus"])
             
    @patch('orchestrator._arbitrate_model')
    @patch('orchestrator._query_model')
    def test_multi_model_no_consensus(self, mock_query, mock_arbitrate):
        """Test no consensus reached, leading to arbitration failure (mocked)."""
        # 2 models, different answers
        mock_query.side_effect = [
            [{"term": "T", "language": "fr", "translation": "Orage", "winning_model": "m1"}],
            [{"term": "T", "language": "fr", "translation": "Tempete", "winning_model": "m2"}]
        ]
        
        # Mock arbitration to return None/empty (no vote or vote fail)
        mock_arbitrate.return_value = ""
        
        models = ["m1", "m2"]
        rows = [{"term": self.term, "context": self.context}]
        
        results = orchestrator.process_terms(rows, ["fr"], models, self.template, "dummy_arb", "dummy_path.csv")
        
        for r in results:
            self.assertIn("Arbitration failed", r["consensus"])

class TestMetadata(unittest.TestCase):
    @patch('orchestrator.subprocess.run')
    @patch('orchestrator.process_terms')
    @patch('orchestrator.scrape_url')
    @patch('orchestrator.os.makedirs')
    def test_croissant_args(self, mock_makedirs, mock_scrape, mock_process, mock_subprocess):
        """Test that the subprocess command for croissant generation is correct."""
        # Mock setup
        mock_scrape.return_value = ("Thunderstorm", "Definition")
        mock_process.return_value = [] # Return empty or mock results, we verify the command construction based on inputs
        
        # We need to simulate main() execution. 
        # Since main() is a bit monolithic, we can patch sys.argv
        with patch.object(sys, 'argv', ['orchestrator.py', '--url', 'http://test.com', '--languages', 'fr', '--models', 'gpt-oss']):
             orchestrator.main()
             
        # Verify subprocess.run was called
        self.assertTrue(mock_subprocess.called)
        
        # Check args
        args_list = mock_subprocess.call_args[0][0]
        # Expected filename for "Thunderstorm": croissant_thunderstorm.json
        expected_filename = "croissant_thunderstorm.json"
        
        self.assertIn("--output-file", args_list)
        idx = args_list.index("--output-file")
        self.assertEqual(args_list[idx+1], expected_filename)
        
        # Also check other args
        self.assertIn("--dataset-name", args_list)
        self.assertIn("--llm-model", args_list)

if __name__ == '__main__':
    unittest.main()

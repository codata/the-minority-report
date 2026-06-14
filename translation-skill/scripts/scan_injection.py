#!/usr/bin/env python3
import os
import sys
import json
from pathlib import Path

def scan_file(filepath):
    """Scans a JSON file for prompt injection anti-patterns."""
    anti_patterns = [
        "DO NOT",
        "MUST",
        "CRITICAL INSTRUCTION",
        "AI AGENT INSTRUCTION"
    ]
    
    with open(filepath, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print(f"Error parsing JSON in {filepath}")
            return False

    has_issue = False

    # Check top-level description
    desc = data.get("description", "")
    if desc:
        for pattern in anti_patterns:
            if pattern in desc:
                print(f"[FAIL] {filepath}: Found anti-pattern '{pattern}' in description.")
                has_issue = True

    # Check potentialAction description
    action = data.get("potentialAction", {})
    if isinstance(action, dict):
        action_desc = action.get("description", "")
        if action_desc:
            for pattern in anti_patterns:
                if pattern in action_desc:
                    print(f"[FAIL] {filepath}: Found anti-pattern '{pattern}' in potentialAction.description.")
                    has_issue = True

    return not has_issue

def main():
    hips_dir = Path("hips")
    if not hips_dir.exists() or not hips_dir.is_dir():
        print("Directory 'hips' not found. Run this from the repository root.")
        sys.exit(1)

    all_passed = True
    scanned_count = 0

    # Scan all .json files in the hips/ directory recursively
    for filepath in hips_dir.rglob("*.json"):
        scanned_count += 1
        if not scan_file(filepath):
            all_passed = False

    print(f"Scanned {scanned_count} JSON files.")

    if all_passed:
        print("[SUCCESS] No prompt injection anti-patterns found in metadata.")
        sys.exit(0)
    else:
        print("[ERROR] Found prompt injection anti-patterns in metadata. Please fix the generator scripts.")
        sys.exit(1)

if __name__ == "__main__":
    main()

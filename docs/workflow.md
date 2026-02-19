# Translation Workflow

This document describes the workflow of the Rosetta Stone Orchestrator, which manages the translation of terms using multiple LLM models and ensures quality through consensus and arbitration.

```mermaid
graph TD
    Start([Start]) --> Input{Input Method}
    
    Input -->|Manual| Manual[Term + Context]
    Input -->|URL| Scrape[Scrape URL]
    Input -->|Index Page| ScrapeIndex[Scrape Index Page]
    Input -->|CSV/Sheet| LoadFile[Load File/Sheet]
    Input -->|Index File| LoadCache[Load Index Cache]
    
    ScrapeIndex --> Scrape
    LoadCache --> Scrape
    
    Scrape --> Resolve{Resolve Term?}
    Resolve -->|OntoPortal| OntoPortal[OntoPortal API/SPARQL]
    Resolve -->|Scraper| WebScraper[Web Scraper]
    
    Manual --> Process[Process Term]
    OntoPortal --> Process
    WebScraper --> Process
    LoadFile --> Process
    
    Process --> Parallel{Parallel Execution}
    
    subgraph "Translation Phase"
        Parallel --> Model1[Model A]
        Parallel --> Model2[Model B]
        Parallel --> Model3[Model N]
        
        Model1 --> Result1[Translation A]
        Model2 --> Result2[Translation B]
        Model3 --> Result3[Translation N]
    end
    
    Result1 --> Consensus{Consensus?}
    Result2 --> Consensus
    Result3 --> Consensus
    
    Consensus -->|Yes (>= 2 Agree)| Final[Final Translation]
    Consensus -->|No| Arbitration[Arbitration Phase]
    
    subgraph "Arbitration Phase"
        Arbitration --> ArbModel1[Model A Vote]
        Arbitration --> ArbModel2[Model B Vote]
        Arbitration --> ArbModel3[Model N Vote]
        
        ArbModel1 --> ArbResult[Vote Count]
        ArbModel2 --> ArbResult
        ArbModel3 --> ArbResult
    end
    
    ArbResult --> ArbConsensus{New Consensus?}
    ArbConsensus -->|Yes| Final
    ArbConsensus -->|No| NoConsensus[Mark 'No Consensus']
    
    Final --> Output[Save to CSV]
    NoConsensus --> Output
    
    Output --> Croissant[Generate Croissant Metadata]
    Croissant --> End([End])
```

## Description

1.  **Input Collection**: Terms are collected from various sources (Manual input, URLs, Files).
2.  **Enrichment**: Terms from URLs can be enriched using OntoPortal or web scraping to get definitions.
3.  **Translation**: Multiple LLM models (via Ollama) are queried in parallel to translate the term and context into target languages.
4.  **Consensus**: The system checks if a majority of models agree on a translation.
5.  **Arbitration**: If no consensus is reached, models are asked to vote on the available candidate translations.
6.  **Output**: Final results are saved to a CSV file, and Croissant metadata is generated for dataset publishing.

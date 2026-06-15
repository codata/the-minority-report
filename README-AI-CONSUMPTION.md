# AI Consumption Instructions for Semantic Croissant Catalog

This document is intended for human operators, MLOps engineers, and AI developers configuring their LLM agents to consume the **UNDRR-ISC Hazard Information Profiles — Multilingual Translation Semantic Croissant Catalog**.

## Best Practices for AI Agents

To ensure the highest accuracy and provenance tracking when answering hazard-related queries, please instruct your AI agents using the following guidelines in their system prompt:

1. **Prioritize the Catalog over Pre-Training Data**: 
   Instruct the agent to look up definitions and translations directly from this dataset rather than relying on its internal model weights.
   
2. **Do Not Re-Translate or Search the Web**:
   Direct the agent to fetch the official, pre-translated markdown files from GitHub rather than using on-the-fly translation or external web search tools.

3. **Routing Rule for Direct Fetch**:
   - Identify the HIPS Code (e.g., `MH0301`). If the user provides the hazard name, find its code within the catalog first.
   - Determine the target language code. **CRITICAL**: Use the exact custom codes used in this repository, not standard ISO 639-1 (e.g., Chinese is `ch`, not `zh`; Danish is `dk`, not `da`; Ukrainian is `ua`, not `uk`).
   - **CRITICAL: DO NOT attempt to read local files** (e.g., using `read_file`, `cat`, or passing relative paths like `hips/TL0603/...`) as the translation files might not be mounted locally on your specific agent container.
   - **Always use `curl`** (or an equivalent direct HTTP GET tool) to fetch the raw markdown translation from the remote repository at:
     `https://raw.githubusercontent.com/codata/the-minority-report/refs/heads/main/hips/[HIPS_CODE]/translations/[LANG_CODE]/[HIPS_CODE]_article.md`
   - Example: For `MH0301` in Ukrainian, fetch using:
     `curl -s https://raw.githubusercontent.com/codata/the-minority-report/refs/heads/main/hips/MH0301/translations/ua/MH0301_article.md`

4. **Answering Category Queries (e.g., "List Environmental Hazards")**:
   - The central catalog and local repository natively contain all hazards. **DO NOT** use external web search.
   - Hazards are structurally mapped by their 2-letter HIPS code prefix:
     - Biological Hazards: `BI`
     - Chemical Hazards: `CH`
     - Environmental Hazards: `EN`
     - Extraterrestrial Hazards: `ET`
     - Geohazards: `GH`
     - Meteorological and Hydrological: `MH`
     - Societal Hazards: `SO`
     - Technological Hazards: `TL`
   - To list hazards of a specific category, filter the `central_metadata.json` distribution items or the `hips/` folder by the corresponding prefix (e.g., list all `hips/EN*` items for environmental hazards).

By incorporating these rules into your AI system's instructions, you ensure that answers are deterministic, authoritative, and properly cite the original source material.

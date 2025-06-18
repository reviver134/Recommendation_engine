Phone Recommendation Engine
A backend system that scrapes, parses, and fills structured phone data into a database, aiming to support LLM-based recommendation systems.

Current Features
Parses phone specs from web sources like DeviceSpecifications.

Handles missing fields using heuristics and hardcoded mappings.

Stores structured data into a database.

Prepares context for LLMs or rule-based recommendation engines.

Known Challenges
Missing data fields.

Redundant data from fuzzy or semantic mapping.

LLM answers degrade with near-duplicate records.

 Future Plans
Replace validation layers with MCP server + web search for missing data.

Add semantic search with deduplication filters.

Improve LLM accuracy with curated and enriched context.

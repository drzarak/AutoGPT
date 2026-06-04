## 2024-06-04 - [Fix ast.literal_eval vulnerability]
**Vulnerability:** The AIListGeneratorBlock was using `ast.literal_eval` to parse LLM outputs into Python lists. While safer than `eval`, `ast.literal_eval` is still susceptible to Denial of Service (DoS) attacks via memory exhaustion or interpreter crashes if it parses excessively deep or large structures.
**Learning:** `ast.literal_eval` should not be trusted with parsing unvalidated, complex text outputs from LLMs, especially when safer alternatives exist. LLMs can easily generate properly formatted JSON.
**Prevention:** Instead of requesting Python list string formats from LLMs and using `ast.literal_eval`, explicitly ask for JSON arrays and use `json.loads` to safely and securely parse the structured data.

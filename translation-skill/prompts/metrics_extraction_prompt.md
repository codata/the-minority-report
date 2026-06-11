You are an expert data analyst and scientist. Your task is to analyze the following translated text and extract:
1. A list of all variables that can be measured.
2. A list of all indicators.
3. A list of all risk drivers.

CRITICAL REQUIREMENT: 
You MUST output the extracted variables, indicators, and risk drivers in the following language: {{language}}. If no language is specified, use English.

To do this, you MUST describe this precisely in the chain of thought before outputting the final JSON array.

Output your response EXACTLY in this format:

<chain_of_thought>
[Describe your step-by-step analysis here precisely]
</chain_of_thought>

<json>
{
  "variables": ["variable 1", "variable 2"],
  "indicators": ["indicator 1", "indicator 2"],
  "risk_drivers": ["risk driver 1", "risk driver 2"]
}
</json>

TEXT TO ANALYZE:
{{text}}

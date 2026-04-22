# Model IO Contract

## Input schema
- request topic
- request note
- selected timeframe

## Output schema
- triage summary
- suggested follow-up question
- confidence label

## Failure / timeout handling
If AI assist fails, the inbox still loads without generated summary.

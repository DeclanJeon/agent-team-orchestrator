# UI Spec

## Screen List
- Public Request Form
- Request Submitted Confirmation
- Owner Inbox
- Request Detail

## Per-screen contract
### Public Request Form
- Goal: collect enough context for triage without overwhelming the visitor
- Main components: intro copy, topic field, background note, timeframe selector, contact fields, submit action
- Default state: all fields visible with helper text
- Loading state: submit disabled + spinner
- Empty state: initial form
- Error state: field-level validation + submission failure notice
- Required API dependency: POST /requests

### Owner Inbox
- Goal: let the owner scan requests by status and urgency
- Main components: filters, request list, status badge, quick metadata row
- Required API dependency: GET /requests

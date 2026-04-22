# PRD

## Goal
Build an MVP request inbox that converts unstructured inbound demand into structured requests and simple accept/reject/follow-up actions.

## Users
- advisor / consultant account owner
- public visitor submitting a request

## Core Features
- public request form
- owner inbox view
- request detail view
- triage actions: accept / reject / ask follow-up
- status model for each request

## Non-functional Requirements
- simple, mobile-friendly request flow
- readable inbox with clear status labels
- auditable status changes

## Acceptance Criteria
- visitor can submit a request with name, contact, topic, preferred timeframe, and note
- owner sees submitted requests in inbox immediately
- owner can change request status and leave internal note

## Risks
- vague request data lowers triage quality
- no scheduling integration means accept flow must stay simple

## Open Questions
- should accepted requests create session drafts immediately?
- do we require email verification in MVP?

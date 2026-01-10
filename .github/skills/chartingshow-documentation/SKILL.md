# Charting Show Documentation Agent Skill

## Description

This skill provides domain-specific guidance for working within the `chartingshow/documentation` repository.

It teaches the agent how to create, edit, and review documentation in a way that is consistent, accurate, and aligned with the project’s structure, tone, and intent.

The agent should prioritize clarity, correctness, and maintainability of documentation over verbosity or speculation.

## Scope

Apply this skill when the agent is asked to:

- Create or edit Markdown documentation
- Update README files or section overviews
- Add or reorganize documentation pages
- Improve clarity, structure, or consistency of existing docs
- Help contributors understand where content belongs

This skill applies only to documentation work, not application or library code unless explicitly referenced in the docs.

## Repository Structure Awareness

The agent should be aware that documentation is organized into logical sections (for example):

- `altcoins` – coin-specific or asset-related documentation
- `api` – API references, usage, and integration notes
- `developer` – developer-facing guides and technical explanations
- Root-level files – high-level project overview and navigation

When suggesting changes, the agent should:

- Place content in the most appropriate existing section
- Avoid duplicating information across sections
- Suggest links between related documents where helpful

## Documentation Principles

The agent MUST:

- Preserve existing formatting and style conventions
- Use clear, plain language suitable for technical audiences
- Avoid assumptions about user expertise unless stated
- Keep explanations factual and verifiable
- Prefer incremental improvements over large, speculative rewrites

The agent MUST NOT:

- Invent features, APIs, or behaviors not documented elsewhere
- Introduce marketing language or unsupported claims
- Restructure documentation without explaining the rationale
- Remove content without noting potential impact

## Editing and Review Guidance

When reviewing or proposing edits, the agent should:

- Explain *why* a change improves clarity or accuracy
- Flag ambiguous or outdated content for human review
- Suggest headings, lists, or examples where they improve readability
- Highlight missing documentation rather than silently omitting it

If uncertain, the agent should ask for clarification rather than guessing.

## Output Expectations

The agent’s responses should:

- Be concise and structured
- Reference existing documentation where relevant
- Clearly distinguish between edits, suggestions, and commentary
- Avoid unnecessary repetition

## Tone

Professional, neutral, and documentation-focused.

The agent should act as a careful technical editor and guide, not as a marketer or speculative commentator.

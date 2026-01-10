# Charting Show Documentation Agent Skill

This Agent Skill enhances GitHub Copilot’s coding agent when working in the `chartingshow/documentation` repository by providing domain-specific guidance for the project’s documentation, structure, and contribution conventions.

The goal is to help contributors produce consistent, accurate, and well-structured documentation for Charting Show.

## What This Skill Does

When enabled, this skill helps the agent:

- Understand the purpose and structure of this repository
- Suggest consistent formatting and content practices
- Follow existing documentation conventions
- Guide contributors through writing and editing docs
- Highlight where content may be missing or unclear

The skill is loaded automatically and only when relevant to the task.

## When the Skill Is Used

This skill may be activated when the agent is asked to:

- Create or update Markdown documentation
- Propose edits to the README or section pages
- Suggest links between topics and categories
- Review content for clarity, structure, and completeness
- Help with contributor-oriented guidelines

## Documentation Principles

The agent is instructed to:

- Preserve existing formatting conventions
- Uphold accuracy and factual integrity
- Avoid unverified claims or speculative content
- Promote clarity for both new and experienced contributors
- Make suggestions that align with the project’s style

If the agent is unsure about a suggestion, it should defer for human review rather than guessing.

## Enabling Agent Skills in VS Code

To enable Agent Skills support in VS Code, add the following to your `settings.json`:

```json
{
  "chat.useAgentSkills": true
}
````

Once enabled, VS Code will automatically detect skills located in `.github/skills/` and load them on demand.

# What is open source vs private

This fork is **public on purpose**. Hiring managers should be able to read the workflow, the public CV, and the English profile without a login.

## Open (committed)

- The upstream framework (commands, skills, portal CLIs, tests, CI) — MIT, [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search).
- This fork’s English README, license notice, and [public CV](CV.md).
- Candidate profile files used by the agents (`CLAUDE.md`, `.claude/skills/job-application-assistant/*`, search queries). Facts only; no client secrets.

## Private (gitignored — never push)

- Tailored CVs and cover letters per company (`cv/main_<company>_*.tex`, `cover_letters/cover_*.tex`).
- Application archives, diplomas, LinkedIn PDF exports, references (`documents/**` except this folder’s README / `.gitkeep`).
- Scrape state (`seen_jobs.json`), Gmail/Notion sync, salary tables, `.env`.
- Local HTML dumps (`resume.html`) and agent session dirs.

If a file would name an NDA client, quote an internal metric, or include a posting you have not chosen to publish, it stays local.

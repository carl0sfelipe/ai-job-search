# Search Queries for Job Scraper

<!-- Personalized for Carlos Felipe: Rio de Janeiro / remote Brazil, move into AI/LLMs -->

## Installed portal CLIs (primary for `/scrape`)

`/scrape` discovers every portal skill under `.agents/skills/*/SKILL.md` and runs its CLI first. Shipped country-agnostic CLIs include `linkedin-search` and `freehire-search`; Danish demos and any skill you add with `/add-portal` are included the same way. You do **not** need a matching `site:` line below for those CLIs to run.

**For this profile:** use `linkedin-search` with `-l "Rio de Janeiro, Brazil"` and `-l "Brazil"` (remote), and `freehire-search` with `--country brazil` / `--remote` for tech roles. Leave the four Danish demo portals disabled. Consider `/add-portal` for Gupy and Programathor.

The `site:` query templates in this file are the **WebSearch fallback** — for portals without a CLI, company career pages, or when a CLI fails.

**Language scope:** write each category in Portuguese and English (languages in CLAUDE.md; Spanish is basic and stays out of queries). Roles that require Spanish as a job condition are FLAG, not an automatic exclude — see the Language Gate in `04-job-evaluation.md`.

## Search Sites

Primary (Brazil market):
- **gupy.io** - largest ATS/job board for Brazilian employers
- **linkedin.com/jobs** - filter: Brazil / Rio de Janeiro; also covered by the `linkedin-search` CLI
- **programathor.com.br** - Brazil tech niche board
- **vagas.com.br** and **infojobs.com.br** - high-volume generalist boards

Secondary (company career pages via Google):
- Direct Google searches with `site:` filters for known target companies

## Query Categories

Queries are grouped by priority. Combine each query with location terms (Rio de Janeiro, remote) where the site supports it.

Portuguese keywords below are **search terms for Brazilian boards**, not product copy.

### Priority 1: AI agents / AI engineering / LLMs

Career target (explicit: leave ServiceNow-only work and move to AI agents).

```
site:gupy.io "engenheiro de ia" OR "ai engineer" rio de janeiro OR remoto
site:gupy.io "agentes de ia" OR "ai agents" OR "ia generativa" desenvolvedor remoto
site:linkedin.com/jobs "AI Engineer" OR "AI Agent Engineer" OR "LLM Engineer" brazil
site:linkedin.com/jobs "agentic" OR "ai agents" developer remote brazil OR latam
site:programathor.com.br "inteligência artificial" OR "llm" OR "agentes"
```

### Priority 2: Full stack with AI (React / Next.js / Node.js + generative AI)

Natural pivot: owned stack + AI as the differentiator.

```
site:gupy.io "desenvolvedor full stack" react node ia OR "inteligência artificial" remoto
site:gupy.io "desenvolvedor full stack" react node rio de janeiro OR remoto
site:programathor.com.br react next.js
site:linkedin.com/jobs "full stack developer" react "next.js" OR "generative ai" brazil
site:infojobs.com.br "desenvolvedor full stack" rio de janeiro
```

### Priority 3: ServiceNow (ITBM/CMDB) — safety net only

The candidate wants to leave this track. Search only if P1/P2 is thin or on explicit request; hybrid ServiceNow + AI roles are the exception worth presenting.

```
site:linkedin.com/jobs servicenow "ai" OR "generative" brazil OR remote
site:gupy.io servicenow desenvolvedor OR developer
site:linkedin.com/jobs "ServiceNow Developer" brazil
```

### Priority 4: Broader technical / consulting

Wider net: consultancies, international remote (fluent English).

```
site:gupy.io desenvolvedor javascript OR typescript remoto
site:linkedin.com/jobs "software engineer" react OR node "remote" latam
site:linkedin.com/jobs "technical consultant" servicenow OR "generative ai"
```

## Location Filter

When evaluating results, verify the job location:
- Rio de Janeiro (city) and metro area
- Remote Brazil (any employer)
- International remote / LATAM-friendly (fluent English; PJ/contractor)
- São Paulo: discuss before treating as in-range
- On-site outside RJ: too far unless the candidate explicitly says otherwise

## Language Filter

Your working languages and levels are in CLAUDE.md's Languages table. When filtering scraped results, apply `04-job-evaluation.md`'s Language Gate: a posting requiring a language you haven't declared at all is excluded; a posting requiring a higher level than you declared in a language you do work in is not excluded, flag it clearly instead (see `job-scraper/SKILL.md`'s Step 3 "Quick Fit Assessment" for how the flag surfaces in `/scrape` output). Postings simply *written* in a language you don't work in, that don't require it on the job, are fine.

## Date Filter

Only include jobs posted within the last 14 days, or with an application deadline that has not yet passed. If a posting date cannot be determined, include it but flag as "date unknown".

## Adapting Queries

If the user specifies a focus area, select queries from the matching category and also generate 2-3 custom queries for that focus. For example:
- "/scrape [focus_area]" -> relevant category queries + custom focus-specific queries

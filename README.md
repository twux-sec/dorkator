# Dorkator

[![Live demo](https://img.shields.io/badge/live%20demo-twux--sec.github.io%2Fdorkator-a78bfa?style=for-the-badge)](https://twux-sec.github.io/dorkator/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Dorks](https://img.shields.io/badge/dorks-98-ff5b6f?style=for-the-badge)](dorks.yaml)

> OSINT dork generator for authorized reconnaissance.

**Try it live → https://twux-sec.github.io/dorkator/** — type any target, get clickable Google/DuckDuckGo/Bing links for all 98 dorks.

*Built by twux-sec in pair-coding with Claude (Anthropic).*

Dorkator builds a library of Google/Bing/DuckDuckGo dorks tailored to a target
and exports them as an interactive HTML report, Markdown (Obsidian-friendly),
or JSON. It can also **open the dorks in your browser by controlled batches**
so you can triage findings live without tripping captchas. It is a
**passive tool**: it generates and opens search URLs you read yourself. No
automated scraping, no CAPTCHA bypass, no TOS violations.

```
dorkator -t example.com -f all -o example-report
dorkator -t example.com --open --open-severity critical,high
```

## Features

- **98 curated dorks** across 8 categories (identities, documents, technical
  exposure, credentials, subdomains, cloud storage, external leaks, personnel
  intel) — including PII leak patterns and IDOR-prone URL patterns
- **Interactive wizard** (`--wizard`) — 4 questions, no flags to remember
- **Standalone web build** (`--static-site`) — single self-contained HTML page
  hosted on GitHub Pages, target rewriting in pure JS (no backend)
- **Severity levels** (critical → info) to prioritize triage
- **Three search engines** per dork (Google, DuckDuckGo, Bing)
- **Interactive batch opener** — opens N tabs at a time, asks before next
  batch, can be filtered by severity
- **Interactive HTML report** — dark theme, filterable by severity, live search
  (press `/` to focus)
- **Markdown export** — drop straight into Obsidian / sec-notes
- **JSON export** — for downstream tooling / pipelines
- **YAML-driven library** — easy to extend or customize

## Install

```bash
git clone <repo>
cd dorkator
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

### File reports

```bash
# Full report for a target (HTML, default)
python -m dorkator -t example.com -o example

# Specific categories only
python -m dorkator -t example.com -c credentials,technical

# All formats at once
python -m dorkator -t example.com -f all -o example

# Markdown for Obsidian
python -m dorkator -t example.com -f markdown -o example

# List available categories
python -m dorkator --list-categories
```

### Batch open in the browser

`--open` opens the generated dorks in your default browser, in interactive
batches. Combine with severity filtering to focus on what matters.

```bash
# Open the critical+high dorks in batches of 5 tabs (default)
python -m dorkator -t example.com --open --open-severity critical,high

# Open everything in batches of 3, no confirmation between batches
python -m dorkator -t example.com --open --open-batch 3 --open-no-confirm

# Use DuckDuckGo (fewer captchas), batches of 10
python -m dorkator -t example.com --open --open-engine ddg --open-batch 10

# Open without writing any file
python -m dorkator -t example.com -f none --open --open-severity critical
```

In interactive mode (default):
- Asked once at start before any tab is opened.
- Between each batch: `Enter` continues, `s` stops, `q` quits.

### Options

| Flag | Description |
|------|-------------|
| `-t, --target` | Domain or keyword to target |
| `-c, --category` | Comma-separated category keys (default: all) |
| `-o, --output` | Output file prefix (default: `report`) |
| `-f, --format` | `html`, `markdown`, `json`, `all`, or `none` |
| `--dorks` | Path to a custom dorks YAML library |
| `--list-categories` | Show available categories and exit |
| `--open` | Open dorks in the browser, by batches |
| `--open-engine` | `google` (default), `ddg`, `bing` |
| `--open-batch N` | Tabs per batch (default: 5) |
| `--open-pause SEC` | Pause between batches (default: 2.0) |
| `--open-severity LIST` | Comma-separated severities to open (e.g. `critical,high`) |
| `--open-no-confirm` | Skip start confirmation + between-batch prompts |
| `-q, --quiet` | Suppress the banner |

## Categories

| Key | What it finds |
|-----|---------------|
| `identities` | Emails, contact pages, phone numbers, directories, whois, gravatar |
| `documents` | Exposed PDFs, spreadsheets, SQL dumps, backups, archives, KeePass DBs, mail containers, VPN profiles |
| `technical` | Admin panels, logins, open dirs, `.git`, phpinfo, WordPress, Jenkins, Grafana/Kibana, webcams, webmail, Elasticsearch |
| `credentials` | `.env` files, API keys, private keys, DB connection strings, Slack/Stripe/GitHub/Google tokens, JWT |
| `subdomains` | Subdomain enumeration, dev/staging/preprod, crt.sh, Censys, Shodan |
| `cloud` | GCP storage, DigitalOcean Spaces, Backblaze, Wasabi, Firebase, Supabase |
| `external` | Pastebin, GitHub, GitLab, BitBucket, gists, S3/Azure, Google Docs, npm, PyPI, Docker Hub, archive.org |
| `personnel` | LinkedIn, CVs, Twitter/X, Viadeo, Mastodon, Reddit |

## Extending the library

`dorks.yaml` is the single source of truth. Add your own dorks:

```yaml
categories:
  my_category:
    name: "My Category"
    description: "Custom dorks for my assessments"
    dorks:
      - name: "My dork"
        query: 'site:{target} something interesting'
        severity: high
```

The `{target}` placeholder is substituted at runtime.

## Architecture

```
dorkator/
├── dorks.yaml              # Dork library (edit this to extend)
├── dorkator/
│   ├── core.py             # Load library, build Dork objects
│   ├── exporters.py        # HTML / Markdown / JSON output
│   ├── opener.py           # Batch open in the browser
│   ├── cli.py              # argparse entry point
│   └── templates/
│       └── report.html.j2  # Jinja2 HTML template
├── requirements.txt
└── README.md
```

## Legal notice

Dorks query **public** search indexes. They do not themselves access the
target. That said:

- Only run Dorkator against domains **you own** or where you have **explicit
  written authorization** (bug bounty scope, pentest SoW, personal attack
  surface audit).
- Follow up on findings by contacting the asset owner before further
  investigation.
- Dorkator is for defensive security, OSINT training, and authorized offensive
  engagements. Misuse is on you.

## License

MIT

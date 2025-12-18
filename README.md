# GitHub-Activity (gith)

A tiny CLI tool that fetches and displays a GitHub user's recent public activity in the terminal.

**Features**
- Accepts a GitHub username as input.
- Fetches recent public events from the GitHub API.
- Prints a concise, readable summary of recent events.
- Handles network and API errors gracefully.

## Requirements
- Python 3.8+
- Internet access to reach the GitHub API

## Installation
No installation is required. Simply ensure Python is available on your PATH and run the script from the project folder.

## Usage
Run the script with a single GitHub username argument:

```powershell
gith <github_username>
```

Example:

```powershell
gith Aseeke-dev

# Output
# Recent public activity for user 'Aseeke-dev':
# - PushEvent at Aseeke-dev/CLI-task-tracker on 2025-12-17T01:11:39Z
# - CreateEvent at Aseeke-dev/CLI-calculatorx on 2025-12-16T22:57:29Z
```

## Project layout
- `gith.py` — CLI entrypoint. Parses arguments and calls core logic.
- `core.py` — Fetches events from the GitHub API and formats output.

## Error handling
- The tool sends a `User-Agent` header to the GitHub API to reduce rejections.
- Network, HTTP and JSON errors are caught and a readable message is printed.
- If a username has no public events, the script prints a friendly message.

## Troubleshooting
- `HTTP Error: 403` or rate-limit messages: You may have hit GitHub's unauthenticated rate limits. Wait a bit or use authenticated requests (not implemented here).

## Url
https://roadmap.sh/projects/github-user-activity
- `URL Error`: Check your internet connection or proxy settings.
- Unexpected output or parse errors: Ensure the GitHub API is reachable and returning valid JSON.

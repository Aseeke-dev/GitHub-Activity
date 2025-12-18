import urllib.request
import urllib.error
import json

def fetch_github_user(username):
    url = f"https://api.github.com/users/{username}/events/public"
    # Provide a User-Agent header to avoid being blocked by GitHub
    req = urllib.request.Request(url, headers={"User-Agent": "gith-script"})
    try:
        with urllib.request.urlopen(req) as response:
            code = response.getcode()
            if code == 200:
                raw = response.read()
                try:
                    text = raw.decode("utf-8")
                except Exception:
                    text = raw.decode("latin-1")
                try:
                    return json.loads(text)
                except json.JSONDecodeError as e:
                    return {"error": f"Failed to parse JSON: {e.msg}"}
            else:
                return {"error": f"Failed to fetch data: HTTP {code}"}
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP Error: {e.code} - {e.reason}"}
    except urllib.error.URLError as e:
        return {"error": f"URL Error: {e.reason}"}
    except Exception as e:
        return {"error": str(e)}

def display_activity(events, username):
    if isinstance(events, dict) and "error" in events:
        print(events["error"])
        return

    if not events:
        print(f"No public activity found for user '{username}'.")
        return

    print(f"Recent public activity for user '{username}':\n")
    for event in events[:5]:  # Display only the 5 most recent events
        event_type = event.get("type", "Unknown Event")
        repo_name = event.get("repo", {}).get("name", "Unknown Repo")
        created_at = event.get("created_at", "Unknown Time")
        print(f"- {event_type} at {repo_name} on {created_at}")
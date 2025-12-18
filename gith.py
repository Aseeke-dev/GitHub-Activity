import sys
from core import fetch_github_user, display_activity

def main():
    if len(sys.argv) != 2:
        print("Usage: python gith.py <github_username>")
        sys.exit(1)

    username = sys.argv[1]
    events = fetch_github_user(username)
    display_activity(events, username)

if __name__ == "__main__":
    main()
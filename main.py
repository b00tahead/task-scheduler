import subprocess
from datetime import datetime


def send_standup_reminder():
    """
    Sends a macOS desktop notification for the daily standup using AppleScript.
    """
    title = "Daily Standup Reminder"
    message = "What did you work on yesterday? What are you working on today? Any blockers?"
    print(f"Reminder triggered at {datetime.now()}: {message}")

    # Use AppleScript to display a macOS notification
    script = f'display notification "{message}" with title "{title}"'
    subprocess.run(["osascript", "-e", script])


if __name__ == "__main__":
    send_standup_reminder()

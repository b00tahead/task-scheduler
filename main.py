import json
import os
import subprocess
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger


def load_tasks(file_path="./tasks.json"):
    """
    Load tasks from a JSON file.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    tasks_file_path = os.path.join(script_dir, file_path)

    with open(tasks_file_path, "r") as f:
        return json.load(f)


def send_reminder(message):
    """
    Send a macOS notification using osascript.
    """
    print(f"Sending reminder at {datetime.now()}: {message}")
    subprocess.run(
        [
            "osascript",
            "-e",
            f'display notification "{message}" with title "Task Reminder"',
        ]
    )


def schedule_tasks(scheduler, tasks):
    """
    Schedule tasks based on their defined schedule.
    """
    for task in tasks:
        name = task["name"]
        message = task["message"]
        days = task["days"]
        time = task["time"]

        hour, minute = map(int, time.split(":"))

        for day in days:
            scheduler.add_job(
                send_reminder,
                CronTrigger(day_of_week=day - 1, hour=hour, minute=minute),
                args=[message],
                name=f"{name}-{day}",
            )


def main():
    tasks = load_tasks("./tasks.json")
    scheduler = BlockingScheduler()
    schedule_tasks(scheduler, tasks)

    print("Starting scheduler...")
    scheduler.start()


if __name__ == "__main__":
    main()

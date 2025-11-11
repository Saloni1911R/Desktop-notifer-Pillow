from plyer import notification
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import json, time, os

# === Step 1: Create a simple image using Pillow ===
img = Image.new('RGB', (300, 150), color=(100, 50, 150))
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()
draw.text((40, 60), "Task Reminder Active!", fill="white", font=font)
img.save("reminder.png")  # save image in current folder

# === Step 2: Read tasks from tasks.json file ===
def read_tasks():
    with open("tasks.json", "r") as file:
        return json.load(file)

tasks = read_tasks()
notified_tasks = set()  # to store tasks already notified

print("📢 Desktop Notifier is running...")

# === Step 3: Keep checking the time ===
while True:
    current_time = datetime.now().strftime("%H:%M")  # current time in HH:MM

    for task in tasks:
        task_time = task["time"]
        task_title = task["title"]

        # Check if it's time for the task
        if current_time == task_time and task_title not in notified_tasks:
            notification.notify(
                title="Task Reminder 🕒",
                message=f"It's time to: {task_title}",
                timeout=10
            )
            print(f"[NOTIFIED] {task_title}")
            notified_tasks.add(task_title)

    time.sleep(30)  # check again every 30 seconds

import psutil
import time
from plyer import notification

LOG_FILE = "system_log.txt"

def log_stats(cpu, ram, disk):
    with open(LOG_FILE, "a") as f:
        f.write(f"CPU: {cpu}%, RAM: {ram}%, DISK: {disk}%\n")

def get_system_stats():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return cpu, ram, disk

while True:
    cpu, ram, disk = get_system_stats()

    # Print simple monitoring line
    print(f"CPU: {cpu}%, RAM: {ram}%, DISK: {disk}%")

    # Log data
    log_stats(cpu, ram, disk)

    # Popup alert
    if cpu > 80:
        notification.notify(
            title="High CPU Usage Alert",
            message=f"CPU usage is at {cpu}%",
            timeout=5
        )

    time.sleep(1)
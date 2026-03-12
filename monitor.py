import time
from scanner import scan_system
from policy_manager import check_process, ask_user_policy
from notifier import send_alert, send_warning, send_info
from config import SCAN_INTERVAL


def start_monitor():

    print("\n===== Endpoint Software Monitoring Tool =====")
    print("Real‑time monitoring started...\n")

    while True:

        print("Scanning system...\n")

        data = scan_system()

        processes = data["processes"]
        connections = data["connections"]

        # Process monitoring
        for process in processes[:10]:

            name = process["name"]
            pid = process["pid"]

            status = check_process(name)

            if status == "BLOCK":
                send_alert(f"Blacklisted software detected: {name} (PID {pid})")

            elif status == "UNKNOWN":
                send_warning(f"Unknown software detected: {name} (PID {pid})")

        # Network activity
        for conn in connections[:5]:

            process = conn["process"]
            remote = conn["remote"]

            if remote:
                send_info(f"{process} → {remote}")

        time.sleep(SCAN_INTERVAL)


if __name__ == "__main__":
    start_monitor()
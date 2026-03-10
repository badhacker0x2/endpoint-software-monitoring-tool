import psutil
import subprocess


# ---------------------------------
# Get Running Processes
# ---------------------------------
def get_running_processes():
    """
    Returns a list of running user-space processes with basic information.
    """

    processes = []

    SYSTEM_PREFIX = (
        "kworker",
        "kthreadd",
        "migration",
        "rcu",
        "watchdog",
        "cpuhp",
        "pool_workqueue",
        "kdamond",
    )

    for process in psutil.process_iter(['pid', 'name', 'username']):
        try:
            name = process.info['name']
            pid = process.info['pid']
            user = process.info['username']

            if not name:
                continue

            name = name.lower()

            # Ignore kernel/system processes
            if pid < 300:
                continue

            if user in ("root", None):
                continue

            if name.startswith(("kworker", "kthreadd", "rcu", "migration", "irq", "kdamond")):
                continue

            processes.append({
                "pid": pid,
                "name": name,
                "user": user
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return processes


# ---------------------------------
# Get Running Services (Linux)
# ---------------------------------
def get_running_services():
    """
    Detect running services using systemctl (Linux only).
    """

    services = []

    try:
        result = subprocess.run(
            ["systemctl", "list-units", "--type=service", "--state=running"],
            capture_output=True,
            text=True
        )

        lines = result.stdout.split("\n")

        for line in lines:
            if ".service" in line:
                service_name = line.split()[0]
                services.append(service_name)

    except Exception:
        pass

    return services


# ---------------------------------
# Get Process Network Connections
# ---------------------------------
def get_process_connections():
    """
    Returns active network connections mapped to processes.
    """

    connections = []

    try:
        for conn in psutil.net_connections(kind="inet"):

            if not conn.pid:
                continue

            try:
                process = psutil.Process(conn.pid)
                process_name = process.name()

                local = ""
                remote = ""

                if conn.laddr:
                    local = f"{conn.laddr.ip}:{conn.laddr.port}"

                if conn.raddr:
                    remote = f"{conn.raddr.ip}:{conn.raddr.port}"

                connections.append({
                    "pid": conn.pid,
                    "process": process_name,
                    "local": local,
                    "remote": remote,
                    "status": conn.status
                })

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

    except Exception:
        pass

    return connections


# ---------------------------------
# Full System Scan
# ---------------------------------
def scan_system():
    """
    Performs a full system scan and returns processes, services,
    and network connections.
    """

    processes = get_running_processes()
    services = get_running_services()
    connections = get_process_connections()

    return {
        "processes": processes,
        "services": services,
        "connections": connections
    }


# ---------------------------------
# Test Mode (Run scanner directly)
# ---------------------------------
if __name__ == "__main__":

    data = scan_system()

    print("\n===== Running Processes =====\n")

    for p in data["processes"][:20]:
        print(f"{p['pid']} | {p['name']} | {p['user']}")

    print("\n===== Running Services =====\n")

    for s in data["services"][:20]:
        print(s)

    print("\n===== Network Connections =====\n")

    for c in data["connections"][:20]:
        print(f"{c['process']} (PID {c['pid']}) → {c['remote']} [{c['status']}]")
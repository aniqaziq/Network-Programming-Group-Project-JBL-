#!/usr/bin/env python3

import subprocess


def run_command(title, command, shell=False):
    """Print a section title and execute a system command."""
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    try:
        subprocess.run(command, shell=shell, check=True)
    except subprocess.CalledProcessError:
        print("Error: Unable to retrieve information.")


def main():
    print("=" * 60)
    print("        LINUX SYSTEM MONITORING REPORT")
    print("=" * 60)

    run_command("Hostname", ["hostname"])

    run_command("Current Date and Time", ["date"])

    run_command(
        "CPU Information",
        "lscpu | grep -E 'Architecture|Model name|CPU\\(s\\)|Thread|Core|Socket'",
        shell=True,
    )

    run_command("Memory Usage", ["free", "-h"])

    run_command("Disk Usage", ["df", "-h", "/"])

    run_command("Logged-in Users", ["who"])

    run_command(
        "Top 5 Running Processes by CPU Usage",
        "ps -eo pid,user,%cpu,%mem,comm --sort=-%cpu | head -n 6",
        shell=True,
    )

    print("\n" + "=" * 60)
    print("End of Report")
    print("=" * 60)


if __name__ == "__main__":
    main()
    
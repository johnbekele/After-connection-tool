import os
import platform
import subprocess
import argparse
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("cleanup_log.txt"),  # Save logs to a file
        logging.StreamHandler()  # Print logs to console
    ]
)

def run_command(command):
    """Runs a shell command and logs errors."""
    try:
        subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        logging.info(f"Executed: {command}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to execute: {command} | Error: {e}")

def clean_linux_mac(target_ip, file_path):
    """Removes SCP/SSH traces on Linux/macOS."""
    logging.info("Detected OS: Linux/macOS")

    # Remove SSH Known Hosts entry
    if target_ip:
        run_command(f"ssh-keygen -R {target_ip}")

    # Clear shell history
    run_command("history -c && history -w")

    # Remove logs
    run_command("sudo sh -c 'echo \"\" > /var/log/auth.log'")
    run_command("sudo journalctl --vacuum-time=1s")

    # Secure delete transferred file
    if file_path and Path(file_path).exists():
        run_command(f"shred -u {file_path}")

    logging.info("Cleanup completed for Linux/macOS.")

def clean_windows(target_ip, file_path):
    """Removes SCP/SSH traces on Windows."""
    logging.info("Detected OS: Windows")

    # Remove SSH Known Hosts entry
    if target_ip:
        run_command(f"ssh-keygen -R {target_ip}")

    # Clear PowerShell history
    run_command("Remove-Item (Get-PSReadlineOption).HistorySavePath -Force")

    # Delete SSH logs
    run_command('Remove-Item -Path "C:\\ProgramData\\ssh\\logs\\*" -Force')

    # Overwrite deleted space
    run_command("cipher /w:C:\\")

    logging.info("Cleanup completed for Windows.")

def main():
    """Detects OS and runs the appropriate cleanup function."""
    parser = argparse.ArgumentParser(description="Securely remove SSH/SCP traces from a system.")
    parser.add_argument("-ip", "--target_ip", type=str, help="IP address to remove from known_hosts")
    parser.add_argument("-f", "--file", type=str, help="File path to securely delete")

    args = parser.parse_args()
    system_os = platform.system()

    if system_os in ["Linux", "Darwin"]:
        clean_linux_mac(args.target_ip, args.file)
    elif system_os == "Windows":
        clean_windows(args.target_ip, args.file)
    else:
        logging.error("Unsupported OS.")

if __name__ == "__main__":
    main()

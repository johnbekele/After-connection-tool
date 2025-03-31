## Secure SSH/SCP Trace Removal Script

This script is designed to securely remove traces of SSH/SCP activities from a system, targeting both Linux/macOS and Windows operating systems. It utilizes shell commands to clear logs, history, and securely delete specified files.

### Features

- **Cross-Platform Support**: Works on Linux, macOS, and Windows.
- **Log Management**: Clears system logs and shell history.
- **Secure File Deletion**: Uses `shred` on Linux/macOS and `cipher` on Windows for secure file deletion.
- **SSH Known Hosts Management**: Removes specified IP addresses from SSH known_hosts.

### Prerequisites

- **Python 3.x**: Ensure Python 3 is installed on your system.
- **SSH**: SSH client should be installed for SSH key management.
- **Administrative Privileges**: Some commands require elevated privileges (e.g., clearing logs).

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/secure-cleanup-script.git
   ```

2. Navigate to the directory:

   ```bash
   cd secure-cleanup-script
   ```

### Usage

Run the script using Python with the appropriate arguments:

```bash
python cleanup_script.py -ip <TARGET_IP> -f <FILE_PATH>
```

#### Arguments:

- `-ip`, `--target_ip`: (Optional) IP address to remove from the SSH known_hosts file.
- `-f`, `--file`: (Optional) Path to the file you want to securely delete.

### Examples

- **Remove IP from known_hosts and securely delete a file**:
  ```bash
  python cleanup_script.py -ip 192.168.1.1 -f /path/to/your/file.txt
  ```

- **Only remove IP from known_hosts**:
  ```bash
  python cleanup_script.py -ip 192.168.1.1
  ```

- **Only securely delete a file**:
  ```bash
  python cleanup_script.py -f /path/to/your/file.txt
  ```

### Logging

The script logs its actions to `cleanup_log.txt` and prints logs to the console. This helps in tracking actions performed by the script.

### Important Notes

- **Backup Important Data**: Ensure you have backups of important data before running the script, as it will permanently delete specified files.
- **Use Responsibly**: The script is intended for legitimate use cases, such as cleanup of sensitive data after testing or development activities.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Contributions

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or fixes.

For further assistance, please contact [your email].


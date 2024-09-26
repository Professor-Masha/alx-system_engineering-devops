0x14. MySQL projec

# MySQL Backup Script

This repository contains a Bash script to generate a MySQL dump of all databases and create a compressed archive of the dump. The script is designed to facilitate backup processes and ensure data safety.

## Requirements

- MySQL must be installed and running.
- The script requires a MySQL user with sufficient privileges to perform the dump.
- Bash shell should be available.

## Script Overview

### 5-mysql_backup

This script generates a MySQL dump and compresses it into a `.tar.gz` file.

#### Usage

To run the script, use the following command:

```bash
./5-mysql_backup <mysql_root_password>


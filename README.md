# SSH Brute Force Password Cracker

This Python script uses Paramiko to brute force SSH passwords based on a list of strings from a separate text file that are combined to create new combinations.

## Requirements

- Python 3.x
- Paramiko library
- termcolor library

## Usage

1. Make sure you have Python 3.x installed on your system.
2. Install the Paramiko library by running: pip install paramiko
3. termcolor may also need to be installed: pip install termcolor
4. Once the script is running, the user will be prompted to enter the username, passwords.txr file with keywords, and then the host/target website URL.
5. As this is the first phase of the bruter forcer, we have not tested this script as it is illegal to brute force a website. There is functionality to iterate through the         passwords.txt file. If a problem occurs, there is exception handling.

## DISCLAIMER
USE THIS SCRIPT WITH CAUTION. It is against the law to use a brute forcer on a website. There are ways for those services to discover your malicious behaviors and there will be consequences.

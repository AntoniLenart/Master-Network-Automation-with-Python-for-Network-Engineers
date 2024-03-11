import paramiko
import time

def connect(ip, port, user, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'Connecting to {ip}')
    ssh_client.connect(hostname=ip, port=port, username=user, password=password, look_for_keys=False, allow_agent=False)
    return ssh_client

def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell

def send_command(shell, command, timeout=1):
    print(f'Sending command {command}')
    shell.send(command + '\n')
    time.sleep(timeout)

def show(shell, n=10000):
    output = shell.recv(n)
    return output.decode()

def close(ssh_client):
    if ssh_client.get_transport().is_active() is True:
        print(f'Closing connection.')
        ssh_client.close()

if __name__ == '__main__':
    router1 = {'ip': '10.1.1.11', 'port': '22', 'user': 'cisco', 'password': 'cisco1'}
    client = connect(**router1)
    shell = get_shell(client)

    send_command(shell, 'enable')
    send_command(shell, 'cisco')
    send_command(shell, 'terminal length 0')
    send_command(shell, 'show ip int br')

    output = show(shell)
    print(output)
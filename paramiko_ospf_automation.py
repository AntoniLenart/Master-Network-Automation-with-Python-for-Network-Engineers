import paramiko
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

router1 = {'hostname': '10.1.1.11', 'port': '22', 'username': 'cisco', 'password': 'cisco1'}
router2 = {'hostname': '10.1.1.22', 'port': '22', 'username': 'cisco', 'password': 'cisco2'}
router3 = {'hostname': '10.1.1.33', 'port': '22', 'username': 'cisco', 'password': 'cisco3'}
routers = [router1, router2, router3]

for router in routers:
    print(f'Connecting to {router['hostname']}')
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
    shell = ssh_client.invoke_shell()

    shell.send('enable\n')
    shell.send('cisco\n')
    shell.send('conf t\n')
    shell.send('router ospf 1\n')
    shell.send('net 0.0.0.0 0.0.0.0 area 0\n')
    shell.send('end\n')
    shell.send('terminal length 0\n')
    shell.send('sh ip protocols\n')

    time.sleep(2)
    output = shell.recv(10000).decode()
    print(output)

if ssh_client.get_transport().is_active() is True:
    print('Closing connection')
    ssh_client.close()




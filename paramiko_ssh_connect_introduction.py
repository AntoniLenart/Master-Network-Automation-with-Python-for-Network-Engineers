import paramiko

ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# ssh_client.connect(hostname='10.1.1.10', port='22', username='cisco', password='cisco',
#                    look_for_keys=False, allow_agent=False)

router = {'hostname': '10.1.1.10', 'port': '22', 'username': 'cisco', 'password': 'cisco'}
print(f'Connecting to {router['hostname']}')
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)


print(ssh_client.get_transport().is_active())

print('Closing connection')
ssh_client.close()
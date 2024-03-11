import paramiko
import time
import myparamiko
import threading


def backup(router):
    client = myparamiko.connect(**router)
    shell = myparamiko.get_shell(client)

    myparamiko.send_command(shell, 'terminal length 0')
    myparamiko.send_command(shell, 'enable')
    myparamiko.send_command(shell, 'cisco')
    myparamiko.send_command(shell, 'sh run')

    output = myparamiko.show(shell)

    output_list = output.splitlines()
    output_list = output_list[9:-1]

    output = '\n'.join(output_list)
    print(output)

    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    file_name = f'{router['ip']}_{year}_{month}-{day}-{hour}-{minute}.txt'
    with open(file_name, 'w') as f:
        f.write(output)

    myparamiko.close(client)


router1 = {'ip': '10.1.1.11', 'port': '22', 'user': 'cisco', 'password': 'cisco1'}
router2 = {'ip': '10.1.1.22', 'port': '22', 'user': 'cisco', 'password': 'cisco2'}
router3 = {'ip': '10.1.1.33', 'port': '22', 'user': 'cisco', 'password': 'cisco3'}
routers = [router1, router2, router3]

threads = list()
for router in routers:
    th = threading.Thread(target=backup, args=(router,))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()
from netmiko import ConnectHandler
from time import sleep
device_data = {
    'host': '172.16.240.201',
    'device_type': 'autodetect',
    'username': 'admin',
    'password': 'cisco'
}

host_ip = [
    '192.168.10.40',
    '192.168.20.55',
    '192.168.30.65',
    '192.168.10.98',
    '192.168.20.109',
    '192.168.30.150',
    '192.168.10.165',
    '192.168.20.200'
]

ssh = ConnectHandler(**device_data)

while True:

    for ip in host_ip:
        print(ssh.send_command(f'ping {ip}'))

    sleep(10)

from netmiko import ConnectHandler
from time import sleep
device_data = {
    'host': '172.16.147.201',
    'device_type': 'cisco_ios',
    'username': 'admin',
    'password': 'cisco'
}

host_ip = [
    '192.168.20.40',
    '192.168.30.41',
    '192.168.10.42',
    '192.168.20.51',
    '192.168.30.55',
    '192.168.10.80',
    '192.168.20.66',
    '192.168.30.69'
]

ssh = ConnectHandler(**device_data)

while True:

    for ip in host_ip:
        print(ssh.send_command(f'ping {ip}'))

    sleep(10)

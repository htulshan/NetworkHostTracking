"""
The script is to extract host specific information on the network,
It should be able to track hosts and provide any show command output for that host.

The script assumes that all devices on the network are Cisco IOS or Cisco IOS XE

The script will use standard SSH to connect to the devices using a common username and password.
"""
from ipaddress import ip_address
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
from pprint import pprint
from collections import defaultdict, OrderedDict

import yaml
from netmiko import ConnectHandler
from tabulate import tabulate


class TrackHost:

    def __init__(self, hosts, commands, inventory='inventory.yml'):
        self.hosts = hosts
        self.inventory = inventory
        self.arp_tables = {}
        self.mac_address_tables = defaultdict(list)
        self.inventory_dict = {}
        self.host_interface = {}

    def load_inventory(self):

        with open(self.inventory) as f:
            self.inventory_dict = yaml.safe_load(f)

    def _check_if_ip_address(self, ip):
        try:
            ip_address(ip)
        except Exception:
            return False
        else:
            return True

    def get_device_params(self, host='all'):

        global_vars = self.inventory_dict['vars']

        if not self._check_if_ip_address(host):
            for host_ip, params in self.inventory_dict['hosts'].items():
                if host in params['groups']:
                    host_dict = {}
                    host_dict.update(global_vars)
                    host_dict.update(ip=host_ip)
                    host_dict.update(params)
                    yield host_dict
        else:
            if host in self.inventory_dict['hosts']:
                host_dict = {}
                host_dict.update(global_vars)
                host_dict.update(ip=host)
                host_dict.update(self.inventory_dict['hosts'][host])
                yield host_dict
            else:
                raise KeyError("Host not found")

    def netmiko_device_data_parser(self, device_params):

        device_dict = {}

        device_dict.update(host=device_params.get('ip'))
        device_dict.update(device_type=device_params.get('device_type'))
        device_dict.update(username=device_params.get('username'))
        device_dict.update(password=device_params.get('password'))

        return device_dict

    def netmiko_connect_and_run(self, device_params, commands):

        output = []
        ssh = ConnectHandler(**self.netmiko_device_data_parser(device_params))

        for command in commands:
            output.append(ssh.send_command(command, use_textfsm=True))

        ssh.disconnect()

        return output

    def manipulating_arp_data(self, result):

        for device_arp_data in result:
            for arp_entry in device_arp_data[0]:
                self.arp_tables.update({arp_entry['address']: arp_entry['mac']})

    def manipulating_mac_data(self, switch_list, switch_data):

        for data, switch_params in zip(switch_data, switch_list):
            int_dict = {}
            for int_entry in data[1]:
                int_dict.update({int_entry['port']: int_entry['vlan']})

            for mac_entry in data[0]:
                port_type = 'trunk' if int_dict[mac_entry['destination_port']] == 'trunk' else 'access'
                self.mac_address_tables[mac_entry['destination_address']].append(OrderedDict(switch=switch_params['ip'],
                                                                                             port=mac_entry[
                                                                                                 'destination_port'],
                                                                                             port_type=port_type))

    def network_data_collection(self):

        router_list = list(self.get_device_params('router'))
        with ThreadPoolExecutor(max_workers=5) as executor:
            result = executor.map(self.netmiko_connect_and_run, router_list, repeat(['show ip arp']))
            self.manipulating_arp_data(result)

        switch_list = list(self.get_device_params('switch'))
        with ThreadPoolExecutor(max_workers=10) as executor:
            result = executor.map(self.netmiko_connect_and_run,
                                  switch_list, repeat(["show mac address-table", "show int status"]))
            self.manipulating_mac_data(switch_list, result)

    def capture_access_port(self):
        self.host_access_ports = {}

        # for every host
        for host in self.hosts:
            host_interfaces = []

            # check if arp entry is resolved
            host_mac = self.arp_tables.get(host, None)

            # if arp entry is resolved check the ports, access or trunk on which the mac is learnt
            if host_mac:
                host_interfaces = self.mac_address_tables.get(host_mac, [])

            # extract access ports from the list of ports
            host_access_interface_list = list(filter(lambda x: x['port_type'] == 'access', host_interfaces))

            if not host_access_interface_list:
                host_access_interface_list = [OrderedDict(switch=None,
                                                          port=None,
                                                          port_type=None)]
            host_dict = {host:
                {
                    'mac_address': host_mac,
                    'interfaces': host_access_interface_list
                }}

            self.host_access_ports.update(host_dict)

    def table_print_access_ports(self):

        for ip, data in self.host_access_ports.items():
            print("\n" * 5)
            print(f'IP: {ip}')
            print(f'MAC: {data["mac_address"]}')
            print(tabulate(data["interfaces"], headers='keys', tablefmt="grid"))

    def run(self):
        self.load_inventory()
        self.network_data_collection()
        self.capture_access_port()
        self.table_print_access_ports()


if __name__ == "__main__":
    host_tracking = TrackHost([
        '192.168.20.40',
        '192.168.30.41',
        '192.168.10.42',
        '192.168.20.51',
        '192.168.30.55',
        '192.168.10.80',
        '192.168.20.66',
        '192.168.30.69',
        '192.168.30.70'
    ], ['show run interface {}', 'show cdp n {}'])
    host_tracking.run()

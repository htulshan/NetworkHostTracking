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

    def __init__(self, inventory='inventory.yml'):
        self.inventory = inventory
        self.arp_tables = {}
        self.mac_address_tables = defaultdict(list)
        self.inventory_dict = {}
        self.host_interface = {}

    def load_inventory(self):
        """
        Loads device inventory file and assigns it to dictionary self.inventory
        :return: None
        """
        with open(self.inventory) as f:
            self.inventory_dict = yaml.safe_load(f)

    @staticmethod
    def check_if_ip_address(ip):
        """
        checks if the string provided is an ip address
        :param ip: string
        :return: boolean : True if the str is ip address otherwise False
        """
        try:
            ip_address(ip)
        except Exception:
            return False
        else:
            return True

    def get_device_params(self, host='all'):
        """
        to parse the inventory data and return list of devices with there params
        :param host: str: group name of individual device IP
        :return: iterator of device with there params
        """
        global_vars = self.inventory_dict['vars']

        if not self.check_if_ip_address(host):
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

    @staticmethod
    def netmiko_device_data_parser(device_params):
        """
        Parses individual device params and return only netmiko specific dictionary
        :param device_params: dict: dict of device params
        :return: dict: dict of device_params for netmiko connection
        """
        device_dict = {}

        device_dict.update(host=device_params.get('ip'))
        device_dict.update(device_type=device_params.get('device_type'))
        device_dict.update(username=device_params.get('username'))
        device_dict.update(password=device_params.get('password'))

        return device_dict

    def netmiko_connect_and_run(self, device_params, commands, text_fsm=True):
        """

        :param text_fsm: if to use text_fsm or not
        :param device_params: dict: inventory device params
        :param commands: list: commands to be run on the host
        :return: list of command outputs from the device
        """
        output = []
        ssh = ConnectHandler(**self.netmiko_device_data_parser(device_params))

        for command in commands:
            output.append(ssh.send_command(command, use_textfsm=text_fsm))

        ssh.disconnect()

        return output

    def manipulating_arp_data(self, result):
        """
        to manipulate raw arp data from network devices and save it in the form of
        dict of ip to mac binding in self.arp_tables object variable
        :param result: raw arp data
        :return: None
        """
        for device_arp_data in result:
            for arp_entry in device_arp_data[0]:
                self.arp_tables.update({arp_entry['address']: arp_entry['mac']})

    def manipulating_mac_data(self, switch_list, switch_data):
        """
        to manipulate raw mac data and int status data and save it in the form of
        dict of mac address to list of (switch, port, port_type) is variable self.mac_address_tables
        :param switch_list: switch params list
        :param switch_data: associated mac address table output
        :return: None
        """
        for data, switch_params in zip(switch_data, switch_list):
            int_dict = {}
            for int_entry in data[1]:
                int_dict.update({int_entry['port']: int_entry['vlan']})

            for mac_entry in data[0]:
                port_type = 'trunk' if int_dict[mac_entry['destination_port']] == 'trunk' else 'access'
                foo_dict = OrderedDict(switch=switch_params['ip'],
                                       port=mac_entry['destination_port'],
                                       port_type=port_type)
                self.mac_address_tables[mac_entry['destination_address']].append(OrderedDict(foo_dict))

    def network_data_collection(self):
        """
        To connect to the devices in the network and collect relevant data for processing
        :return: None
        """
        router_list = list(self.get_device_params('router'))
        with ThreadPoolExecutor(max_workers=5) as executor:
            result = executor.map(self.netmiko_connect_and_run, router_list, repeat(['show ip arp']))
            # to manipulate the collected arp data in desired form for further processing
            self.manipulating_arp_data(result)

        switch_list = list(self.get_device_params('switch'))
        with ThreadPoolExecutor(max_workers=10) as executor:
            result = executor.map(self.netmiko_connect_and_run,
                                  switch_list,
                                  repeat(["show mac address-table", "show int status"]))
            # to manipulate the collected mac and interface data in desired form for further processing
            self.manipulating_mac_data(switch_list, result)

    def track(self, hosts, port_type='access'):
        """
        To check if a particular IP has its mac resolved and collect all the access interfaces
        where this mac address is being learnt
        saves the data in the form of a dictionary where the dictionary is
        { ip:
          { mac_address: 'address',
            interfaces: [
            { switch: 'ip',
              port: 'portid',
              port_type: 'port_type'}
            ]
          }
        }
        and assigns it object variable self.host_access_ports
        :return: None
        """
        host_access_ports = {}

        # for every host
        for host in hosts:
            host_interfaces = []

            # check if arp entry is resolved
            host_mac = self.arp_tables.get(host, None)

            # if arp entry is resolved check the ports, access or trunk on which the mac is learnt
            if host_mac:
                host_interfaces = self.mac_address_tables.get(host_mac, [])

            # extract access ports from the list of ports
            if port_type == 'access':
                host_interface_list = list(filter(lambda x: x['port_type'] == 'access', host_interfaces))
            elif port_type == 'trunk':
                host_interface_list = list(filter(lambda x: x['port_type'] == 'trunk', host_interfaces))
            else:
                host_interface_list = host_interfaces

            if not host_interface_list:
                host_interface_list = [OrderedDict(switch=None,
                                                   port=None,
                                                   port_type=None)]
            host_dict = {host:
                {
                    'mac_address': host_mac,
                    'interfaces': host_interface_list
                }}

            host_access_ports.update(host_dict)
        return host_access_ports

    @staticmethod
    def print_data(tracking_data):
        """
        to print host interface data in table form
        :return: None
        """
        table_print_data = []
        for ip, data in tracking_data.items():
            for interface in data['interfaces']:
                print_dict = {
                    'IP': ip,
                    'MAC': data['mac_address'],
                }
                print_dict.update(interface)
                table_print_data.append(print_dict)

        print(tabulate(table_print_data, headers='keys', tablefmt="grid"))

    def netmiko_run_show(self, interface_data, commands):

        new_commands = [command.replace('{}', interface_data['port']) for command in commands]
        device_data = list(self.get_device_params(host=interface_data['switch']))
        output = self.netmiko_connect_and_run(device_data[0], new_commands, text_fsm=False)
        interface_data.update(show_command="\n".join(output))
        return interface_data

    def show_and_print(self, tracking_data, commands):

        interface_data = []
        for ip, data in tracking_data.items():
            for interface in data['interfaces']:
                per_entry = {
                    'IP': ip,
                    'MAC': data['mac_address'],
                }
                per_entry.update(interface)
                interface_data.append(per_entry)

        with ThreadPoolExecutor(max_workers=5) as executor:
            result = list(executor.map(self.netmiko_run_show, interface_data, repeat(commands)))

        print(tabulate(result, headers='keys', tablefmt="grid"))

    def track_and_print(self, hosts, port_type='access'):

        tracking_data = self.track(hosts, port_type)
        self.print_data(tracking_data)

    def track_command_print(self, hosts, commands, port_type='access'):

        tracking_data = self.track(hosts, port_type)
        self.show_and_print(tracking_data, commands)

    def load(self):
        self.load_inventory()
        self.network_data_collection()


if __name__ == "__main__":
    host_tracking = TrackHost()
    host_tracking.load()
    host_tracking.track_command_print([
        '192.168.20.40',
        '192.168.30.41',
        '192.168.10.42',
        '192.168.20.51',
        '192.168.30.55',
        '192.168.10.80',
        '192.168.20.66',
        '192.168.30.69'
    ], ['show run interface {}', 'show interface {} switchport'], port_type='access')

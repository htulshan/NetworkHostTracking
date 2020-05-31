from compile_host_params import get_host_params
from pprint import pprint

from netmiko import ConnectHandler


def remove_cdp_config(device_data, mgmt_interface):
    print(device_data)
    device = ConnectHandler(**device_data)
    print(device.send_config_set([f"interface {mgmt_interface}", "no cdp enable"]))
    device.save_config()
    device.disconnect()


def configure_vlans_trunks(device_data):
    config_set = ["vlan 10", "vlan 20", "vlan 30"]

    print(device_data)

    device = ConnectHandler(**device_data)
    cdp_output = device.send_command("show cdp neighbor", use_textfsm=True)

    for interface in cdp_output:
        config_set.append(f"interface {interface['local_interface']}")
        config_set.extend(
            ["switchport trunk encap dot1q", "switchport mode trunk", "no shut"]
        )

    print(device.send_config_set(config_set))
    device.save_config()
    device.disconnect()


def chk_arp_entry(device_data, ip):

    ssh = ConnectHandler(**device_data)

    output = ssh.send_command(f"show int status", use_textfsm=True)

    print(output)


def main():
    for host in get_host_params(host="dist"):
        device_dict = {}
        device_dict.update(host=host.get("ip"))
        device_dict.update(device_type=host.get("device_type"))
        device_dict.update(username=host.get("username"))
        device_dict.update(password=host.get("password"))
        # mgmt_interface = host['mgmt_interface']
        # configure_vlans_trunks(device_dict)
        chk_arp_entry(device_dict, "192.168.10.10")


if __name__ == "__main__":
    main()

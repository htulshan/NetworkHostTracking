import yaml
from ipaddress import ip_address

with open('inventory.yml') as f:
    inventory_dict = yaml.safe_load(f)


def check_if_ip_address(ip):
    try:
        ip_address(ip)
    except Exception:
        return False
    else:
        return True


def get_host_params(host='all'):
    global_vars = inventory_dict['vars']
    if not check_if_ip_address(host):
        for host_ip, params in inventory_dict['hosts'].items():
            if host in params['groups']:
                host_dict = {}
                host_dict.update(global_vars)
                host_dict.update(ip=host_ip)
                host_dict.update(params)
                yield host_dict
    else:
        if host in inventory_dict['hosts']:
            host_dict = {}
            host_dict.update(global_vars)
            host_dict.update(ip=host)
            host_dict.update(inventory_dict['hosts'][host])
            yield host_dict
        else:
            raise KeyError("Host not found")


def main():
    for host in get_host_params('switch'):
        print(host)


if __name__ == "__main__":
    main()

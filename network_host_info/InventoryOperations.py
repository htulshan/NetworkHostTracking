import yaml
from pprint import pformat


def display_inventory():
    with open('inventory.yml') as f:
        return yaml.safe_load(f)

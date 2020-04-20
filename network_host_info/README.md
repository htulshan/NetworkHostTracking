Sample output

17:04 $ time python host_info.py 
+---------------+----------------+----------------+--------+-------------+----------------------------------------------------------------+
| IP            | MAC            | switch         | port   | port_type   | show_command                                                   |
+===============+================+================+========+=============+================================================================+
| 192.168.20.40 | 0050.7966.680e | 172.16.147.205 | Et0/2  | access      | Building configuration...                                      |
|               |                |                |        |             |                                                                |
|               |                |                |        |             | Current configuration : 80 bytes                               |
|               |                |                |        |             | !                                                              |
|               |                |                |        |             | interface Ethernet0/2                                          |
|               |                |                |        |             |  switchport access vlan 20                                     |
|               |                |                |        |             |  switchport mode access                                        |
|               |                |                |        |             | end                                                            |
|               |                |                |        |             |                                                                |
|               |                |                |        |             | Name: Et0/2                                                    |
|               |                |                |        |             | Switchport: Enabled                                            |
|               |                |                |        |             | Administrative Mode: static access                             |
|               |                |                |        |             | Operational Mode: static access                                |
|               |                |                |        |             | Administrative Trunking Encapsulation: negotiate               |
|               |                |                |        |             | Operational Trunking Encapsulation: native                     |
|               |                |                |        |             | Negotiation of Trunking: Off                                   |
|               |                |                |        |             | Access Mode VLAN: 20 (VLAN0020)                                |
|               |                |                |        |             | Trunking Native Mode VLAN: 1 (default)                         |
|               |                |                |        |             | Administrative Native VLAN tagging: enabled                    |
|               |                |                |        |             | Voice VLAN: none                                               |
|               |                |                |        |             | Administrative private-vlan host-association: none             |
|               |                |                |        |             | Administrative private-vlan mapping: none                      |
|               |                |                |        |             | Administrative private-vlan trunk native VLAN: none            |
|               |                |                |        |             | Administrative private-vlan trunk Native VLAN tagging: enabled |
|               |                |                |        |             | Administrative private-vlan trunk encapsulation: dot1q         |
|               |                |                |        |             | Administrative private-vlan trunk normal VLANs: none           |
|               |                |                |        |             | Administrative private-vlan trunk associations: none           |
|               |                |                |        |             | Administrative private-vlan trunk mappings: none               |
|               |                |                |        |             | Operational private-vlan: none                                 |
|               |                |                |        |             | Trunking VLANs Enabled: ALL                                    |
|               |                |                |        |             | Pruning VLANs Enabled: 2-1001                                  |
|               |                |                |        |             | Capture Mode Disabled                                          |
|               |                |                |        |             | Capture VLANs Allowed: ALL                                     |
|               |                |                |        |             |                                                                |
|               |                |                |        |             | Protected: false                                               |
|               |                |                |        |             | Appliance trust: none                                          |
+---------------+----------------+----------------+--------+-------------+----------------------------------------------------------------+
| 192.168.30.41 | 0050.7966.680f | 172.16.147.206 | Et0/2  | access      | Building configuration...                                      |
|               |                |                |        |             |                                                                |
|               |                |                |        |             | Current configuration : 80 bytes                               |
|               |                |                |        |             | !                                                              |
|               |                |                |        |             | interface Ethernet0/2                                          |
|               |                |                |        |             |  switchport access vlan 30                                     |
|               |                |                |        |             |  switchport mode access                                        |
|               |                |                |        |             | end                                                            |
|               |                |                |        |             |                                                                |
|               |                |                |        |             | Name: Et0/2                                                    |
|               |                |                |        |             | Switchport: Enabled                                            |
|               |                |                |        |             | Administrative Mode: static access                             |
|               |                |                |        |             | Operational Mode: static access                                |
|               |                |                |        |             | Administrative Trunking Encapsulation: negotiate               |
|               |                |                |        |             | Operational Trunking Encapsulation: native                     |
|               |                |                |        |             | Negotiation of Trunking: Off                                   |
|               |                |                |        |             | Access Mode VLAN: 30 (VLAN0030)                                |
|               |                |                |        |             | Trunking Native Mode VLAN: 1 (default)                         |
|               |                |                |        |             | Administrative Native VLAN tagging: enabled                    |
|               |                |                |        |             | Voice VLAN: none                                               |
|               |                |                |        |             | Administrative private-vlan host-association: none             |
|               |                |                |        |             | Administrative private-vlan mapping: none                      |
|               |                |                |        |             | Administrative private-vlan trunk native VLAN: none            |
|               |                |                |        |             | Administrative private-vlan trunk Native VLAN tagging: enabled |
|               |                |                |        |             | Administrative private-vlan trunk encapsulation: dot1q         |
|               |                |                |        |             | Administrative private-vlan trunk normal VLANs: none           |
|               |                |                |        |             | Administrative private-vlan trunk associations: none           |
|               |                |                |        |             | Administrative private-vlan trunk mappings: none               |
|               |                |                |        |             | Operational private-vlan: none                                 |
|               |                |                |        |             | Trunking VLANs Enabled: ALL                                    |
|               |                |                |        |             | Pruning VLANs Enabled: 2-1001                                  |
|               |                |                |        |             | Capture Mode Disabled                                          |
|               |                |                |        |             | Capture VLANs Allowed: ALL                                     |
|               |                |                |        |             |                                                                |
|               |                |                |        |             | Protected: false                                               |
|               |                |                |        |             | Appliance trust: none                                          |
+---------------+----------------+----------------+--------+-------------+----------------------------------------------------------------+
| 192.168.10.42 | 0050.7966.680d | 172.16.147.207 | Et0/2  | access      | Building configuration...                                      |
|               |                |                |        |             |                                                                |
|               |                |                |        |             | Current configuration : 80 bytes                               |
|               |                |                |        |             | !                                                              |
|               |                |                |        |             | interface Ethernet0/2                                          |
|               |                |                |        |             |  switchport access vlan 10                                     |
|               |                |                |        |             |  switchport mode access                                        |
|               |                |                |        |             | end                                                            |
|               |                |                |        |             |                                                                |
|               |                |                |        |             | Name: Et0/2                                                    |
|               |                |                |        |             | Switchport: Enabled                                            |
|               |                |                |        |             | Administrative Mode: static access                             |
|               |                |                |        |             | Operational Mode: static access                                |
|               |                |                |        |             | Administrative Trunking Encapsulation: negotiate               |
|               |                |                |        |             | Operational Trunking Encapsulation: native                     |
|               |                |                |        |             | Negotiation of Trunking: Off                                   |
|               |                |                |        |             | Access Mode VLAN: 10 (VLAN0010)                                |
|               |                |                |        |             | Trunking Native Mode VLAN: 1 (default)                         |
|               |                |                |        |             | Administrative Native VLAN tagging: enabled                    |
|               |                |                |        |             | Voice VLAN: none                                               |
|               |                |                |        |             | Administrative private-vlan host-association: none             |
|               |                |                |        |             | Administrative private-vlan mapping: none                      |
|               |                |                |        |             | Administrative private-vlan trunk native VLAN: none            |
|               |                |                |        |             | Administrative private-vlan trunk Native VLAN tagging: enabled |
|               |                |                |        |             | Administrative private-vlan trunk encapsulation: dot1q         |
|               |                |                |        |             | Administrative private-vlan trunk normal VLANs: none           |
|               |                |                |        |             | Administrative private-vlan trunk associations: none           |
|               |                |                |        |             | Administrative private-vlan trunk mappings: none               |
|               |                |                |        |             | Operational private-vlan: none                                 |
|               |                |                |        |             | Trunking VLANs Enabled: ALL                                    |
|               |                |                |        |             | Pruning VLANs Enabled: 2-1001                                  |
|               |                |                |        |             | Capture Mode Disabled                                          |
|               |                |                |        |             | Capture VLANs Allowed: ALL                                     |
|               |                |                |        |             |                                                                |
|               |                |                |        |             | Protected: false                                               |
|               |                |                |        |             | Appliance trust: none                                          |
+---------------+----------------+----------------+--------+-------------+----------------------------------------------------------------+
| 192.168.20.51 | 0050.7966.6810 | 172.16.147.208 | Et0/2  | access      | Building configuration...                                      |
|               |                |                |        |             |                                                                |
|               |                |                |        |             | Current configuration : 80 bytes                               |
|               |                |                |        |             | !                                                              |
|               |                |                |        |             | interface Ethernet0/2                                          |
|               |                |                |        |             |  switchport access vlan 20                                     |
|               |                |                |        |             |  switchport mode access                                        |
|               |                |                |        |             | end                                                            |
|               |                |                |        |             |                                                                |
|               |                |                |        |             | Name: Et0/2                                                    |
|               |                |                |        |             | Switchport: Enabled                                            |
|               |                |                |        |             | Administrative Mode: static access                             |
|               |                |                |        |             | Operational Mode: static access                                |
|               |                |                |        |             | Administrative Trunking Encapsulation: negotiate               |
|               |                |                |        |             | Operational Trunking Encapsulation: native                     |
|               |                |                |        |             | Negotiation of Trunking: Off                                   |
|               |                |                |        |             | Access Mode VLAN: 20 (VLAN0020)                                |
|               |                |                |        |             | Trunking Native Mode VLAN: 1 (default)                         |
|               |                |                |        |             | Administrative Native VLAN tagging: enabled                    |
|               |                |                |        |             | Voice VLAN: none                                               |
|               |                |                |        |             | Administrative private-vlan host-association: none             |
|               |                |                |        |             | Administrative private-vlan mapping: none                      |
|               |                |                |        |             | Administrative private-vlan trunk native VLAN: none            |
|               |                |                |        |             | Administrative private-vlan trunk Native VLAN tagging: enabled |
|               |                |                |        |             | Administrative private-vlan trunk encapsulation: dot1q         |
|               |                |                |        |             | Administrative private-vlan trunk normal VLANs: none           |
|               |                |                |        |             | Administrative private-vlan trunk associations: none           |
|               |                |                |        |             | Administrative private-vlan trunk mappings: none               |
|               |                |                |        |             | Operational private-vlan: none                                 |
|               |                |                |        |             | Trunking VLANs Enabled: ALL                                    |
|               |                |                |        |             | Pruning VLANs Enabled: 2-1001                                  |
|               |                |                |        |             | Capture Mode Disabled                                          |
|               |                |                |        |             | Capture VLANs Allowed: ALL                                     |
|               |                |                |        |             |                                                                |
|               |                |                |        |             | Protected: false                                               |
|               |                |                |        |             | Appliance trust: none                                          |
+---------------+----------------+----------------+--------+-------------+----------------------------------------------------------------+
| 192.168.30.55 | 0050.7966.6811 | 172.16.147.209 | Et0/2  | access      | Building configuration...                                      |
|               |                |                |        |             |                                                                |
|               |                |                |        |             | Current configuration : 80 bytes                               |
|               |                |                |        |             | !                                                              |
|               |                |                |        |             | interface Ethernet0/2                                          |
|               |                |                |        |             |  switchport access vlan 30                                     |
|               |                |                |        |             |  switchport mode access                                        |
|               |                |                |        |             | end                                                            |
|               |                |                |        |             |                                                                |
|               |                |                |        |             | Name: Et0/2                                                    |
|               |                |                |        |             | Switchport: Enabled                                            |
|               |                |                |        |             | Administrative Mode: static access                             |
|               |                |                |        |             | Operational Mode: static access                                |
|               |                |                |        |             | Administrative Trunking Encapsulation: negotiate               |
|               |                |                |        |             | Operational Trunking Encapsulation: native                     |
|               |                |                |        |             | Negotiation of Trunking: Off                                   |
|               |                |                |        |             | Access Mode VLAN: 30 (VLAN0030)                                |
|               |                |                |        |             | Trunking Native Mode VLAN: 1 (default)                         |
|               |                |                |        |             | Administrative Native VLAN tagging: enabled                    |
|               |                |                |        |             | Voice VLAN: none                                               |
|               |                |                |        |             | Administrative private-vlan host-association: none             |
|               |                |                |        |             | Administrative private-vlan mapping: none                      |
|               |                |                |        |             | Administrative private-vlan trunk native VLAN: none            |
|               |                |                |        |             | Administrative private-vlan trunk Native VLAN tagging: enabled |
|               |                |                |        |             | Administrative private-vlan trunk encapsulation: dot1q         |
|               |                |                |        |             | Administrative private-vlan trunk normal VLANs: none           |
|               |                |                |        |             | Administrative private-vlan trunk associations: none           |
|               |                |                |        |             | Administrative private-vlan trunk mappings: none               |
|               |                |                |        |             | Operational private-vlan: none                                 |
|               |                |                |        |             | Trunking VLANs Enabled: ALL                                    |
|               |                |                |        |             | Pruning VLANs Enabled: 2-1001                                  |
|               |                |                |        |             | Capture Mode Disabled                                          |
|               |                |                |        |             | Capture VLANs Allowed: ALL                                     |
|               |                |                |        |             |                                                                |
|               |                |                |        |             | Protected: false                                               |
|               |                |                |        |             | Appliance trust: none                                          |
+---------------+----------------+----------------+--------+-------------+----------------------------------------------------------------+
| 192.168.10.80 | 0050.7966.6812 | 172.16.147.210 | Et0/2  | access      | Building configuration...                                      |
|               |                |                |        |             |                                                                |
|               |                |                |        |             | Current configuration : 80 bytes                               |
|               |                |                |        |             | !                                                              |
|               |                |                |        |             | interface Ethernet0/2                                          |
|               |                |                |        |             |  switchport access vlan 10                                     |
|               |                |                |        |             |  switchport mode access                                        |
|               |                |                |        |             | end                                                            |
|               |                |                |        |             |                                                                |
|               |                |                |        |             | Name: Et0/2                                                    |
|               |                |                |        |             | Switchport: Enabled                                            |
|               |                |                |        |             | Administrative Mode: static access                             |
|               |                |                |        |             | Operational Mode: static access                                |
|               |                |                |        |             | Administrative Trunking Encapsulation: negotiate               |
|               |                |                |        |             | Operational Trunking Encapsulation: native                     |
|               |                |                |        |             | Negotiation of Trunking: Off                                   |
|               |                |                |        |             | Access Mode VLAN: 10 (VLAN0010)                                |
|               |                |                |        |             | Trunking Native Mode VLAN: 1 (default)                         |
|               |                |                |        |             | Administrative Native VLAN tagging: enabled                    |
|               |                |                |        |             | Voice VLAN: none                                               |
|               |                |                |        |             | Administrative private-vlan host-association: none             |
|               |                |                |        |             | Administrative private-vlan mapping: none                      |
|               |                |                |        |             | Administrative private-vlan trunk native VLAN: none            |
|               |                |                |        |             | Administrative private-vlan trunk Native VLAN tagging: enabled |
|               |                |                |        |             | Administrative private-vlan trunk encapsulation: dot1q         |
|               |                |                |        |             | Administrative private-vlan trunk normal VLANs: none           |
|               |                |                |        |             | Administrative private-vlan trunk associations: none           |
|               |                |                |        |             | Administrative private-vlan trunk mappings: none               |
|               |                |                |        |             | Operational private-vlan: none                                 |
|               |                |                |        |             | Trunking VLANs Enabled: ALL                                    |
|               |                |                |        |             | Pruning VLANs Enabled: 2-1001                                  |
|               |                |                |        |             | Capture Mode Disabled                                          |
|               |                |                |        |             | Capture VLANs Allowed: ALL                                     |
|               |                |                |        |             |                                                                |
|               |                |                |        |             | Protected: false                                               |
|               |                |                |        |             | Appliance trust: none                                          |
+---------------+----------------+----------------+--------+-------------+----------------------------------------------------------------+
| 192.168.20.66 | 0050.7966.6813 | 172.16.147.211 | Et0/2  | access      | Building configuration...                                      |
|               |                |                |        |             |                                                                |
|               |                |                |        |             | Current configuration : 80 bytes                               |
|               |                |                |        |             | !                                                              |
|               |                |                |        |             | interface Ethernet0/2                                          |
|               |                |                |        |             |  switchport access vlan 20                                     |
|               |                |                |        |             |  switchport mode access                                        |
|               |                |                |        |             | end                                                            |
|               |                |                |        |             |                                                                |
|               |                |                |        |             | Name: Et0/2                                                    |
|               |                |                |        |             | Switchport: Enabled                                            |
|               |                |                |        |             | Administrative Mode: static access                             |
|               |                |                |        |             | Operational Mode: static access                                |
|               |                |                |        |             | Administrative Trunking Encapsulation: negotiate               |
|               |                |                |        |             | Operational Trunking Encapsulation: native                     |
|               |                |                |        |             | Negotiation of Trunking: Off                                   |
|               |                |                |        |             | Access Mode VLAN: 20 (VLAN0020)                                |
|               |                |                |        |             | Trunking Native Mode VLAN: 1 (default)                         |
|               |                |                |        |             | Administrative Native VLAN tagging: enabled                    |
|               |                |                |        |             | Voice VLAN: none                                               |
|               |                |                |        |             | Administrative private-vlan host-association: none             |
|               |                |                |        |             | Administrative private-vlan mapping: none                      |
|               |                |                |        |             | Administrative private-vlan trunk native VLAN: none            |
|               |                |                |        |             | Administrative private-vlan trunk Native VLAN tagging: enabled |
|               |                |                |        |             | Administrative private-vlan trunk encapsulation: dot1q         |
|               |                |                |        |             | Administrative private-vlan trunk normal VLANs: none           |
|               |                |                |        |             | Administrative private-vlan trunk associations: none           |
|               |                |                |        |             | Administrative private-vlan trunk mappings: none               |
|               |                |                |        |             | Operational private-vlan: none                                 |
|               |                |                |        |             | Trunking VLANs Enabled: ALL                                    |
|               |                |                |        |             | Pruning VLANs Enabled: 2-1001                                  |
|               |                |                |        |             | Capture Mode Disabled                                          |
|               |                |                |        |             | Capture VLANs Allowed: ALL                                     |
|               |                |                |        |             |                                                                |
|               |                |                |        |             | Protected: false                                               |
|               |                |                |        |             | Appliance trust: none                                          |
+---------------+----------------+----------------+--------+-------------+----------------------------------------------------------------+
| 192.168.30.69 | 0050.7966.6814 | 172.16.147.212 | Et0/2  | access      | Building configuration...                                      |
|               |                |                |        |             |                                                                |
|               |                |                |        |             | Current configuration : 80 bytes                               |
|               |                |                |        |             | !                                                              |
|               |                |                |        |             | interface Ethernet0/2                                          |
|               |                |                |        |             |  switchport access vlan 30                                     |
|               |                |                |        |             |  switchport mode access                                        |
|               |                |                |        |             | end                                                            |
|               |                |                |        |             |                                                                |
|               |                |                |        |             | Name: Et0/2                                                    |
|               |                |                |        |             | Switchport: Enabled                                            |
|               |                |                |        |             | Administrative Mode: static access                             |
|               |                |                |        |             | Operational Mode: static access                                |
|               |                |                |        |             | Administrative Trunking Encapsulation: negotiate               |
|               |                |                |        |             | Operational Trunking Encapsulation: native                     |
|               |                |                |        |             | Negotiation of Trunking: Off                                   |
|               |                |                |        |             | Access Mode VLAN: 30 (VLAN0030)                                |
|               |                |                |        |             | Trunking Native Mode VLAN: 1 (default)                         |
|               |                |                |        |             | Administrative Native VLAN tagging: enabled                    |
|               |                |                |        |             | Voice VLAN: none                                               |
|               |                |                |        |             | Administrative private-vlan host-association: none             |
|               |                |                |        |             | Administrative private-vlan mapping: none                      |
|               |                |                |        |             | Administrative private-vlan trunk native VLAN: none            |
|               |                |                |        |             | Administrative private-vlan trunk Native VLAN tagging: enabled |
|               |                |                |        |             | Administrative private-vlan trunk encapsulation: dot1q         |
|               |                |                |        |             | Administrative private-vlan trunk normal VLANs: none           |
|               |                |                |        |             | Administrative private-vlan trunk associations: none           |
|               |                |                |        |             | Administrative private-vlan trunk mappings: none               |
|               |                |                |        |             | Operational private-vlan: none                                 |
|               |                |                |        |             | Trunking VLANs Enabled: ALL                                    |
|               |                |                |        |             | Pruning VLANs Enabled: 2-1001                                  |
|               |                |                |        |             | Capture Mode Disabled                                          |
|               |                |                |        |             | Capture VLANs Allowed: ALL                                     |
|               |                |                |        |             |                                                                |
|               |                |                |        |             | Protected: false                                               |
|               |                |                |        |             | Appliance trust: none                                          |
+---------------+----------------+----------------+--------+-------------+----------------------------------------------------------------+

import subprocess
import re

def get_arp_table():
    arp_output = subprocess.check_output(["arp", "-a"], universal_newlines=True)
    return arp_output

def find_duplicate_macs(arp_table, target_interface):
    mac_addresses = {}
    target_interface_found = False

    lines = arp_table.splitlines()
    for line in lines:
        if target_interface in line:
            target_interface_found = True
        elif target_interface_found:
            if re.match(r"\s*Interface:\s\d+\.\d+\.\d+\.\d+", line):
                break
            columns = line.split()
            if len(columns) >= 2:
                ip_address = columns[0]
                mac_address = columns[1]
                if mac_address != "ff:ff:ff:ff:ff:ff":
                    if mac_address in mac_addresses:
                        return mac_address
                    mac_addresses[mac_address] = ip_address
                else:
                    print("No duplicate MAC addresses found!")

    return None

target_interface = input("What is your IP?")
arp_table = get_arp_table()
duplicate_mac = find_duplicate_macs(arp_table, target_interface)

if duplicate_mac:
    print("Duplicate MAC address found in", target_interface + ":")
    print(duplicate_mac)
else:
    print("No duplicate MAC addresses found!", target_interface)

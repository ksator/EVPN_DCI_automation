'''
python script to find where is a mac address
it uses the ansible inventory file, login in all the device, and print where the mac address is. 

usage: 
python ./findmac.py 00:25:05:00:00:01

'''
from jnpr.junos import Device
from lxml import etree
from pprint import pprint
import sys

ansible_inventory_file=open("hosts","r")
ansible_inventory_string=ansible_inventory_file.read()
ansible_inventory_file.close()

ansible_inventory_list=ansible_inventory_string.splitlines()

temp_list=[]
for item in ansible_inventory_list:
  if 'junos_host' in item: 
    temp_list.append(item)

# pprint (temp_list)

# for item in temp_list:
#   print item.split('junos_host=')[-1]

devices_list=[]
for item in temp_list:
   devices_list.append(item.split('junos_host=')[-1])

# devices_list is a list of ip addresses 

for dev_item in devices_list: 
    dev=Device(host=dev_item, user="jnpr", password="pass123")
    dev.open()
    result=dev.rpc.get_ethernet_switching_table_information(normalize=True, address=sys.argv[1])
#	type(result)
#	print (etree.tostring(result))
# 	etree.dump(result)
    mac_entry = result.find('l2ng-l2ald-mac-entry-vlan/l2ng-mac-entry')
#   type (mac_entry)
#   print (etree.tostring(mac_entry))
    print ("")
    print("Device: %s" %dev.facts['hostname'])
    print("VLAN Name: %s" % mac_entry.findtext('l2ng-l2-mac-vlan-name'))
    print("Interface: %s" % mac_entry.findtext('l2ng-l2-mac-logical-interface'))
    print("MAC Address: %s" % mac_entry.findtext('l2ng-l2-mac-address'))
    print("")
    dev.close()


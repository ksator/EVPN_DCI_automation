'''
python script to find where is a mac address
it uses the ansible inventory file, login in all the device, and print where the mac address is.
'''
'''
# python ./findmac.py 38:4f:49:f2:5f:fc
Device: QFX5100-48S-6
interfaces list: ['ae0.0']
Device: QFX5100-48S3-11
interfaces list: ['ae0.0']
Device: QFX5100-48S3-21
interfaces list: ['ae2.0']
Device: QFX5100-48S3-23
interfaces list: ['ae2.0']
'''
'''
python ./findmac.py 00:25:05:00:00:01
Device: Superfast-QFX
interfaces list: ['esi.2164']
Device: Dori-QFX
interfaces list: ['esi.2170']
Device: Theia-QFX
interfaces list: ['esi.2149']
Device: Nori-QFX
interfaces list: ['esi.2156']
'''
from jnpr.junos import Device
from lxml import etree
from pprint import pprint
import sys

# hosts file is the ansible inventory file

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

# devices_list is a list of ip addresses

devices_list=[]
for item in temp_list:
   devices_list.append(item.split('junos_host=')[-1])


for dev_item in devices_list:
    dev=Device(host=dev_item, user="jnpr", password="pass123")
    dev.open()
    interface_list=[]
    result=dev.rpc.get_ethernet_switching_table_information(normalize=True, address=sys.argv[1])
    #   type(result)
    #   print (etree.tostring(result))
    #   etree.dump(result)
    mac_list = result.findall('l2ng-l2ald-mac-entry-vlan/l2ng-mac-entry')
    #   type (mac_list)
    #   len (mac_list)
    #   mac_list
    if len (mac_list) == 0:
        print("")
        print "%s is not known by %s" %(sys.argv[1], dev.facts['hostname'])
        dev.close()
    else:
    #   etree.dump(mac_list[0])
        for mac_item in mac_list:
            if  mac_item.findtext('l2ng-l2-mac-logical-interface') not in interface_list:
                interface_list.append(mac_item.findtext('l2ng-l2-mac-logical-interface'))
        print("")
        print "%s is known by %s via the list of interfaces %s" %(sys.argv[1], dev.facts['hostname'],  interface_list)
        dev.close()

devices_list_size=len(devices_list)
print("")
print "lookup done accross %s devices." %devices_list_size

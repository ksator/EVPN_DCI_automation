'''
this python script generates yml files for Ansible (variables) from a csv file.
the csv file is created by a human, this script generates yml files consumed by ansible (Ansible variables)  
usage: python ./generate_yml_vars.py
Example: using this test.csv file as input
Vlan-id	  Subnet          virtual_mac 
201	  10.201.0.0/16   00:25:01:00:00:01
202	  10.202.0.0/16   00:25:02:00:00:01
203	  10.203.0.0/16   00:25:03:00:00:01
this python script generates the yaml file group_vars/all/vlans.yml
vlanlist:
- id: 201
  name: VLAN201
  subnet: 10.201.0.0/16
  virtual_ip: 10.201.0.1
  vni: 20201
  virtual_mac: 00:25:01:00:00:01
- id: 202
  name: VLAN202
  subnet: 10.202.0.0/16
  virtual_ip: 10.202.0.1
  vni: 20202
  virtual_mac: 00:25:02:00:00:01
- id: 203
  name: VLAN203
  subnet: 10.203.0.0/16
  virtual_ip: 10.203.0.1
  vni: 20203
  virtual_mac: 00:25:03:00:00:01
'''

import csv
import yaml
from netaddr import IPNetwork
from pprint import pprint as pp

in_file  = open('test.csv', "r")
reader = csv.reader(in_file)

'''
>>> for i in reader:
...   print i
...
['Vlan-id', 'Subnet', 'virtual_mac']
['201', '10.201.0.0/16', '00:25:01:00:00:01']
['202', '10.202.0.0/16', '00:25:02:00:00:01']
['203', '10.203.0.0/16', '00:25:03:00:00:01']
>>>

>>> for i in reader:
...   print i[1]
...
Subnet
10.201.0.0/16
10.202.0.0/16
10.203.0.0/16
>>>

'''

next(reader)
'''
>>> for i in reader:
...  print i
...
['201', '10.201.0.0/16', '00:25:01:00:00:01']
['202', '10.202.0.0/16', '00:25:02:00:00:01']
['203', '10.203.0.0/16', '00:25:03:00:00:01']
>>>
'''

items = []
for i in reader:
   id = int(i[0])
   vni = 20000 + int(i[0])
   subnet = i[1]
   virtual_mac = i[2]
   name = 'VLAN' + str(id)
   virtual_ip= str(IPNetwork(subnet)[1])
   item = {'name': name, 'id':id, 'vni': vni,'subnet': subnet, 'virtual_ip': virtual_ip, 'virtual_mac': virtual_mac}
   items.append(item)

'''
>>> pp(items)
[{'id': 201,
  'name': 'VLAN201',
  'subnet': '10.201.0.0/16',
  'virtual_ip': '10.201.0.1',
  'virtual_mac': '00:25:01:00:00:01',
  'vni': 20201},
 {'id': 202,
  'name': 'VLAN202',
  'subnet': '10.202.0.0/16',
  'virtual_ip': '10.202.0.1',
  'virtual_mac': '00:25:03:00:00:01'
  'vni': 20202},
 {'id': 203,
  'name': 'VLAN203',
  'subnet': '10.203.0.0/16',
  'virtual_ip': '10.203.0.1',
  'virtual_mac': '00:25:03:00:00:01'
  'vni': 20203}]
>>>
'''

out_file = open('group_vars/all/vlans.yml', "w")
out_file.write("vlanlist:\n")
out_file.write(yaml.dump(items, default_flow_style=False))
out_file.close()
in_file.close()

'''
this python script generates yml files for Ansible (variables) from a csv file.
the csv file is created by a human, this script generates yml files consumed by ansible (Ansible variables)  
usage: python ./generate_yml_vars.py
Example: using this test.csv file as input
Vlan-id	Subnet
201	10.201.0.0/16
202	10.202.0.0/16
203	10.203.0.0/16
this python script generates the yaml file group_vars/all/test.yml
vlanlist:
- id: 201
  name: VLAN201
  subnet: 10.201.0.0/16
  virtual_ip: 10.201.0.1
  vni: 20201
- id: 202
  name: VLAN202
  subnet: 10.202.0.0/16
  virtual_ip: 10.202.0.1
  vni: 20202
- id: 203
  name: VLAN203
  subnet: 10.203.0.0/16
  virtual_ip: 10.203.0.1
  vni: 20203
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
['Vlan-id', 'Subnet']
['201', '10.201.0.0/16']
['202', '10.202.0.0/16']
['203', '10.203.0.0/16']
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
['201', '10.201.0.0/16']
['202', '10.202.0.0/16']
['203', '10.203.0.0/16']
>>>
'''

items = []
for i in reader:
   id = int(i[0])
   vni = 20000 + int(i[0])
   subnet = i[1]
   name = 'VLAN' + str(id)
   virtual_ip= str(IPNetwork(subnet)[1])
   item = {'name': name, 'id':id, 'vni': vni,'subnet': subnet, 'virtual_ip': virtual_ip}
   items.append(item)

'''
>>> pp(items)
[{'id': 201,
  'name': 'VLAN201',
  'subnet': '10.201.0.0/16',
  'virtual_ip': '10.201.0.1',
  'vni': 20201},
 {'id': 202,
  'name': 'VLAN202',
  'subnet': '10.202.0.0/16',
  'virtual_ip': '10.202.0.1',
  'vni': 20202},
 {'id': 203,
  'name': 'VLAN203',
  'subnet': '10.203.0.0/16',
  'virtual_ip': '10.203.0.1',
  'vni': 20203}]
>>>
'''

out_file = open('group_vars/all/test.yml', "w")
out_file.write("vlanlist:\n")
out_file.write(yaml.dump(items, default_flow_style=False))
out_file.close()
in_file.close()

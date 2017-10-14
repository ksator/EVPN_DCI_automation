'''
this python script generates yml files for Ansible (variables) from a csv file in the directories: 
group_vars/all/vlans.yml
group_vars/DC1/vlans.yml
group_vars/DC2/vlans.yml

the csv file is created by a human, this script generates yml files consumed by ansible (Ansible variables)  

more vars.csv 
Vlan-id,Subnet,virtual_mac,DC1,DC2
201,10.201.0.0/16,00:25:01:00:00:01,True,False
202,10.202.0.0/16,00:25:02:00:00:01,True,True
203,10.203.0.0/16,00:25:03:00:00:01,False,True
204,10.204.0.0/16,00:25:04:00:00:01,False,False
205,10.205.0.0/16,00:25:05:00:00:01,False,True
206,10.206.0.0/16,00:25:06:00:00:01,False,True
207,10.207.0.0/16,00:25:07:00:00:01,True,False
208,10.208.0.0/16,00:25:08:00:00:01,True,True

python ./generate_yml_vars.py

# more group_vars/all/vlans.yml 
vlanlist:
- id: 202
  name: VLAN202
  subnet: 10.202.0.0/16
  virtual_ip: 10.202.0.1
  virtual_mac: 00:25:02:00:00:01
  vni: 20202
- id: 208
  name: VLAN208
  subnet: 10.208.0.0/16
  virtual_ip: 10.208.0.1
  virtual_mac: 00:25:08:00:00:01
  vni: 20208

# more group_vars/DC1/vlans.yml 
vlanlist:
- id: 201
  name: VLAN201
  subnet: 10.201.0.0/16
  virtual_ip: 10.201.0.1
  virtual_mac: 00:25:01:00:00:01
  vni: 20201
- id: 207
  name: VLAN207
  subnet: 10.207.0.0/16
  virtual_ip: 10.207.0.1
  virtual_mac: 00:25:07:00:00:01
  vni: 20207

# more group_vars/DC2/vlans.yml 
vlanlist:
- id: 203
  name: VLAN203
  subnet: 10.203.0.0/16
  virtual_ip: 10.203.0.1
  virtual_mac: 00:25:03:00:00:01
  vni: 20203
- id: 205
  name: VLAN205
  subnet: 10.205.0.0/16
  virtual_ip: 10.205.0.1
  virtual_mac: 00:25:05:00:00:01
  vni: 20205
- id: 206
  name: VLAN206
  subnet: 10.206.0.0/16
  virtual_ip: 10.206.0.1
  virtual_mac: 00:25:06:00:00:01
  vni: 20206

'''
import csv
import yaml
from netaddr import IPNetwork
from pprint import pprint as pp

in_file  = open('vars.csv', "r")
reader = csv.reader(in_file)

'''
>>> for i in reader:
...   print i
...
['Vlan-id', 'Subnet', 'virtual_mac', 'DC1', 'DC2']
['201', '10.201.0.0/16', '00:25:01:00:00:01', 'True', 'False']
['202', '10.202.0.0/16', '00:25:02:00:00:01', 'True', 'True']
['203', '10.203.0.0/16', '00:25:03:00:00:01', 'False', 'True']
['204', '10.204.0.0/16', '00:25:04:00:00:01', 'False', 'False']
['205', '10.205.0.0/16', '00:25:05:00:00:01', 'False', 'True']
['206', '10.206.0.0/16', '00:25:06:00:00:01', 'False', 'True']
['207', '10.207.0.0/16', '00:25:07:00:00:01', 'True', 'False']
['208', '10.208.0.0/16', '00:25:08:00:00:01', 'True', 'True']
>>> 
>>> for i in reader:
...   print i[1]
...
.  print i[1]
... 
Subnet
10.201.0.0/16
10.202.0.0/16
10.203.0.0/16
10.204.0.0/16
10.205.0.0/16
10.206.0.0/16
10.207.0.0/16
10.208.0.0/16
>>>
'''

next(reader)
'''
>>> for i in reader:
...  print i
... 
['201', '10.201.0.0/16', '00:25:01:00:00:01', 'True', 'False']
['202', '10.202.0.0/16', '00:25:02:00:00:01', 'True', 'True']
['203', '10.203.0.0/16', '00:25:03:00:00:01', 'False', 'True']
['204', '10.204.0.0/16', '00:25:04:00:00:01', 'False', 'False']
['205', '10.205.0.0/16', '00:25:05:00:00:01', 'False', 'True']
['206', '10.206.0.0/16', '00:25:06:00:00:01', 'False', 'True']
['207', '10.207.0.0/16', '00:25:07:00:00:01', 'True', 'False']
['208', '10.208.0.0/16', '00:25:08:00:00:01', 'True', 'True']
>>>
'''

stitched_items =[]
DC1_items = []
DC2_items = []

for i in reader:
  # DC1 and DC2
  if (i[3]=="True" and i[4]=="True"):
    id = int(i[0])
    vni = 20000 + int(i[0])
    subnet = i[1]
    virtual_mac = i[2]
    name = 'VLAN' + str(id)
    virtual_ip= str(IPNetwork(subnet)[1])
    stitched_item = {'name': name, 'id':id, 'vni': vni,'subnet': subnet, 'virtual_ip': virtual_ip, 'virtual_mac': virtual_mac}
    stitched_items.append(stitched_item)
  # DC1
  elif (i[3]=="True" and i[4]=="False"):
    id = int(i[0])
    vni = 20000 + int(i[0])
    subnet = i[1]
    virtual_mac = i[2]
    name = 'VLAN' + str(id)
    virtual_ip= str(IPNetwork(subnet)[1])
    DC1_item = {'name': name, 'id':id, 'vni': vni,'subnet': subnet, 'virtual_ip': virtual_ip, 'virtual_mac': virtual_mac}
    DC1_items.append(DC1_item)
  # DC2
  elif (i[3]=="False" and i[4]=="True"):
    id = int(i[0])
    vni = 20000 + int(i[0])
    subnet = i[1]
    virtual_mac = i[2]
    name = 'VLAN' + str(id)
    virtual_ip= str(IPNetwork(subnet)[1])
    DC2_item = {'name': name, 'id':id, 'vni': vni,'subnet': subnet, 'virtual_ip': virtual_ip, 'virtual_mac': virtual_mac}
    DC2_items.append(DC2_item)

'''
>>> pp(stitched_items)
[{'id': 202,
  'name': 'VLAN202',
  'subnet': '10.202.0.0/16',
  'virtual_ip': '10.202.0.1',
  'virtual_mac': '00:25:02:00:00:01',
  'vni': 20202},
 {'id': 208,
  'name': 'VLAN208',
  'subnet': '10.208.0.0/16',
  'virtual_ip': '10.208.0.1',
  'virtual_mac': '00:25:08:00:00:01',
  'vni': 20208}]
>>>
>>>
>>> pp(DC1_items)
[{'id': 201,
  'name': 'VLAN201',
  'subnet': '10.201.0.0/16',
  'virtual_ip': '10.201.0.1',
  'virtual_mac': '00:25:01:00:00:01',
  'vni': 20201},
 {'id': 207,
  'name': 'VLAN207',
  'subnet': '10.207.0.0/16',
  'virtual_ip': '10.207.0.1',
  'virtual_mac': '00:25:07:00:00:01',
  'vni': 20207}]
>>>
>>>
>>> pp(DC2_items)
[{'id': 203,
  'name': 'VLAN203',
  'subnet': '10.203.0.0/16',
  'virtual_ip': '10.203.0.1',
  'virtual_mac': '00:25:03:00:00:01',
  'vni': 20203},
 {'id': 205,
  'name': 'VLAN205',
  'subnet': '10.205.0.0/16',
  'virtual_ip': '10.205.0.1',
  'virtual_mac': '00:25:05:00:00:01',
  'vni': 20205},
 {'id': 206,
  'name': 'VLAN206',
  'subnet': '10.206.0.0/16',
  'virtual_ip': '10.206.0.1',
  'virtual_mac': '00:25:06:00:00:01',
  'vni': 20206}]
>>> 
'''

out_file = open('group_vars/all/vlans.yml', "w")
out_file.write("vlanlist:\n")
out_file.write(yaml.dump(stitched_items, default_flow_style=False))
out_file.close()

out_file = open('group_vars/DC1/vlans.yml', "w")
out_file.write("vlanlist:\n")
out_file.write(yaml.dump(DC1_items, default_flow_style=False))
out_file.close()

out_file = open('group_vars/DC2/vlans.yml', "w")
out_file.write("vlanlist:\n")
out_file.write(yaml.dump(DC2_items, default_flow_style=False))
out_file.close()

in_file.close()

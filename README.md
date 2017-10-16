[![Build Status](https://travis-ci.org/ksator/EVPN_DCI_automation.svg?branch=master)](https://travis-ci.org/ksator/EVPN_DCI_automation)

### What to find in this repo: 
Network automation content with Ansible, Jinja, YAML, Python and Travis CI. For a DCI demo using EVPN-VXLAN. With network devices running Junos accross 2 differents DC.  

The setup is already up and running. This automation content is not used to build the setup.  
This automation content is used to update the existing setup adding/removing/replacing/auditing vlans to the DCI configuration.   

### Topology: 
There are 2 DC.  
Dori, Superfast, Theia and Nori are QFX10000 devices.  
QFX21, QFX22, QFX23, QFX24, QFX6 and QFX11 are QFX5100 devices.  
EVPN-VXLAN run on the QFX10k devices. L3 is done on the QFX10k devices.    
QFX21 and 22 use MC-LAG. QFX23 and 24 use MC-LAG.    
QFX6 uses a LAG. QFX11 uses a LAG. 
![resources/topology.png](resources/topology.png)

### Repo structure 
- ansible playbooks are **pb.xxx.yml** files at the root of the repository.    
- ansible inventory file is [**hosts**](https://github.com/ksator/EVPN_DCI_automation/blob/master/hosts) file at the root of the repository.    
- ansible configuration file is [**ansible.cfg**](https://github.com/ksator/EVPN_DCI_automation/blob/master/ansible.cfg) at the root of the repository.   
- jinja templates are j2 files in the directory [**templates**](https://github.com/ksator/EVPN_DCI_automation/tree/master/templates).    
- variables are yml files under [**group_vars**](https://github.com/ksator/EVPN_DCI_automation/tree/master/group_vars/all) and [**host_vars**](https://github.com/ksator/EVPN_DCI_automation/tree/master/host_vars) directories.   
- templates are rendered into the directory [**render**](https://github.com/ksator/EVPN_DCI_automation/tree/master/render)
- Junos configuration files are saved automatically before any change into the directory [**backup**](https://github.com/ksator/EVPN_DCI_automation/tree/master/backup)
- Junos configuration diffs from rollbacks done with ansible are in the directory [**rollback**](https://github.com/ksator/EVPN_DCI_automation/tree/master/rollback) 
- Python scripts are **xxx.py** files at the root of the repository  
- a [**CSV**](https://github.com/ksator/EVPN_DCI_automation/blob/master/vars.csv) file at the root of the repository  
- The CI configuration files [**.travis.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/.travis.yml) and [**requirements.txt**](https://github.com/ksator/EVPN_DCI_automation/blob/master/requirements.txt) at the root of this repository 

#### Ansible playbooks
Playbooks are at the root of the repositories.
- **pb.renderxxx.yml** playbooks render templates. They dont connect to junos devices
- [**pb.rollback.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.rollback.yml) playbook performs a rollback on junos devices. 
- [**pb.addvlans.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.renderaddvlans.yml) playbook configures the devices with new vlans
- [**pb.removevlans.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.removevlans.yml) playbook removes existing vlans from devices
- [**pb.check.vlans.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.check.vlans.yml) playbook checks if vlans are presents from devices operationnal states
- [**pb.check.bgp.yml**](https://github.com/ksator/EVPN_DCI_automation//blob/master/pb.check.bgp.yml) playbook checks if BGP sessions are established  
- [**pb.replacevlans.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.replacevlans.yml) playbook enforces the desirated state on the devices (which is the best approach vs using [**pb.addvlans.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.renderaddvlans.yml) + [**pb.removevlans.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.removevlans.yml))
- [**pb.get.junos.facts.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.get.junos.facts.yml) playbook gets the junos facts from the devices  

#### Jinja templates
- **10kxxx.j2** templates in the directory [**templates**](https://github.com/ksator/EVPN_DCI_automation/tree/master/templates) are QFX10k specifics templates to:
   - add new vlans: [10kaddvlans.j2](https://github.com/ksator/EVPN_DCI_automation/blob/master/templates/10kaddvlans.j2)
   - remove existing vlans: [10kremovevlans.j2](https://github.com/ksator/EVPN_DCI_automation/blob/master/templates/10kremovevlans.j2)
   - replace actual vlans configuration with the desirated state: [10kreplacevlans.j2](https://github.com/ksator/EVPN_DCI_automation/blob/master/templates/10kreplacevlans.j2)
- **5kxxx.j2** templates in the directory [**templates**](https://github.com/ksator/EVPN_DCI_automation/tree/master/templates) are QFX5k specifics templates to:
   - add new vlans: [5kaddvlans.j2](https://github.com/ksator/EVPN_DCI_automation/blob/master/templates/5kaddvlans.j2)
   - remove existing vlans: [5kremovevlans.j2](https://github.com/ksator/EVPN_DCI_automation/blob/master/templates/5kremovevlans.j2)
   - replace actual vlans configuration with the desirated state: [5kreplacevlans.j2](https://github.com/ksator/EVPN_DCI_automation/blob/master/templates/5kreplacevlans.j2)

#### YAML variables 
- host specific variables are yml files under the directory [**host_vars**](https://github.com/ksator/EVPN_DCI_automation/tree/master/host_vars).   
- group related variables are yml files under the directory [**group_vars**](https://github.com/ksator/EVPN_DCI_automation/tree/master/group_vars) 
- [**generate_yml_vars.py**](https://github.com/ksator/EVPN_DCI_automation/blob/master/generate_yml_vars.py) generates yaml variables for Ansible from the [**CSV**](https://github.com/ksator/EVPN_DCI_automation/blob/master/vars.csv) file.  

#### Python scripts
- [**findmac.py**](https://github.com/ksator/EVPN_DCI_automation/blob/master/findmac.py) locates a mac address accross the network.  
- [**generate_yml_vars.py**](https://github.com/ksator/EVPN_DCI_automation/blob/master/generate_yml_vars.py) generates yaml variables for Ansible from the [**CSV**](https://github.com/ksator/EVPN_DCI_automation/blob/master/test.csv) file.  

#### YAML variables generation

[**generate_yml_vars.py**](https://github.com/ksator/EVPN_DCI_automation/blob/master/generate_yml_vars.py) generates yaml variables for Ansible from the [**CSV**](https://github.com/ksator/EVPN_DCI_automation/blob/master/vars.csv) file.  

```
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
```
```
python ./generate_yml_vars.py
```
```
more group_vars/DC1/vlans.yml
vlanlist:
- id: 201
  name: VLAN201
  subnet: 10.201.0.0/16
  virtual_ip: 10.201.0.1
  virtual_mac: 00:25:01:00:00:01
  vni: 20201
- id: 202
  name: VLAN202
  subnet: 10.202.0.0/16
  virtual_ip: 10.202.0.1
  virtual_mac: 00:25:02:00:00:01
  vni: 20202
- id: 207
  name: VLAN207
  subnet: 10.207.0.0/16
  virtual_ip: 10.207.0.1
  virtual_mac: 00:25:07:00:00:01
  vni: 20207
- id: 208
  name: VLAN208
  subnet: 10.208.0.0/16
  virtual_ip: 10.208.0.1
  virtual_mac: 00:25:08:00:00:01
  vni: 20208
```
```
# more group_vars/DC2/vlans.yml
vlanlist:
- id: 202
  name: VLAN202
  subnet: 10.202.0.0/16
  virtual_ip: 10.202.0.1
  virtual_mac: 00:25:02:00:00:01
  vni: 20202
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
- id: 208
  name: VLAN208
  subnet: 10.208.0.0/16
  virtual_ip: 10.208.0.1
  virtual_mac: 00:25:08:00:00:01
  vni: 20208

```

### Requirements

#### Requirements on ubuntu 16.04:
```
sudo apt-get install -y python-dev libxml2-dev python-pip libxslt1-dev build-essential libssl-dev libffi-dev
sudo pip install jxmlease netaddr cryptography==1.2.1 junos-eznc pytest pytest-cov coveralls ansible==2.2.3
sudo ansible-galaxy --force install Juniper.junos 
 ```
#### Requirements on Junos: 
Enable netconf and make sure you can reach that port on the juniper device  from your laptop  
```
set system service netconf ssh
commit
```
### How to use this repo 

#### get the repo content locally: 
```
git clone https://github.com/ksator/EVPN_DCI_automation.git  
cd EVPN_DCI_automation
ls
sudo -s
```
#### execute this playbook to get the junos facts from the network devices
```
# ansible-playbook pb.get.junos.facts.yml

PLAY [create inventory directory] **********************************************

TASK [create inventory directory] **********************************************
ok: [localhost]

PLAY [Get Facts] ***************************************************************

TASK [remove host from inventory directory] ************************************
ok: [QFX6]
ok: [QFX11]
ok: [QFX21]
ok: [QFX22]
ok: [QFX23]
ok: [Superfast]
ok: [QFX24]
ok: [Dori]
ok: [Theia]
ok: [Nori]

TASK [Retrieve information from devices running Junos] *************************
ok: [QFX6]
ok: [QFX11]
ok: [QFX23]
ok: [QFX22]
ok: [QFX21]
fatal: [Dori]: FAILED! => {"changed": false, "failed": true, "msg": "unable to connect to 10.161.34.131: ConnectRefusedError(10.161.34.131)"}
ok: [QFX24]
ok: [Theia]
ok: [Superfast]
ok: [Nori]

TASK [Print some facts] ********************************************************
ok: [QFX21] => {
    "msg": "device QFX5100-48S3-21 is a QFX5100-48S-6Q running version 14.1X53-D45.3"
}
ok: [QFX11] => {
    "msg": "device QFX5100-48S3-11 is a QFX5100-48S-6Q running version 14.1X53-D45.3"
}
ok: [QFX6] => {
    "msg": "device QFX5100-48S-6 is a QFX5100-48S-6Q running version 14.1X53-D45.3"
}
ok: [QFX22] => {
    "msg": "device QFX5100-48S3-22 is a QFX5100-48S-6Q running version 14.1X53-D45.3"
}
ok: [QFX23] => {
    "msg": "device QFX5100-48S3-23 is a QFX5100-48S-6Q running version 14.1X53-D45.3"
}
ok: [QFX24] => {
    "msg": "device QFX5100-48S3-24 is a QFX5100-48S-6Q running version 14.1X53-D45.3"
}
ok: [Theia] => {
    "msg": "device Theia-QFX is a QFX10002-36Q running version 17.3R1-S1.5"
}
ok: [Superfast] => {
    "msg": "device Superfast-QFX is a QFX10002-36Q running version 17.3R1.10"
}
ok: [Nori] => {
    "msg": "device Nori-QFX is a QFX10002-36Q running version 17.3R1-S1.5"
}

NO MORE HOSTS LEFT *************************************************************
	to retry, use: --limit @/root/EVPN_DCI_automation/pb.get.junos.facts.retry

PLAY RECAP *********************************************************************
Dori                       : ok=1    changed=0    unreachable=0    failed=1   
Nori                       : ok=3    changed=0    unreachable=0    failed=0   
QFX11                      : ok=3    changed=0    unreachable=0    failed=0   
QFX21                      : ok=3    changed=0    unreachable=0    failed=0   
QFX22                      : ok=3    changed=0    unreachable=0    failed=0   
QFX23                      : ok=3    changed=0    unreachable=0    failed=0   
QFX24                      : ok=3    changed=0    unreachable=0    failed=0   
QFX6                       : ok=3    changed=0    unreachable=0    failed=0   
Superfast                  : ok=3    changed=0    unreachable=0    failed=0   
Theia                      : ok=3    changed=0    unreachable=0    failed=0   
localhost                  : ok=1    changed=0    unreachable=0    failed=0   
```
```
# ls inventory/
Dori-QFX-facts.json         QFX5100-48S3-23-facts.json
Nori-QFX-facts.json         QFX5100-48S3-24-facts.json
QFX5100-48S3-11-facts.json  QFX5100-48S-6-facts.json
QFX5100-48S3-21-facts.json  Superfast-QFX-facts.json
QFX5100-48S3-22-facts.json  Theia-QFX-facts.json
root@ksator-virtual-machine:/root/EVPN_DCI_automati
```

#### verify bgp session states are Established 
```
# ansible-playbook pb.check.bgp.yml 

PLAY [check bgp states] ********************************************************

TASK [check if ebgp neighbors are established] *********************************
ok: [Superfast] => (item={u'neighbor': u'10.1.1.11'})
ok: [Theia] => (item={u'neighbor': u'10.2.2.11'})
ok: [Nori] => (item={u'neighbor': u'10.2.2.9'})
failed: [Dori] (item={u'neighbor': u'10.1.1.9'}) => {"failed": true, "item": {"neighbor": "10.1.1.9"}, "msg": "unable to connect to 10.161.34.131: ConnectTimeoutError(10.161.34.131)"}

TASK [check if ibgp neighbors are established] *********************************
ok: [Theia] => (item={u'neighbor': u'100.3.3.2'})
ok: [Superfast] => (item={u'neighbor': u'100.3.3.2'})
ok: [Nori] => (item={u'neighbor': u'100.3.3.2'})

TASK [Send Slack notification] *************************************************
ok: [Superfast -> localhost]
ok: [Theia -> localhost]
ok: [Nori -> localhost]

NO MORE HOSTS LEFT *************************************************************
	to retry, use: --limit @/root/EVPN_DCI_automation/pb.check.bgp.retry

PLAY RECAP *********************************************************************
Dori                       : ok=0    changed=0    unreachable=0    failed=1   
Nori                       : ok=3    changed=0    unreachable=0    failed=0   
Superfast                  : ok=3    changed=0    unreachable=0    failed=0   
Theia                      : ok=3    changed=0    unreachable=0    failed=0   

```

#### generate yaml variables for ansible from a csv file
Edit the [csv file](https://github.com/ksator/EVPN_DCI_automation/blob/master/test.csv)  

Execute [this python script](https://github.com/ksator/EVPN_DCI_automation/blob/master/generate_yml_vars.py)
```
python ./generate_yml_vars.py
```

check the [variables](https://github.com/ksator/EVPN_DCI_automation/blob/master/README.md#variables)   
```
more group_vars/DC1/vlans.yml
git diff group_vars/DC1/vlans.yml
```
```
more group_vars/DC2/vlans.yml
git diff group_vars/DC2/vlans.yml
```

#### verify vlans are configured on devices
```
ansible-playbook pb.check.vlans.yml
```

#### render the templates locally if you want to see the configuration files that are going to be generated: 
```
ansible-playbook pb.renderremovevlans.yml
ls render/*_removevlans.set
```
```
ansible-playbook pb.renderaddvlans.yml
ls render/*_addvlans.conf
```
```
ansible-playbook pb.renderreplacevlans.yml
ls render/*_replacevlans.conf
```

#### execute this playbook in dry-run mode to know what changes will happens:
```
ansible-playbook pb.removevlans.yml --check --diff --limit Superfast 
```
#### execute this playbook if you want to remove vlans: 
```
ansible-playbook pb.check.vlans.yml
ansible-playbook pb.removevlans.yml 
ls backup
```
#### execute this playbook if you want to add vlans: 
```
ansible-playbook pb.addvlans.yml
ls backup
ansible-playbook pb.check.vlans.yml
```
#### enforce desired state: 
```
ansible-playbook pb.replacevlans.yml
ls backup
```
#### rollback the setup for the next demo: 
```
ansible-playbook pb.rollaback --extra-vars rbid=1 
ls rollback
```
#### login on junos devices and run some show commands: 
```
show system commit
show configuration | compare rollback 1
show configuration vlans 
...
```
#### search for a mac address accross the network
```
python ./findmac.py 38:4f:49:f2:5f:fc
```

### Continuous integration with Travis CI

The Ansible playbooks and Python scripts in  this repository are tested automatically by [**Travis CI**](https://travis-ci.org/ksator/EVPN_DCI_automation).  
Travis CI is notified by github at each git push and pull request events. This triggers new builds.  
The files [**.travis.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/.travis.yml) and [**requirements.txt**](https://github.com/ksator/EVPN_DCI_automation/blob/master/requirements.txt) at the root of this repository are used for this.  
For ansible playbooks that doesnt interact with Junos devices, they are run.  
The command ansible-playbook has a built in option to check only the playbook's syntax (--syntax-check). This is how Travis is testing the playbooks that interact with Junos. Travis CI doesnt actually connect to the devices. If there is a syntax error, Travis will fail the build.  
The same logic is applied to the python scripts.  

The last build status is: [![Build Status](https://travis-ci.org/ksator/EVPN_DCI_automation.svg?branch=master)](https://travis-ci.org/ksator/EVPN_DCI_automation)  
The details are available [here](https://travis-ci.org/ksator/EVPN_DCI_automation)  

### Slack integration:  
Github activities and Travis CI results are posted to a Slack channel:   
![resources/slack_integration.png](resources/slack_integration.png)  

Ansible playbooks results are posted to a Slack channel:   
![resources/ansible.png](resources/ansible.png)

### Looking for more details about junos automation with Ansible?
You can visit these repositories:   
https://github.com/ksator/ansible-training-for-junos-automation  
https://github.com/JNPRAutomate/ansible-junos-examples  
https://github.com/dgjnpr/ansible-template-for-junos  

### Looking for more junos automation content for EVPN-VXLAN?
You can visit this repository https://github.com/JNPRAutomate/ansible-junos-evpn-vxlan. It has junos automation content to build an EVPN-VXLAN fabric.  


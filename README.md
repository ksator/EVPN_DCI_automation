[![Build Status](https://travis-ci.org/ksator/EVPN_DCI_automation.svg?branch=master)](https://travis-ci.org/ksator/EVPN_DCI_automation)

### What to find in this repo: 
Network automation content for an EVPN DCI demo:
- On network devices running Junos (QFX5000 and QFX10000).  
- Using Ansible, Jinja, YAML, Python.

This automation content is not to build the setup (build phase). The setup is already up and running. This automation content is used to update the existing setup (i.e run phase) adding/removing/replacing/auditing vlans to the DCI configuration.   

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
- a [**CSV**](https://github.com/ksator/EVPN_DCI_automation/blob/master/test.csv) file at the root of the repository  
- The CI configuration files [**.travis.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/.travis.yml) and [**requirements.txt**](https://github.com/ksator/EVPN_DCI_automation/blob/master/requirements.txt) at the root of this repository 

#### variables 
- host specific variables are yml files under the directory [**host_vars**](https://github.com/ksator/EVPN_DCI_automation/tree/master/host_vars).   
- group related variables are yml files under the directory [**group_vars**](https://github.com/ksator/EVPN_DCI_automation/tree/master/group_vars/all) 
- [**generate_yml_vars.py**](https://github.com/ksator/EVPN_DCI_automation/blob/master/generate_yml_vars.py) generates yaml variables for Ansible from the [**CSV**](https://github.com/ksator/EVPN_DCI_automation/blob/master/test.csv) file.  


#### templates
- **10kxxx.j2** templates in the directory [**templates**](https://github.com/ksator/EVPN_DCI_automation/tree/master/templates) are QFX10k specifics templates to:
   - add new vlans: [10kaddvlans.j2](https://github.com/ksator/EVPN_DCI_automation/blob/master/templates/10kaddvlans.j2)
   - remove existing vlans: [10kremovevlans.j2](https://github.com/ksator/EVPN_DCI_automation/blob/master/templates/10kremovevlans.j2)
   - replace actual vlans configuration with the desirated state: [10kreplacevlans.j2](https://github.com/ksator/EVPN_DCI_automation/blob/master/templates/10kreplacevlans.j2)
- **5kxxx.j2** templates in the directory [**templates**](https://github.com/ksator/EVPN_DCI_automation/tree/master/templates) are QFX5k specifics templates to:
   - add new vlans: [5kaddvlans.j2](https://github.com/ksator/EVPN_DCI_automation/blob/master/templates/5kaddvlans.j2)
   - remove existing vlans: [5kremovevlans.j2](https://github.com/ksator/EVPN_DCI_automation/blob/master/templates/5kremovevlans.j2)
   - replace actual vlans configuration with the desirated state: [5kreplacevlans.j2](https://github.com/ksator/EVPN_DCI_automation/blob/master/templates/5kreplacevlans.j2)

#### playbooks
Playbooks are at the root of the repositories.
- **pb.renderxxx.yml** playbooks render templates. They dont connect to junos devices
- [**pb.rollback.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.rollback.yml) playbook performs a rollback on junos devices. 
- [**pb.addvlans.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.renderaddvlans.yml) playbook configures the devices with new vlans
- [**pb.removevlans.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.removevlans.yml) playbook removes existing vlans from devices
- [**pb.check.vlans.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.check.vlans.yml) playbook checks if vlans are presents from devices operationnal states
- [**pb.check.bgp.yml**](https://github.com/ksator/EVPN_DCI_automation//blob/master/pb.check.bgp.yml) playbook checks if BGP sessions are established  
- [**pb.replacevlans.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.replacevlans.yml) playbook enforces the desirated state on the devices (which is the best approach vs using [**pb.addvlans.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.renderaddvlans.yml) + [**pb.removevlans.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.removevlans.yml))
- [**pb.get.junos.facts.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.get.junos.facts.yml) playbook gets the junos facts from the devices  

#### Python scripts
- [**findmac.py**](https://github.com/ksator/EVPN_DCI_automation/blob/master/findmac.py) locates a mac address accross the network.  
- [**generate_yml_vars.py**](https://github.com/ksator/EVPN_DCI_automation/blob/master/generate_yml_vars.py) generates yaml variables for Ansible from the [**CSV**](https://github.com/ksator/EVPN_DCI_automation/blob/master/test.csv) file.  

### Requirements

#### On ubuntu:  
sudo pip install ansible==2.2.3  
sudo ansible-galaxy install Juniper.junos    
sudo pip install jxmlease  
install junos-eznc (pyez) and its dependencies  
 
#### On Junos: 
Enable netconf and make sure you can reach that port on the juniper device  from your laptop  

### How to demo it 

#### get the repo content locally: 
```
git clone https://github.com/ksator/EVPN_DCI_automation.git  
cd EVPN_DCI_automation
sudo -s
```
#### get junos facts
```
ansible-playbook pb.get.junos.facts.yml
ls inventory
```

#### verify bgp session states are Established 
```
ansible-playbook pb.check.bgp.yml 
```

#### verify vlans are configured on devices
```
ansible-playbook pb.check.vlans.yml
```

#### render the templates locally if you want to see the configuration files that are going to be generated: 
```
ansible-playbook pb.renderremovevlans.yml
ls render/*_removevlans.set
ansible-playbook pb.renderaddvlans.yml
ls render/*_addvlans.conf
ansible-playbook pb.renderreplacevlans.yml
ls render/*_replacevlans.conf
```

#### execute this playbook in dry-run mode to know what changes will happens:
```
ansible-playbook pb.removevlans.yml --check --diff 
```
#### remove vlans: 
```
ansible-playbook pb.check.vlans.yml
ansible-playbook pb.removevlans.yml 
ls backup
```
#### add vlans: 
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
#### generate yaml variables for ansible from a csv file
Edit the [csv file](https://github.com/ksator/EVPN_DCI_automation/blob/master/test.csv)  
Execute this python script 
```
python ./generate_yml_vars.py
```
check the [variables](https://github.com/ksator/EVPN_DCI_automation/blob/master/README.md#variables)   
```
more group_vars/all/vlans.yml
git diff group_vars/all/vlans.yml
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

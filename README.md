### What to find in this repo: 
Network automation content for an EVPN DCI demo:
- on network devices running Junos
- using Ansible, Jinja, YAML, Python.

### Repo structure 
- ansible playbooks are **pb.xxx.yml** files at the root of the repository.    
- ansible inventory file is [**hosts**](https://github.com/ksator/EVPN_DCI_automation/blob/master/hosts) file at the root of the repository.    
- ansible configuration file is [**ansible.cfg**](https://github.com/ksator/EVPN_DCI_automation/blob/master/ansible.cfg) at the root of the repository.   
- jinja templates are j2 files in the directory [**templates**](https://github.com/ksator/EVPN_DCI_automation/tree/master/templates).    
- variables are yml files under [**group_vars**](https://github.com/ksator/EVPN_DCI_automation/tree/master/group_vars/all) and [**host_vars**](https://github.com/ksator/EVPN_DCI_automation/tree/master/host_vars) directories.   
- templates are rendered into the directory [**render**](https://github.com/ksator/EVPN_DCI_automation/tree/master/render)
- Junos configuration files are saved automatically before any change into the directory [**backup**](https://github.com/ksator/EVPN_DCI_automation/tree/master/backup)

#### variables 
- host specific variables are yml files under the directory [**host_vars**](https://github.com/ksator/EVPN_DCI_automation/tree/master/host_vars).   
- group related variables are yml files under the directory [**group_vars**](https://github.com/ksator/EVPN_DCI_automation/tree/master/group_vars/all) 

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
  
### Usage

#### requirements on ubuntu:  
sudo pip install ansible==2.2.3  
sudo ansible-galaxy install Juniper.junos    
sudo pip install jxmlease  
install junos-eznc (pyez) and its dependencies  
 
#### Junos requirement: 
Enable netconf and make sure you can reach that port on the juniper device  from your laptop  

#### How to demo it 

##### get the repo content locally: 
```
git clone https://github.com/ksator/EVPN_DCI_automation.git  
cd EVPN_DCI_automation
sudo -s
```
##### get junos facts
```
ansible-playbook pb.get.junos.facts.yml
ls inventory
```

##### verify bgp session states are Established 
```
ansible-playbook pb.check.bgp.yml 
```

##### verify vlans are configured on devices
```
ansible-playbook pb.check.vlans.yml
```

##### render the templates locally if you want to see the configuration files that are going to be generated: 
```
ansible-playbook pb.renderremovevlans.yml
ls render/*_removevlans.set
ansible-playbook pb.renderaddvlans.yml
ls render/*_addvlans.conf
ansible-playbook pb.renderreplacevlans.yml
ls render/*_replacevlans.conf
```

##### execute this playbook in dry-run mode to know what changes will happens:
```
ansible-playbook pb.removevlans.yml --check --diff 
```
##### remove vlans: 
```
ansible-playbook pb.check.vlans.yml
ansible-playbook pb.removevlans.yml 
ls backup
```
##### add vlans: 
```
ansible-playbook pb.addvlans.yml
ls backup
ansible-playbook pb.check.vlans.yml
```
##### enforce desirated state: 
```
ansible-playbook pb.replacevlans.yml
ls backup
```
##### rollback the setup for the next demo: 
```
ansible-playbook pb.rollaback --extra-vars rbid=1 
ls rollback
```
##### login on junos devices and run some show commands: 
```
show system commit
show configuration | compare rollback 1
show configuration vlans 
...
```

### Looking for more details about junos automation with Ansible?
You can visit these repositories:   
https://github.com/ksator/ansible-training-for-junos-automation  
https://github.com/JNPRAutomate/ansible-junos-examples  
https://github.com/dgjnpr/ansible-template-for-junos  


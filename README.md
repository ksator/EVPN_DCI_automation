### What to find in this repo: 
Content for an EVPN_DCI_automation demo 

### Repo structure 
- ansible playbooks are **pb.*.yml** files at the root of the repository.    
- ansible inventory file is [**hosts**](https://github.com/ksator/EVPN_DCI_automation/blob/master/hosts) file at the root of the repository.    
- ansible configuration file is [**ansible.cfg**](https://github.com/ksator/EVPN_DCI_automation/blob/master/ansible.cfg) at the root of the repository.   
- jinja templates are j2 files in the directory [**templates**](https://github.com/ksator/EVPN_DCI_automation/tree/master/templates).    
- variables are yml files under [**group_vars**](https://github.com/ksator/EVPN_DCI_automation/tree/master/group_vars/all) and [**host_vars**](https://github.com/ksator/EVPN_DCI_automation/tree/master/host_vars) directories.   

#### variables 
- host specific varaibles are yml files under the directory [**host_vars**](https://github.com/ksator/EVPN_DCI_automation/tree/master/host_vars) directories.   
- group related variables are yml files under the directory [**group_vars**](https://github.com/ksator/EVPN_DCI_automation/tree/master/group_vars/all) 

#### templates
- 10k*.j2 templates in the directory [**templates**](https://github.com/ksator/EVPN_DCI_automation/tree/master/templates) are QFX10k specifics to:
   - add new vlans
   - remove existing vlans
   - replace actual vlans configuration with the desirated state
- 5k*.j2 templates in the directory [**templates**](https://github.com/ksator/EVPN_DCI_automation/tree/master/templates) are QFX5k specifics
   - add new vlans
   - remove existing vlans
   - replace actual vlans configuration with the desirated state

#### playbooks
- **pb.render*.yml** playbooks render templates. They dont connect to junos devices
- **pb.rollback.yml** playbook performs a rollback on junos devices. 
- **pb.addvlans.yml** playbook configure the devices with new vlans
- **pb.removevlans.yml** playbook removes vlans from devices
- **pb.check.vlans.yml** playbook checks from devices operationnal states if vlans are presents
- **pb.replacevlans.yml** playbook enforces the desirated state on the devices
- **pb.get.junos.facts.yml** playbook gets the junos facts from the devices  
  
### how to clone this repo: 
```
git clone https://github.com/ksator/EVPN_DCI_automation.git  
cd EVPN_DCI_automation
```
### requirements on ubuntu:  
sudo pip install ansible==2.2.3  
sudo ansible-galaxy install Juniper.junos    
sudo pip install jxmlease  
install junos-eznc (pyez) and its dependencies  
 
### Junos requirement: 
Enable netconf and make sure you can reach that port on the juniper device  from your laptop  

### Looking for more details about junos automation with Ansible?
You can visit these repositories:   
https://github.com/ksator/ansible-training-for-junos-automation  
https://github.com/JNPRAutomate/ansible-junos-examples  
https://github.com/dgjnpr/ansible-template-for-junos  


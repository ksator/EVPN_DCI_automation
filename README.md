### About this repo:  
Content for an EVPN_DCI_automation demo 

### What to find in this repo: 
ansible playbooks are **pb.*.yml** files at the root of the repository.    
ansible inventory file is **hosts** file at the root of the repository.    
ansible configuration file is **ansible.cfg** at the root of the repository.   
jinja templates are j2 files in the directory **templates**.    
variables are yml files under **group_vars** and **host_vars** directories.   

#### templates
https://github.com/ksator/EVPN_DCI_automation/tree/master/templates 

#### variables 

#### playbooks



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


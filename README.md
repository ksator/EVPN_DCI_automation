### About this repo:  
ansible playbooks are pb.*.yml  
ansible inventory file is hosts  
jinja templates are j2 files in the directory templates 
variables are yml files under group_vars and host_vars  

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

### Examples: 
```
root@ksator-virtual-machine:~/EVPN_DCI_automation# ansible-playbook pb.get.junos.facts.yml

PLAY [create inventory directory] **********************************************

TASK [create inventory directory] **********************************************
ok: [localhost]

PLAY [Get Facts] ***************************************************************

TASK [remove host from inventory directory] ************************************
ok: [Dori]
ok: [Theia]
ok: [QFX6]
ok: [Nori]
ok: [Superfast]
ok: [QFX11]
ok: [QFX21]
ok: [QFX24]
ok: [QFX22]
ok: [QFX23]

TASK [Retrieve information from devices running Junos] *************************
ok: [Theia]
ok: [QFX6]
ok: [Nori]
ok: [Superfast]
ok: [Dori]
ok: [QFX21]
ok: [QFX22]
ok: [QFX11]
ok: [QFX23]
ok: [QFX24]

TASK [Print some facts] ********************************************************
ok: [Superfast] => {
    "msg": "device Superfast-QFX runs version 17.3I20170907_1547_adarshr"
}
ok: [Dori] => {
    "msg": "device Dori-QFX runs version 17.3I20170911_1553_adarshr"
}
ok: [Nori] => {
    "msg": "device Nori-QFX runs version 17.3I20170907_1547_adarshr"
}
ok: [Theia] => {
    "msg": "device Theia-QFX runs version 17.3I20170907_1547_adarshr"
}
ok: [QFX6] => {
    "msg": "device QFX5100-48S-6 runs version 14.1X53-D45.3"
}
ok: [QFX11] => {
    "msg": "device QFX5100-48S3-11 runs version 14.1X53-D45.3"
}
ok: [QFX21] => {
    "msg": "device QFX5100-48S3-21 runs version 14.1X53-D45.3"
}
ok: [QFX24] => {
    "msg": "device QFX5100-48S3-24 runs version 14.1X53-D45.3"
}
ok: [QFX23] => {
    "msg": "device QFX5100-48S3-23 runs version 14.1X53-D45.3"
}
ok: [QFX22] => {
    "msg": "device QFX5100-48S3-22 runs version 14.1X53-D45.3"
}

PLAY RECAP *********************************************************************
Dori                       : ok=3    changed=0    unreachable=0    failed=0
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


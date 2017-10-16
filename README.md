[![Build Status](https://travis-ci.org/ksator/EVPN_DCI_automation.svg?branch=master)](https://travis-ci.org/ksator/EVPN_DCI_automation)

### What to find in this repo: 
Network automation content with Ansible, Jinja, YAML, Python and Travis CI.  
For a DCI demo using EVPN-VXLAN.  
With network devices running Junos accross 2 differents DC.  

The setup is already up and running. So this automation content is not used to build the setup.  
This automation content is used to update the existing setup adding/removing/replacing/auditing vlans to the DCI configuration.   

Additionally, this repo covers how to generate YAML variables (ready to be consumed by Jinja and Ansible) from a CSV file (source-controlled) using Python.  
It has also a Python script to locate a mac address (i.e that connects to all the devices to provide the interfaces associated with a learned MAC addresses). This script uses the Ansible inventory file to get the list of devices ip address.    

### Topology: 

There are 2 DC (DC1 and DC2).    

Dori, Superfast, Theia and Nori are QFX10000 devices.  
QFX21, QFX22, QFX23, QFX24, QFX6 and QFX11 are QFX5100 devices.  

EVPN-VXLAN runs on the QFX10k devices.  
L3 is done on the QFX10k devices.  
DCI (EVPN-VXLAN) is done on the QFX10000 devices.  

QFX21, QFX22, QFX23, QFX24, QFX6 and QFX11 do L2 only.  
QFX21 and 22 use MC-LAG. QFX23 and 24 use MC-LAG.    
QFX6 uses a LAG. QFX11 uses a LAG. 

![resources/topology.png](resources/topology.png)

### Repo structure 
- ansible playbooks are at the root of the repository.    
  - **pb.renderxxx.yml** playbooks render templates. They dont connect to junos devices
    - [pb.renderaddvlans.yml](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.renderaddvlans.yml) 
    - [pb.renderremovevlans.yml](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.renderremovevlans.yml)
    - [pb.renderreplacevlans.yml](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.renderreplacevlans.yml)
  - [**pb.rollback.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.rollback.yml) playbook performs a rollback on junos devices. 
  - [**pb.addvlans.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.renderaddvlans.yml) playbook configures the devices with new vlans
  - [**pb.removevlans.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.removevlans.yml) playbook removes existing vlans from devices
  - [**pb.check.vlans.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.check.vlans.yml) playbook checks if vlans are presents from devices operationnal states
  - [**pb.check.bgp.yml**](https://github.com/ksator/EVPN_DCI_automation//blob/master/pb.check.bgp.yml) playbook checks if BGP sessions are established  
  - [**pb.replacevlans.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.replacevlans.yml) playbook enforces the desired state on the devices (which is the best approach vs using [**pb.addvlans.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.renderaddvlans.yml) + [**pb.removevlans.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.removevlans.yml))
  - [**pb.get.junos.facts.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/pb.get.junos.facts.yml) playbook gets the junos facts from the devices  

- ansible inventory file is [**hosts**](https://github.com/ksator/EVPN_DCI_automation/blob/master/hosts) file at the root of the repository.    

- ansible configuration file is [**ansible.cfg**](https://github.com/ksator/EVPN_DCI_automation/blob/master/ansible.cfg) at the root of the repository.   

- jinja templates are j2 files in the directory [**templates**](https://github.com/ksator/EVPN_DCI_automation/tree/master/templates). 
  - **10kxxx.j2** templates in the directory [**templates**](https://github.com/ksator/EVPN_DCI_automation/tree/master/templates) are QFX10k specifics templates to:
    - add new vlans: [10kaddvlans.j2](https://github.com/ksator/EVPN_DCI_automation/blob/master/templates/10kaddvlans.j2)
    - remove existing vlans: [10kremovevlans.j2](https://github.com/ksator/EVPN_DCI_automation/blob/master/templates/10kremovevlans.j2)
    - replace actual vlans configuration with the desirated state: [10kreplacevlans.j2](https://github.com/ksator/EVPN_DCI_automation/blob/master/templates/10kreplacevlans.j2)
  - **5kxxx.j2** templates in the directory [**templates**](https://github.com/ksator/EVPN_DCI_automation/tree/master/templates) are QFX5k specifics templates to:
    - add new vlans: [5kaddvlans.j2](https://github.com/ksator/EVPN_DCI_automation/blob/master/templates/5kaddvlans.j2)
    - remove existing vlans: [5kremovevlans.j2](https://github.com/ksator/EVPN_DCI_automation/blob/master/templates/5kremovevlans.j2)
    - replace actual vlans configuration with the desirated state: [5kreplacevlans.j2](https://github.com/ksator/EVPN_DCI_automation/blob/master/templates/5kreplacevlans.j2)

- variables are yml files under [**group_vars**](https://github.com/ksator/EVPN_DCI_automation/tree/master/group_vars/all) and [**host_vars**](https://github.com/ksator/EVPN_DCI_automation/tree/master/host_vars) directories.   
  - host specific variables are yml files under the directory [**host_vars**](https://github.com/ksator/EVPN_DCI_automation/tree/master/host_vars).   
  - group related variables are yml files under the directory [**group_vars**](https://github.com/ksator/EVPN_DCI_automation/tree/master/group_vars) 
  - [**generate_yml_vars.py**](https://github.com/ksator/EVPN_DCI_automation/blob/master/generate_yml_vars.py) generates yaml variables for Ansible from the [**CSV**](https://github.com/ksator/EVPN_DCI_automation/blob/master/vars.csv) file.  

- templates are rendered into the directory [**render**](https://github.com/ksator/EVPN_DCI_automation/tree/master/render)

- Junos configuration files are saved automatically before any change into the directory [**backup**](https://github.com/ksator/EVPN_DCI_automation/tree/master/backup)

- Junos configuration diffs from rollbacks done with ansible are in the directory [**rollback**](https://github.com/ksator/EVPN_DCI_automation/tree/master/rollback) 

- Python scripts are at the root of the repository  
  - [**findmac.py**](https://github.com/ksator/EVPN_DCI_automation/blob/master/findmac.py) locates a mac address accross the network.  
  - [**generate_yml_vars.py**](https://github.com/ksator/EVPN_DCI_automation/blob/master/generate_yml_vars.py) generates yaml variables for Ansible from the [**CSV**](https://github.com/ksator/EVPN_DCI_automation/blob/master/test.csv) file.  

- a [**CSV**](https://github.com/ksator/EVPN_DCI_automation/blob/master/vars.csv) file at the root of the repository  

- The CI configuration files [**.travis.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/.travis.yml) and [**requirements.txt**](https://github.com/ksator/EVPN_DCI_automation/blob/master/requirements.txt) at the root of this repository 


### Continuous integration with Travis CI

The Ansible playbooks and Python scripts in  this repository are tested automatically by [**Travis CI**](https://travis-ci.org/ksator/EVPN_DCI_automation).  
Travis CI is notified by github at each git push and pull request events. This triggers new builds.  
The files [**.travis.yml**](https://github.com/ksator/EVPN_DCI_automation/blob/master/.travis.yml) and [**requirements.txt**](https://github.com/ksator/EVPN_DCI_automation/blob/master/requirements.txt) at the root of this repository are used for this.  
For ansible playbooks that doesnt interact with Junos devices, they are executed. If there is a syntax error, Travis will fail the build.      
The command ansible-playbook has a built in option to check only the playbook's syntax (--syntax-check). This is how Travis is testing the playbooks that interact with Junos. Travis CI doesnt actually connect to the devices. If there is a syntax error, Travis will fail the build.  
The same logic is applied to the python scripts.  

The last build status is: [![Build Status](https://travis-ci.org/ksator/EVPN_DCI_automation.svg?branch=master)](https://travis-ci.org/ksator/EVPN_DCI_automation)  
The details are available [here](https://travis-ci.org/ksator/EVPN_DCI_automation)  


### How to use this repo 

#### Requirements 

##### Requirements on ubuntu 16.04:
```
sudo apt-get install -y python-dev libxml2-dev python-pip libxslt1-dev build-essential libssl-dev libffi-dev
sudo pip install jxmlease netaddr cryptography==1.2.1 junos-eznc pytest pytest-cov coveralls ansible==2.2.3
sudo ansible-galaxy --force install Juniper.junos 
 ```
 
##### Requirements on Junos: 
Enable netconf and make sure you can reach that port on the juniper device  from your laptop  
```
set system service netconf ssh
commit
```

#### get the remote repo content locally: 
```
git clone https://github.com/ksator/EVPN_DCI_automation.git 
```
```
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

##### Edit the [csv file](https://github.com/ksator/EVPN_DCI_automation/blob/master/test.csv)  
```
nano vars.csv 
```
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
##### Execute [this python script](https://github.com/ksator/EVPN_DCI_automation/blob/master/generate_yml_vars.py)
```
python ./generate_yml_vars.py
```
##### check the [variables](https://github.com/ksator/EVPN_DCI_automation/blob/master/README.md#variables)   
```
git diff group_vars/DC1/vlans.yml
```
```
git diff group_vars/DC2/vlans.yml
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
#### render the templates locally if you want to see the configuration files that are going to be generated: 

##### Generate the configuration that has the desired state (best approach, declarative approach)
```
# ansible-playbook pb.renderreplacevlans.yml 

PLAY [create render directory] *************************************************

TASK [create render directory] *************************************************
ok: [localhost]

PLAY [render template for QFX10k] **********************************************

TASK [remove files from render directory] **************************************
changed: [Superfast]
changed: [Dori]
changed: [Nori]
changed: [Theia]

TASK [Render template for QFX10k] **********************************************
changed: [Theia]
changed: [Superfast]
changed: [Nori]
changed: [Dori]

PLAY [render template for QFX5k] ***********************************************

TASK [remove files from render directory] **************************************
changed: [QFX6]
changed: [QFX21]
changed: [QFX11]
changed: [QFX23]
changed: [QFX22]
changed: [QFX24]

TASK [Render template for QFX5k] ***********************************************
changed: [QFX23]
changed: [QFX11]
changed: [QFX21]
changed: [QFX22]
changed: [QFX6]
changed: [QFX24]

PLAY RECAP *********************************************************************
Dori                       : ok=2    changed=2    unreachable=0    failed=0   
Nori                       : ok=2    changed=2    unreachable=0    failed=0   
QFX11                      : ok=2    changed=2    unreachable=0    failed=0   
QFX21                      : ok=2    changed=2    unreachable=0    failed=0   
QFX22                      : ok=2    changed=2    unreachable=0    failed=0   
QFX23                      : ok=2    changed=2    unreachable=0    failed=0   
QFX24                      : ok=2    changed=2    unreachable=0    failed=0   
QFX6                       : ok=2    changed=2    unreachable=0    failed=0   
Superfast                  : ok=2    changed=2    unreachable=0    failed=0   
Theia                      : ok=2    changed=2    unreachable=0    failed=0   
localhost                  : ok=1    changed=0    unreachable=0    failed=0   
```
```
# ls render/*_replacevlans.conf
render/Dori_replacevlans.conf   render/QFX23_replacevlans.conf
render/Nori_replacevlans.conf   render/QFX24_replacevlans.conf
render/QFX11_replacevlans.conf  render/QFX6_replacevlans.conf
render/QFX21_replacevlans.conf  render/Superfast_replacevlans.conf
render/QFX22_replacevlans.conf  render/Theia_replacevlans.conf
```
```
# more render/Superfast_replacevlans.conf 
replace:
vlans {
    VLAN201 {
        vlan-id 201;
        l3-interface irb.201;
        vxlan {
            vni 20201;
        }
    }
    VLAN202 {
        vlan-id 202;
        l3-interface irb.202;
        vxlan {
            vni 20202;
        }
    }
    VLAN207 {
        vlan-id 207;
        l3-interface irb.207;
        vxlan {
            vni 20207;
        }
    }
    VLAN208 {
        vlan-id 208;
        l3-interface irb.208;
        vxlan {
            vni 20208;
        }
    }
    VLAN2000 {
        vlan-id 2000;
    }
}
interfaces {
    replace:
    irb {
        unit 201 {
            family inet {
                address 10.201.0.3/16 {
                    virtual-gateway-address 10.201.0.1;
                }
            }
            virtual-gateway-v4-mac 00:25:01:00:00:01;
        }
        unit 202 {
            family inet {
                address 10.202.0.3/16 {
                    virtual-gateway-address 10.202.0.1;
                }
            }
            virtual-gateway-v4-mac 00:25:02:00:00:01;
        }
        unit 207 {
            family inet {
                address 10.207.0.3/16 {
                    virtual-gateway-address 10.207.0.1;
                }
            }
            virtual-gateway-v4-mac 00:25:07:00:00:01;
        }
        unit 208 {
            family inet {
                address 10.208.0.3/16 {
                    virtual-gateway-address 10.208.0.1;
                }
            }
            virtual-gateway-v4-mac 00:25:08:00:00:01;
        }
    }
}
protocols {
    replace:
    pim {
        interface irb.201 {
            distributed-dr;
           }
        interface irb.202 {
            distributed-dr;
           }
        interface irb.207 {
            distributed-dr;
           }
        interface irb.208 {
            distributed-dr;
           }
        rp {
            static {
                address 100.1.1.254;
           }
        }
        interface all {
            mode sparse;
           }
        interface fxp0.0 {
           disable;
           }
        join-load-balance;
    }
    replace:
    igmp-snooping {
        vlan VLAN201 {
            proxy;
        }
        vlan VLAN202 {
            proxy;
        }
        vlan VLAN207 {
            proxy;
        }
        vlan VLAN208 {
            proxy;
        }
    }
}
```

##### Generate the configuration to delete vlans (not the ideal approach)  
```
# ansible-playbook pb.renderremovevlans.yml 

PLAY [create render directory] *************************************************

TASK [create render directory] *************************************************
ok: [localhost]

PLAY [render template for QFX10k] **********************************************

TASK [remove files from render directory] **************************************
changed: [Superfast]
changed: [Nori]
changed: [Dori]
changed: [Theia]

TASK [Render template for QFX10k] **********************************************
changed: [Superfast]
changed: [Dori]
changed: [Nori]
changed: [Theia]

PLAY [render template for QFX5k] ***********************************************

TASK [remove files from render directory] **************************************
changed: [QFX21]
changed: [QFX11]
changed: [QFX6]
changed: [QFX23]
changed: [QFX22]
changed: [QFX24]

TASK [Render template for QFX5k] ***********************************************
changed: [QFX6]
changed: [QFX22]
changed: [QFX11]
changed: [QFX23]
changed: [QFX21]
changed: [QFX24]

PLAY RECAP *********************************************************************
Dori                       : ok=2    changed=2    unreachable=0    failed=0   
Nori                       : ok=2    changed=2    unreachable=0    failed=0   
QFX11                      : ok=2    changed=2    unreachable=0    failed=0   
QFX21                      : ok=2    changed=2    unreachable=0    failed=0   
QFX22                      : ok=2    changed=2    unreachable=0    failed=0   
QFX23                      : ok=2    changed=2    unreachable=0    failed=0   
QFX24                      : ok=2    changed=2    unreachable=0    failed=0   
QFX6                       : ok=2    changed=2    unreachable=0    failed=0   
Superfast                  : ok=2    changed=2    unreachable=0    failed=0   
Theia                      : ok=2    changed=2    unreachable=0    failed=0   
localhost                  : ok=1    changed=0    unreachable=0    failed=0   
```
```
# ls render/*_removevlans.set
render/Dori_removevlans.set   render/QFX23_removevlans.set
render/Nori_removevlans.set   render/QFX24_removevlans.set
render/QFX11_removevlans.set  render/QFX6_removevlans.set
render/QFX21_removevlans.set  render/Superfast_removevlans.set
render/QFX22_removevlans.set  render/Theia_removevlans.set
```

##### Generate the configuration to add vlans (not the ideal approach) 
```
# ansible-playbook pb.renderaddvlans.yml 

PLAY [create render directory] *************************************************

TASK [create render directory] *************************************************
ok: [localhost]

PLAY [render template for QFX10k] **********************************************

TASK [remove files from render directory] **************************************
changed: [Dori]
changed: [Superfast]
changed: [Nori]
changed: [Theia]

TASK [Render template for QFX10k] **********************************************
changed: [Dori]
changed: [Theia]
changed: [Superfast]
changed: [Nori]

PLAY [render template for QFX5k] ***********************************************

TASK [remove files from render directory] **************************************
changed: [QFX11]
changed: [QFX6]
changed: [QFX23]
changed: [QFX21]
changed: [QFX22]
changed: [QFX24]

TASK [Render template for QFX5k] ***********************************************
changed: [QFX21]
changed: [QFX6]
changed: [QFX11]
changed: [QFX22]
changed: [QFX23]
changed: [QFX24]

PLAY RECAP *********************************************************************
Dori                       : ok=2    changed=2    unreachable=0    failed=0   
Nori                       : ok=2    changed=2    unreachable=0    failed=0   
QFX11                      : ok=2    changed=2    unreachable=0    failed=0   
QFX21                      : ok=2    changed=2    unreachable=0    failed=0   
QFX22                      : ok=2    changed=2    unreachable=0    failed=0   
QFX23                      : ok=2    changed=2    unreachable=0    failed=0   
QFX24                      : ok=2    changed=2    unreachable=0    failed=0   
QFX6                       : ok=2    changed=2    unreachable=0    failed=0   
Superfast                  : ok=2    changed=2    unreachable=0    failed=0   
Theia                      : ok=2    changed=2    unreachable=0    failed=0   
localhost                  : ok=1    changed=0    unreachable=0    failed=0   
```
```
# ls render/*_addvlans.conf  
render/Dori_addvlans.conf   render/QFX23_addvlans.conf
render/Nori_addvlans.conf   render/QFX24_addvlans.conf
render/QFX11_addvlans.conf  render/QFX6_addvlans.conf
render/QFX21_addvlans.conf  render/Superfast_addvlans.conf
render/QFX22_addvlans.conf  render/Theia_addvlans.conf

```
#### enforce the desired state against the network (best approach, declarative approach): 

##### execute this playbook in dry-run mode to know what changes will happens on one specific device:
```
ansible-playbook pb.replacevlans.yml --check --diff --limit Superfast 
```
##### execute this playbook to enforce the desired state against the network: 
```
ansible-playbook pb.replacevlans.yml
ls backup
```

##### verify if the desited vlans are configured properly on devices
```
ansible-playbook pb.check.vlans.yml
```

#### login on junos devices and run some show commands: 
```
show system commit
```
```
show configuration | compare rollback 1
```
```
show configuration vlans 
```
#### rollback the setup to the previous state: 
```
ansible-playbook pb.rollaback --extra-vars rbid=1 
ls rollback
```
#### additionnal playbooks (not ideal as more imperative approach)

##### execute this playbook if you want to remove vlans: 

```
ansible-playbook pb.check.vlans.yml
ansible-playbook pb.removevlans.yml 
ls backup
```
##### execute this playbook if you want to add vlans: 
```
ansible-playbook pb.addvlans.yml
ls backup
ansible-playbook pb.check.vlans.yml
```
#### search for a mac address accross the network
```
python ./findmac.py 38:4f:49:f2:5f:fc
```

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


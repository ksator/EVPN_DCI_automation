[![Build Status](https://travis-ci.org/ksator/EVPN_DCI_automation.svg?branch=master)](https://travis-ci.org/ksator/EVPN_DCI_automation)

### What to find in this repo: 
Network automation content with Ansible, Jinja, YAML, Python and Travis CI.  
- For a DCI demo using EVPN-VXLAN.  
- With network devices running Junos. Accross 2 differents DC.  

The setup is already up and running. So this automation content is not used to build the setup.  
This automation content is used to update the existing setup managing (stitching/unstitching/configuring/auditing ...) vlans to the DCI configuration. It uses a declarative approach and enforces the desired state against the network.    

This repo covers also how to generate YAML variables (ready to be consumed by Jinja and Ansible) from a CSV file (source-controlled) using Python.  

It has also a Python script to locate a mac address (i.e that connects to all the devices to provide the interfaces associated with a learned MAC addresses). This script uses the Ansible inventory file to get the list of devices ip address.    

### Repository content

[The documentation is on wiki](https://github.com/ksator/EVPN_DCI_automation/wiki)

- [What to find in this repo](https://github.com/ksator/EVPN_DCI_automation/wiki/What-to-find-in-this-repo)
- [Network topology](https://github.com/ksator/EVPN_DCI_automation/wiki/Network-topology)
- [Repository structure](https://github.com/ksator/EVPN_DCI_automation/wiki/Repository-structure)
- [Requirements to use this repo](https://github.com/ksator/EVPN_DCI_automation/wiki/Requirements-to-use-this-repo)
- [How to get the remote repo content locally](https://github.com/ksator/EVPN_DCI_automation/wiki/How-to-get-the-remote-repo-content-locally)
- [How to generate yaml variables for ansible from a csv file](https://github.com/ksator/EVPN_DCI_automation/wiki/How-to-generate-yaml-variables-for-ansible-from-a-csv-file)
- [How to run the VLANs stitching management demo](https://github.com/ksator/EVPN_DCI_automation/wiki/How-to-run-the-VLANs-stitching-management-demo)
- [how to retry a playbook for the devices that failed](https://github.com/ksator/EVPN_DCI_automation/wiki/how-to-retry-a-playbook-for-the-devices-that-failed)
- [How to search for a mac address accross the network](https://github.com/ksator/EVPN_DCI_automation/wiki/How-to-search-for-a-mac-address-accross-the-network)
- [Continuous integration with Travis CI](https://github.com/ksator/EVPN_DCI_automation/wiki/Continuous-integration-with-Travis-CI)
- [Slack integration](https://github.com/ksator/EVPN_DCI_automation/wiki/Slack-integration)
- [Looking for more details about junos automation with Ansible?](https://github.com/ksator/EVPN_DCI_automation/wiki/Looking-for-more-details-about-junos-automation-with-Ansible%3F)
- [Looking for more junos automation content for EVPN VXLAN?](https://github.com/ksator/EVPN_DCI_automation/wiki/Looking-for-more-junos-automation-content-for-EVPN-VXLAN%3F)



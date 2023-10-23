# Network Automation Project
This is a repository for the capstone project by Ming Xia and Mark Rodriguez.


## Topology
![image](https://github.com/zerolength/NetworkAutomationProj/assets/14089278/8183233e-1b77-415d-bc11-dc5a8149a436)


## Prerequisites
- pip install graphviz
- sudo apt-get install graphviz
- sudo apt install dnsmasq -y
- sudo apt install bridge-utils


## Description of Main Files
_network_topology.yml_ - This file is the data structure for the overall network topology for the project.
This document is used as the structure for the network. It contains the below categories:
- Subnets
- Routers
- Hosts
_main.py_ - This file is the primary script for generating the virtual network. It pulls the structure from _network_toplogy.yml_. It contains the following classes:
- Routers()
  - Has add_default() method for adding default route
  - add_net method for attach to subnet and define gateway
- Subnets()
  - Defines the property of each subnet
  - Tracks whether if the host or router is associated with the subnet
- Host()
  - can have more than 1 interface.
- statically coded associateion between routers and hosts. Those can easily changed by invoking methods such as add_host from subnet() or add_net from router()
- NAT configuration from rodriguezmarkd@
- Start flask service by importing flaskviz.py
 
_networktests.yml_ - This is an ansible script that performs end-to-end testing for the virtual network. Information is then output into networktestsresults.log in JSON format. #from rodriguezmarkd@
- "IP Configuration Readout from Each Host" - Pulls the command 'ip -c link' from each host to verify configuration information.
- "Pinging Outward" - This task performs a simple ping from each host to 8.8.8.8.
- "Pinging from hosts to core router" - This task tests LAN functionality within the virtual network.
- "Show Results" - This task outputs the results to the screen
- "Outputting results to file..." - This task creates the log file

_flaskvis.py_ this is a python file that produce above visualization

_vm_
- Scripts originally from rodriguezmarkd@ . Modified for compatibility
_vm/net-config-1.yaml_
- defines 1st VM
_vm/net-config-2.yaml_
- defines 2nd VM
_user-data.yaml_
- defines common userdata used in VM creation
_vm.sh_
- script use above configuration to create vm via qemu commandline.

_cleaner.sh_ 
- simple cleaning script in bash. Cleans any residual network configuration produced during test. Note some classes have already included desctructor methods. Pending update.
  

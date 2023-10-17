#!/usr/bin/env python
#parser.py
import subprocess
import yaml

def importer(filename):
    with open(filename, "r") as stream:
        try:
            assembly = yaml.safe_load(stream)
            print(assembly)
        except yaml.YAMLError as exc:
            print(exc)
    return assembly

class Subnet ():
    def __init__ (self, nsname, bridge, ip, cidr, gw, dhcp_range):
        self.nsname =  nsname
        self.bridge = bridge
        self.ip = ip
        self.cidr = cidr
        self.gw = gw
        self.dhcp = dhcp_range #this need to be split into begin and end
        print(self.ip)
        print(self.nsname)
        print(self.bridge)
        #sudo ip netns add ohost
        subprocess.run(["sudo","ip","netns","add",nsname]) 

    def __del__ (self):
        subprocess.run(["sudo","ip","netns","del",self.nsname]) 
class Router ():
    def __init__ (self, rname, interfaces)
        self.rname = rname
        self.inf = interfaces
        #add routing code here
    def __del__ (self):
    
def main ():
    filename = "network_topology.yml"
    assembly = importer(filename)
    subnets = assembly ['subnets']
    sholder = []   
    print (subnets)
    for object in subnets:
        new_subnets = Subnet (nsname=object['name'],bridge=object['bridge'],ip=object['subnet_ip'])
        holder.append(new_subnets)
    print (holder)
    routers = assembly ['routers']
    rholder = []
    for object in routers:
        new_router = Router (rname = oject['name'], interfaces = object[interfaces])
    
    input("Press Enter to continue...you can check if netns is up")
if __name__ == "__main__":
    main()

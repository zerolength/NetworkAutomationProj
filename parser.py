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
def ip2subnet(ip, subnet):
    #this function will check ip against subnet and vice versa, fillin in if one is empty

    
    return ip, subnet
def link_ns (ns1, ns2):
    #given 2 namespace and create veth to link them
    #sudo ip link add crout2orout type veth peer name orout2crout
    #sudo ip link set crout2orout netns crouter
    #sudo ip link set orout2crout netns orouter
    linkname= ns1+"-to-"+ns2
    subprocess.run(["sudo","ip","link","add",ns1+"-to-"+ns2,"type","veth","peer","name",ns1+"-to-"+ns2])
    subprocess.run(["sudo","ip","link","set",ns1+"-to-"+ns2,"netns",ns1])
    subprocess.run(["sudo","ip","link","set",ns2+"-to-"+ns1,"netns",ns2])
    
    return linkname
def unlink_ns (ns1, ns2):
    #delete veth yet to implement
    
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


    def __del__ (self):
        subprocess.run(["sudo","ip","netns","del",self.nsname]) 
class Router ():
    def __init__ (self, rname, interfaces)
        self.rname = rname
        #sudo ip netns add ohost
        subprocess.run(["sudo","ip","netns","add",rname]) 
        self.inf = interfaces
        self.links = []
        for interface in interfaces
            [ns1,ns2] = interface['name'].split("-to-") #need testning
            newlink=link_ns (ns1,ns2)
            self.links.append(newlink)
        #add routing code here
        #connect interfaces
    def __del__ (self):
    
def main ():
    filename = "network_topology.yml"
    assembly = importer(filename)
    subnets = assembly ['subnets']
    sholder = []   
    print (subnets)
    for object in subnets:
        new_subnets = Subnet (nsname=object['name'],bridge=object['bridge'],ip=object['subnet_ip'])
        sholder.append(new_subnets)
    print (holder)
    routers = assembly ['routers']
    rholder = []
    for object in routers:
        new_router = Router (rname = oject['name'], interfaces = object[interfaces])
        rholder.append(new_router)
    input("Press Enter to continue...you can check if netns is up")
if __name__ == "__main__":
    main()

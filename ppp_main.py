#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
from mininet.topo import Topo, SingleSwitchTopo
import socket
from socket import timeout
import time

def myNetwork():
    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    info( '*** Add switches\n')

    info( '*** Add hosts\n')



    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)

    

    h1h2 = {'bw':100}
    net.addLink(h1,h2, cls=TCLink, **h1h2)

    info( '*** Starting network\n')
    net.start()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')

    info( '*** Post configure switches and hosts\n')

    p1 = h2.popen(f'sudo python3 ppp_server.py')

    h1.cmd(f'sudo python3 ppp_client.py')

    


    # Send the packet pairs and record the timestamps
    
    # Stop the network
    CLI(net)
    p1.terminate()
    net.stop()



if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

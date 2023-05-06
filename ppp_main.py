#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
from mininet.term import makeTerm

from mininet.util import dumpNodeConnections

bandwidth = 5

def myNetwork(bandwidth):
    net = Mininet( topo=None,
                   build=False,
                   ipBase='192.168.0.0/16')
    info( '* Adding controller\n' )
    info( '* Add switches\n')
    r1 = net.addSwitch('r1', cls=Node)
    r1.cmd('sysctl -w net.ipv4.ip_forward=1')
    r2 = net.addSwitch('r2', cls=Node)
    r2.cmd('sysctl -w net.ipv4.ip_forward=1')

    info( '* Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='192.168.0.103/24', defaultRoute='via 192.168.0.1')
    h2 = net.addHost('h2', cls=Host, ip='192.168.1.2/24', defaultRoute='via 192.168.1.1')
    h3 = net.addHost('h3', cls=Host, ip='192.168.3.11/24',defaultRoute='via 192.168.3.1')
    h4 = net.addHost('h4', cls=Host, ip='192.168.4.2/24',defaultRoute='via 192.168.4.1')


    info( '* Add links\n')
    h1r1 = {'bw':bandwidth}
    net.addLink(h1, r1, intfName2='r1-eth0', params2={'ip':'192.168.0.1/24'},**h1r1)
    r1r2 = {'bw':bandwidth}
    net.addLink(r1, r2, intfName1='r1-eth1', intfName2='r2-eth0', params1={'ip':'192.168.2.1/24'}, params2={'ip':'192.168.2.2/24'},**r1r2)
    r2h2 = {'bw':bandwidth}
    net.addLink(r2, h2, intfName1='r2-eth1', params1={'ip':'192.168.1.1/24'},**r2h2)
    h3r1 = {'bw':bandwidth}   
    net.addLink(h3, r1, intfName1='h3-eth0',intfName2='r1-eth2', params1={'ip':'192.168.3.11/24'}, params2={'ip':'192.168.3.1/24'},**h3r1)
    h2r4 = {'bw':bandwidth}   
    net.addLink(r2, h4, intfName1='r2-eth2', infName2='h4-eth0', params1={'ip':'192.168.4.1/24'}, params2={'ip':'192.168.4.2/24'},**h2r4)

    print(dumpNodeConnections(net.hosts))

    info( '* Starting network\n')
    net.build()

    h1_term = makeTerm(h1,title = "client")
    h2_term = makeTerm(h2,title = "server")
    h3_term = makeTerm(h3,title = "iperf client")
    h4_term = makeTerm(h4,title = "iperf server")
    
    info( '* Post configure switches and hosts\n')

    
    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork(bandwidth)





#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import OVSBridge  # Import the simple switch
from mininet.log import setLogLevel, info

def create_and_test_network():
    "Create a network using a simple, compatible switch."

    # This is the key change: we are explicitly telling Mininet
    # which type of switch to use.
    net = Mininet(switch=OVSBridge)

    info('*** Adding hosts (server and clients)\n')
    server = net.addHost('server', ip='10.0.0.1')
    client1 = net.addHost('client1', ip='10.0.0.2')
    client2 = net.addHost('client2', ip='10.0.0.3')

    info('*** Adding switch\n')
    # The addSwitch command will now use the OVSBridge type we specified
    s1 = net.addSwitch('s1')

    info('*** Creating links\n')
    net.addLink(server, s1)
    net.addLink(client1, s1)
    net.addLink(client2, s1)

    info('*** Starting network\n')
    net.start()

    info('*** Testing network connectivity\n')
    # Run a non-interactive test
    net.pingAll()

    info('*** Stopping network\n')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_and_test_network()
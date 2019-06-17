<html><head><meta charset="GB2312"><title>project2.zip myFatTree.py</title>
<LINK href="/inc/read_style.css" type=text/css rel=stylesheet></head>
<body>
<p><a href=http://www.pudn.com>www.pudn.com</a> &gt; <a href="http://www.pudn.com/Download/item/id/2991809.html">project2.zip</a> &gt myFatTree.py, change:2016-01-09,size:5867b</p><!-- saved from http://www.pudn.com -->
<script src="/inc/gg_read1.js"></script><BR>
<pre name="code" class="py">
#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
#from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      port=6637)

    info( '*** Add switches\n')
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch)
    s18 = net.addSwitch('s18', cls=OVSKernelSwitch)
    s10 = net.addSwitch('s10', cls=OVSKernelSwitch)
    s16 = net.addSwitch('s16', cls=OVSKernelSwitch)
    s11 = net.addSwitch('s11', cls=OVSKernelSwitch)
    s9 = net.addSwitch('s9', cls=OVSKernelSwitch)
    s17 = net.addSwitch('s17', cls=OVSKernelSwitch)
    s13 = net.addSwitch('s13', cls=OVSKernelSwitch)
    s19 = net.addSwitch('s19', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s12 = net.addSwitch('s12', cls=OVSKernelSwitch)
    s20 = net.addSwitch('s20', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s15 = net.addSwitch('s15', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s14 = net.addSwitch('s14', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h5 = net.addHost('h5', cls=Host, ip='10.1.0.2', defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='10.2.0.2', defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.2.0.3', defaultRoute=None)
    h11 = net.addHost('h11', cls=Host, ip='10.2.1.2', defaultRoute=None)
    h12 = net.addHost('h12', cls=Host, ip='10.2.1.3', defaultRoute=None)
    h13 = net.addHost('h13', cls=Host, ip='10.3.0.2', defaultRoute=None)
    h14 = net.addHost('h14', cls=Host, ip='10.3.0.3', defaultRoute=None)
    h15 = net.addHost('h15', cls=Host, ip='10.3.1.2', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h16 = net.addHost('h16', cls=Host, ip='10.3.1.3', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.1.2', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.1.3', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.1.1.3', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.1.0.3', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.1.1.2', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(s1, h1)
    net.addLink(s1, h2)
    net.addLink(s2, h3)
    net.addLink(s2, h4)
    net.addLink(s5, h5)
    net.addLink(s5, h6)
    net.addLink(s6, h7)
    net.addLink(s6, h8)
    net.addLink(s9, h9)
    net.addLink(s9, h10)
    net.addLink(s10, h11)
    net.addLink(s10, h12)
    net.addLink(s13, h13)
    net.addLink(s13, h14)
    net.addLink(s14, h15)
    net.addLink(s14, h16)
    net.addLink(s3, s1)
    net.addLink(s3, s2)
    net.addLink(s4, s1)
    net.addLink(s4, s2)
    net.addLink(s7, s5)
    net.addLink(s7, s6)
    net.addLink(s8, s5)
    net.addLink(s8, s6)
    net.addLink(s11, s9)
    net.addLink(s11, s10)
    net.addLink(s12, s9)
    net.addLink(s12, s10)
    net.addLink(s15, s13)
    net.addLink(s15, s14)
    net.addLink(s16, s13)
    net.addLink(s16, s14)
    net.addLink(s17, s3)
    net.addLink(s17, s7)
    net.addLink(s17, s11)
    net.addLink(s17, s15)
    net.addLink(s3, s18)
    net.addLink(s18, s7)
    net.addLink(s18, s11)
    net.addLink(s18, s15)
    net.addLink(s4, s19)
    net.addLink(s8, s19)
    net.addLink(s12, s19)
    net.addLink(s16, s19)
    net.addLink(s20, s4)
    net.addLink(s20, s8)
    net.addLink(s20, s12)
    net.addLink(s20, s16)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s6').start([c0])
    net.get('s7').start([c0])
    net.get('s8').start([c0])
    net.get('s18').start([c0])
    net.get('s10').start([c0])
    net.get('s16').start([c0])
    net.get('s11').start([c0])
    net.get('s9').start([c0])
    net.get('s17').start([c0])
    net.get('s13').start([c0])
    net.get('s19').start([c0])
    net.get('s2').start([c0])
    net.get('s1').start([c0])
    net.get('s3').start([c0])
    net.get('s12').start([c0])
    net.get('s20').start([c0])
    net.get('s4').start([c0])
    net.get('s15').start([c0])
    net.get('s5').start([c0])
    net.get('s14').start([c0])

    info( '*** Post configure switches and hosts\n')
    s6.cmd('ifconfig s6 10.1.1.1')
    s7.cmd('ifconfig s7 10.1.2.1')
    s8.cmd('ifconfig s8 10.1.3.1')
    s18.cmd('ifconfig s18 10.4.1.2')
    s10.cmd('ifconfig s10 10.2.1.1')
    s16.cmd('ifconfig s16 10.3.3.1')
    s11.cmd('ifconfig s11 10.2.2.1')
    s9.cmd('ifconfig s9 10.2.0.1')
    s17.cmd('ifconfig s17 10.4.1.1')
    s13.cmd('ifconfig s13 10.3.0.1')
    s19.cmd('ifconfig s19 10.4.2.1')
    s2.cmd('ifconfig s2 10.0.1.1')
    s1.cmd('ifconfig s1 10.0.0.1')
    s3.cmd('ifconfig s3 10.0.2.1')
    s12.cmd('ifconfig s12 10.2.3.1')
    s20.cmd('ifconfig s20 10.4.2.2')
    s4.cmd('ifconfig s4 10.0.3.1')
    s15.cmd('ifconfig s15 10.3.2.1')
    s14.cmd('ifconfig s14 10.3.1.1')
    s5.cmd('ifconfig s5 10.1.0.1')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

</pre>
<script src="/inc/gg_read2.js"></script><BR>
</body></html>

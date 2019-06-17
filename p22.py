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


    info( '*** Add switches\n')
    s15 = net.addSwitch('s15', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s19 = net.addSwitch('s19', cls=OVSKernelSwitch)
    s18 = net.addSwitch('s18', cls=OVSKernelSwitch)
    s9 = net.addSwitch('s9', cls=OVSKernelSwitch)
    s13 = net.addSwitch('s13', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s10 = net.addSwitch('s10', cls=OVSKernelSwitch)
    s16 = net.addSwitch('s16', cls=OVSKernelSwitch)
    s14 = net.addSwitch('s14', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s12 = net.addSwitch('s12', cls=OVSKernelSwitch)
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch)
    s17 = net.addSwitch('s17', cls=OVSKernelSwitch)
    s20 = net.addSwitch('s20', cls=OVSKernelSwitch)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s11 = net.addSwitch('s11', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h4 = net.addHost('h4', cls=Host, ip='10.0.1.3',mac='00:00:00:00:01:03', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.1.0.3',mac='00:00:00:01:00:03',  defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.3',mac='00:00:00:00:00:03',  defaultRoute=None)
    h12 = net.addHost('h12', cls=Host, ip='10.2.1.3',mac='00:00:00:02:01:03',  defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.1.0.2',mac='00:00:00:01:00:02',  defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.2.0.3',mac='00:00:00:02:00:03',  defaultRoute=None)
    h11 = net.addHost('h11', cls=Host, ip='10.2.1.2',mac='00:00:00:02:01:02',  defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.1.1.3',mac='00:00:00:01:01:03',  defaultRoute=None)
    h13 = net.addHost('h13', cls=Host, ip='10.3.0.2',mac='00:00:00:03:00:02',  defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.1.1.2',mac='00:00:00:01:01:02',  defaultRoute=None)
    h14 = net.addHost('h14', cls=Host, ip='10.3.0.3',mac='00:00:00:03:00:03',  defaultRoute=None)
    h15 = net.addHost('h15', cls=Host, ip='10.3.1.2',mac='00:00:00:03:01:02',  defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.2',mac='00:00:00:00:00:02',  defaultRoute=None)
    h16 = net.addHost('h16', cls=Host, ip='10.3.1.3',mac='00:00:00:03:01:03',  defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.1.2',mac='00:00:00:00:01:02',  defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='10.2.0.2',mac='00:00:00:02:00:02',  defaultRoute=None)
    
    info( '*** Add links\n')
    net.addLink(s1, s5)
    net.addLink(s1, s9)
    net.addLink(s1, s13)
    net.addLink(s1, s17)
    net.addLink(s2, s5)
    net.addLink(s2, s9)
    net.addLink(s2, s13)
    net.addLink(s2, s17)
    net.addLink(s3, s6)
    net.addLink(s3, s10)
    net.addLink(s3, s14)
    net.addLink(s3, s18)
    net.addLink(s4, s6)
    net.addLink(s4, s10)
    net.addLink(s4, s14)
    net.addLink(s4, s18)

    net.addLink(s5, s7)
    net.addLink(s5, s8)
    net.addLink(s6, s7)
    net.addLink(s6, s8)
    net.addLink(s9, s11)
    net.addLink(s9, s12)
    net.addLink(s10, s11)
    net.addLink(s10, s12)
    net.addLink(s13, s15)
    net.addLink(s13, s16)
    net.addLink(s14, s15)
    net.addLink(s14, s16)
    net.addLink(s17, s19)
    net.addLink(s17, s20)
    net.addLink(s18, s19)
    net.addLink(s18, s20)

    net.addLink(s7, h1)
    net.addLink(s7, h2)
    net.addLink(s8, h3)
    net.addLink(s8, h4)
    net.addLink(s11, h5)
    net.addLink(s11, h6)
    net.addLink(s12, h7)
    net.addLink(s12, h8)
    net.addLink(s15, h9)
    net.addLink(s15, h10)
    net.addLink(s16, h11)
    net.addLink(s16, h12)
    net.addLink(s19, h13)
    net.addLink(s19, h14)
    net.addLink(s20, h15)
    net.addLink(s20, h16)

    info( '*** Starting network\n')
    net.build()
    

    info( '*** Starting switches\n')
    net.get('s15').start([])
    net.get('s7').start([])
    net.get('s5').start([])
    net.get('s19').start([])
    net.get('s18').start([])
    net.get('s9').start([])
    net.get('s13').start([])
    net.get('s2').start([])
    net.get('s3').start([])
    net.get('s10').start([])
    net.get('s16').start([])
    net.get('s14').start([])
    net.get('s6').start([])
    net.get('s4').start([])
    net.get('s12').start([])
    net.get('s8').start([])
    net.get('s17').start([])
    net.get('s20').start([])
    net.get('s1').start([])
    net.get('s11').start([])

    info( '*** Post configure switches and hosts\n')
    s2.cmd('ifconfig s2 10.4.1.2')
    s3.cmd('ifconfig s3 10.4.2.1')
    s4.cmd('ifconfig s4 10.4.2.2')
    s1.cmd('ifconfig s1 10.4.1.1')
    s5.cmd('ifconfig s5 10.0.2.1')
    s6.cmd('ifconfig s6 10.0.3.1')
    s7.cmd('ifconfig s7 10.0.0.1')
    s8.cmd('ifconfig s8 10.0.1.1')
    s9.cmd('ifconfig s9 10.1.2.1')
    s10.cmd('ifconfig s10 10.1.3.1')
    s12.cmd('ifconfig s12 10.1.0.1')
    s11.cmd('ifconfig s11 10.1.1.1')
    s13.cmd('ifconfig s13 10.2.2.1')
    s14.cmd('ifconfig s14 10.2.3.1')
    s15.cmd('ifconfig s15 10.2.0.1')
    s16.cmd('ifconfig s16 10.2.1.1')
    s17.cmd('ifconfig s17 10.3.2.1')
    s18.cmd('ifconfig s18 10.3.3.1')
    s19.cmd('ifconfig s19 10.3.0.1')
    s20.cmd('ifconfig s20 10.3.1.1')

   
    info('*** Set ARP\n')
    h_list = [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16]
    info('*** Set ARP\n')
    for i in range(16):
	    h_list[i].setARP('10.0.0.2','00:00:00:00:00:02')
	    h_list[i].setARP('10.0.0.3','00:00:00:00:00:03') 
	    h_list[i].setARP('10.0.1.3','00:00:00:00:01:03')
	    h_list[i].setARP('10.0.1.2','00:00:00:00:01:02')
	    h_list[i].setARP('10.1.0.2','00:00:00:01:00:02')
	    h_list[i].setARP('10.1.0.3','00:00:00:01:00:03')
	    h_list[i].setARP('10.1.1.2','00:00:00:01:01:02')
	    h_list[i].setARP('10.1.1.3','00:00:00:01:01:03')
	    h_list[i].setARP('10.2.0.2','00:00:00:02:00:02')
	    h_list[i].setARP('10.2.0.3','00:00:00:02:00:03')
	    h_list[i].setARP('10.2.1.2','00:00:00:02:01:02')
	    h_list[i].setARP('10.2.1.3','00:00:00:02:01:03')
	    h_list[i].setARP('10.3.0.2','00:00:00:03:00:02')
	    h_list[i].setARP('10.3.0.3','00:00:00:03:00:03')
	    h_list[i].setARP('10.3.1.2','00:00:00:03:01:02')
	    h_list[i].setARP('10.3.1.3','00:00:00:03:01:03')
 #   s8.cmd(r'ovs-ofctl add-flow s8 dl_dst=00:00:00:00:01:03,actions=output:4' )
#    s8.cmd(r'ovs-ofctl add-flow s8 dl_dst=00:00:00:00:01:02,actions=output:3' )
    
#edge1
    edgeS1=[s7,s11,s15,s19,s8,s12,s16,s20]
    eS=['s7','s11','s15','s19','s8','s12','s16','s20']
    for i in range(8):
    	if i!=0:
		edgeS1[i].cmd(r'ovs-ofctl add-flow '+eS[i]+' dl_dst=00:00:00:00:00:02,actions=output:1' )
		edgeS1[i].cmd(r'ovs-ofctl add-flow '+eS[i]+' dl_dst=00:00:00:00:00:03,actions=output:1' )
    	if i!=1:
		edgeS1[i].cmd(r'ovs-ofctl add-flow '+eS[i]+' dl_dst=00:00:00:01:00:02,actions=output:1' )
		edgeS1[i].cmd(r'ovs-ofctl add-flow '+eS[i]+' dl_dst=00:00:00:01:00:03,actions=output:1' )
    	if i!=2:
		edgeS1[i].cmd(r'ovs-ofctl add-flow '+eS[i]+' dl_dst=00:00:00:02:00:02,actions=output:1' )
		edgeS1[i].cmd(r'ovs-ofctl add-flow '+eS[i]+' dl_dst=00:00:00:02:00:03,actions=output:1' )
    	if i!=3:
		edgeS1[i].cmd(r'ovs-ofctl add-flow '+eS[i]+' dl_dst=00:00:00:03:00:02,actions=output:1' )
		edgeS1[i].cmd(r'ovs-ofctl add-flow '+eS[i]+' dl_dst=00:00:00:03:00:03,actions=output:1' )
    	if i!=4:
		edgeS1[i].cmd(r'ovs-ofctl add-flow '+eS[i]+' dl_dst=00:00:00:00:01:02,actions=output:2' )
		edgeS1[i].cmd(r'ovs-ofctl add-flow '+eS[i]+' dl_dst=00:00:00:00:01:03,actions=output:2' )
    	if i!=5:
		edgeS1[i].cmd(r'ovs-ofctl add-flow '+eS[i]+' dl_dst=00:00:00:01:01:02,actions=output:2' )
		edgeS1[i].cmd(r'ovs-ofctl add-flow '+eS[i]+' dl_dst=00:00:00:01:01:03,actions=output:2' )
    	if i!=6:
		edgeS1[i].cmd(r'ovs-ofctl add-flow '+eS[i]+' dl_dst=00:00:00:02:01:02,actions=output:2' )
		edgeS1[i].cmd(r'ovs-ofctl add-flow '+eS[i]+' dl_dst=00:00:00:02:01:03,actions=output:2' )
    	if i!=7:
		edgeS1[i].cmd(r'ovs-ofctl add-flow '+eS[i]+' dl_dst=00:00:00:03:01:02,actions=output:2' )
		edgeS1[i].cmd(r'ovs-ofctl add-flow '+eS[i]+' dl_dst=00:00:00:03:01:03,actions=output:2' )

    aggS1=[s5,s9,s13,s17,s6,s10,s14,s18]
    eS3=['s5','s9','s13','s17','s6','s10','s14','s18']
    for i in range(8):
	if i!=0:
		
		aggS1[i].cmd(r'ovs-ofctl add-flow '+eS3[i]+' dl_dst=00:00:00:00:00:02,actions=output:1' )
		aggS1[i].cmd(r'ovs-ofctl add-flow '+eS3[i]+' dl_dst=00:00:00:00:00:03,actions=output:2' )
	if i!=4:
		aggS1[i].cmd(r'ovs-ofctl add-flow '+eS3[i]+' dl_dst=00:00:00:00:01:02,actions=output:1' )
		aggS1[i].cmd(r'ovs-ofctl add-flow '+eS3[i]+' dl_dst=00:00:00:00:01:03,actions=output:2' )
	if i!=1:
		
		aggS1[i].cmd(r'ovs-ofctl add-flow '+eS3[i]+' dl_dst=00:00:00:01:00:02,actions=output:1' )
		aggS1[i].cmd(r'ovs-ofctl add-flow '+eS3[i]+' dl_dst=00:00:00:01:00:03,actions=output:2' )

	if i!=5:
		
		aggS1[i].cmd(r'ovs-ofctl add-flow '+eS3[i]+' dl_dst=00:00:00:01:01:02,actions=output:1' )
		aggS1[i].cmd(r'ovs-ofctl add-flow '+eS3[i]+' dl_dst=00:00:00:01:01:03,actions=output:2' )
	if i!=2:
		
		aggS1[i].cmd(r'ovs-ofctl add-flow '+eS3[i]+' dl_dst=00:00:00:02:00:02,actions=output:1' )
		aggS1[i].cmd(r'ovs-ofctl add-flow '+eS3[i]+' dl_dst=00:00:00:02:00:03,actions=output:2' )
	if i!=6:
		
		aggS1[i].cmd(r'ovs-ofctl add-flow '+eS3[i]+' dl_dst=00:00:00:02:01:02,actions=output:1' )
		aggS1[i].cmd(r'ovs-ofctl add-flow '+eS3[i]+' dl_dst=00:00:00:02:01:03,actions=output:2' )
	if i!=3:
		
		aggS1[i].cmd(r'ovs-ofctl add-flow '+eS3[i]+' dl_dst=00:00:00:03:00:02,actions=output:1' )
		aggS1[i].cmd(r'ovs-ofctl add-flow '+eS3[i]+' dl_dst=00:00:00:03:00:03,actions=output:2' )
	if i!=7:
		
		aggS1[i].cmd(r'ovs-ofctl add-flow '+eS3[i]+' dl_dst=00:00:00:03:01:02,actions=output:1' )
		aggS1[i].cmd(r'ovs-ofctl add-flow '+eS3[i]+' dl_dst=00:00:00:03:01:03,actions=output:2' )

    coreS=[s1,s2,s3,s4]
    eS4=['s1','s2','s3','s4']
    for i in range(4):
	coreS[i].cmd(r'ovs-ofctl add-flow '+eS4[i]+' dl_dst=00:00:00:00:00:02,actions=output:1' )
	coreS[i].cmd(r'ovs-ofctl add-flow '+eS4[i]+' dl_dst=00:00:00:00:00:03,actions=output:1' )
	coreS[i].cmd(r'ovs-ofctl add-flow '+eS4[i]+' dl_dst=00:00:00:00:01:02,actions=output:1' )
	coreS[i].cmd(r'ovs-ofctl add-flow '+eS4[i]+' dl_dst=00:00:00:00:01:03,actions=output:1' )

	coreS[i].cmd(r'ovs-ofctl add-flow '+eS4[i]+' dl_dst=00:00:00:01:00:02,actions=output:2' )
	coreS[i].cmd(r'ovs-ofctl add-flow '+eS4[i]+' dl_dst=00:00:00:01:00:03,actions=output:2' )
	coreS[i].cmd(r'ovs-ofctl add-flow '+eS4[i]+' dl_dst=00:00:00:01:01:02,actions=output:2' )
	coreS[i].cmd(r'ovs-ofctl add-flow '+eS4[i]+' dl_dst=00:00:00:01:01:03,actions=output:2' )

	coreS[i].cmd(r'ovs-ofctl add-flow '+eS4[i]+' dl_dst=00:00:00:02:00:02,actions=output:3' )
	coreS[i].cmd(r'ovs-ofctl add-flow '+eS4[i]+' dl_dst=00:00:00:02:00:03,actions=output:3' )
	coreS[i].cmd(r'ovs-ofctl add-flow '+eS4[i]+' dl_dst=00:00:00:02:01:02,actions=output:3' )
	coreS[i].cmd(r'ovs-ofctl add-flow '+eS4[i]+' dl_dst=00:00:00:02:01:03,actions=output:3' )

	coreS[i].cmd(r'ovs-ofctl add-flow '+eS4[i]+' dl_dst=00:00:00:03:00:02,actions=output:4' )
	coreS[i].cmd(r'ovs-ofctl add-flow '+eS4[i]+' dl_dst=00:00:00:03:00:03,actions=output:4' )
	coreS[i].cmd(r'ovs-ofctl add-flow '+eS4[i]+' dl_dst=00:00:00:03:01:02,actions=output:4' )
	coreS[i].cmd(r'ovs-ofctl add-flow '+eS4[i]+' dl_dst=00:00:00:03:01:03,actions=output:4' )

    aggS2=[s5,s6]
    eS5=['s5','s6']
    for i in range(2):
	aggS2[i].cmd(r'ovs-ofctl add-flow '+eS5[i]+' dl_dst=00:00:00:00:00:02,actions=output:3' )
	aggS2[i].cmd(r'ovs-ofctl add-flow '+eS5[i]+' dl_dst=00:00:00:00:00:03,actions=output:3' )
	aggS2[i].cmd(r'ovs-ofctl add-flow '+eS5[i]+' dl_dst=00:00:00:00:01:02,actions=output:4' )
	aggS2[i].cmd(r'ovs-ofctl add-flow '+eS5[i]+' dl_dst=00:00:00:00:01:03,actions=output:4' )
    aggS3=[s9,s10]
    eS6=['s9','s10']
    for i in range(2):
	aggS3[i].cmd(r'ovs-ofctl add-flow '+eS6[i]+' dl_dst=00:00:00:01:00:02,actions=output:3' )
	aggS3[i].cmd(r'ovs-ofctl add-flow '+eS6[i]+' dl_dst=00:00:00:01:00:03,actions=output:3' )
	aggS3[i].cmd(r'ovs-ofctl add-flow '+eS6[i]+' dl_dst=00:00:00:01:01:02,actions=output:4' )
	aggS3[i].cmd(r'ovs-ofctl add-flow '+eS6[i]+' dl_dst=00:00:00:01:01:03,actions=output:4' )
    aggS4=[s13,s14]
    eS7=['s13','s14']
    for i in range(2):
	aggS4[i].cmd(r'ovs-ofctl add-flow '+eS7[i]+' dl_dst=00:00:00:02:00:02,actions=output:3' )
	aggS4[i].cmd(r'ovs-ofctl add-flow '+eS7[i]+' dl_dst=00:00:00:02:00:03,actions=output:3' )
	aggS4[i].cmd(r'ovs-ofctl add-flow '+eS7[i]+' dl_dst=00:00:00:02:01:02,actions=output:4' )
	aggS4[i].cmd(r'ovs-ofctl add-flow '+eS7[i]+' dl_dst=00:00:00:02:01:03,actions=output:4' )
    aggS5=[s17,s18]
    eS8=['s17','s18']
    for i in range(2):
	aggS5[i].cmd(r'ovs-ofctl add-flow '+eS8[i]+' dl_dst=00:00:00:03:00:02,actions=output:3' )
	aggS5[i].cmd(r'ovs-ofctl add-flow '+eS8[i]+' dl_dst=00:00:00:03:00:03,actions=output:3' )
	aggS5[i].cmd(r'ovs-ofctl add-flow '+eS8[i]+' dl_dst=00:00:00:03:01:02,actions=output:4' )
	aggS5[i].cmd(r'ovs-ofctl add-flow '+eS8[i]+' dl_dst=00:00:00:03:01:03,actions=output:4' )

    edgeS2=[s7,s8]
    eS1=['s7','s8']
    for i in range(2):
	if i!=1:
		edgeS2[i].cmd(r'ovs-ofctl add-flow '+eS1[i]+' dl_dst=00:00:00:00:00:02,actions=output:3' )
		edgeS2[i].cmd(r'ovs-ofctl add-flow '+eS1[i]+' dl_dst=00:00:00:00:00:03,actions=output:4' )
	if i!=0:
		edgeS2[i].cmd(r'ovs-ofctl add-flow '+eS1[i]+' dl_dst=00:00:00:00:01:02,actions=output:3' )
		edgeS2[i].cmd(r'ovs-ofctl add-flow '+eS1[i]+' dl_dst=00:00:00:00:01:03,actions=output:4' )
    edgeS3=[s11,s12]
    eS9=['s11','s12']
    for i in range(2):
	if i!=1:
		edgeS3[i].cmd(r'ovs-ofctl add-flow '+eS9[i]+' dl_dst=00:00:00:01:00:02,actions=output:3' )
		edgeS3[i].cmd(r'ovs-ofctl add-flow '+eS9[i]+' dl_dst=00:00:00:01:00:03,actions=output:4' )
		
	if i!=0:
		edgeS3[i].cmd(r'ovs-ofctl add-flow '+eS9[i]+' dl_dst=00:00:00:01:01:02,actions=output:3' )
		edgeS3[i].cmd(r'ovs-ofctl add-flow '+eS9[i]+' dl_dst=00:00:00:01:01:03,actions=output:4' )
    edgeS4=[s15,s16]
    eS10=['s15','s16']
    for i in range(2):
	if i!=1:
		edgeS4[i].cmd(r'ovs-ofctl add-flow '+eS10[i]+' dl_dst=00:00:00:02:00:02,actions=output:3' )
		edgeS4[i].cmd(r'ovs-ofctl add-flow '+eS10[i]+' dl_dst=00:00:00:02:00:03,actions=output:4' )

	if i!=0:
		edgeS4[i].cmd(r'ovs-ofctl add-flow '+eS10[i]+' dl_dst=00:00:00:02:01:02,actions=output:3' )
		edgeS4[i].cmd(r'ovs-ofctl add-flow '+eS10[i]+' dl_dst=00:00:00:02:01:03,actions=output:4' )
    edgeS5=[s19,s20]
    eS11=['s19','s20']
    for i in range(2):
	if i!=1:
		edgeS5[i].cmd(r'ovs-ofctl add-flow '+eS11[i]+' dl_dst=00:00:00:03:00:02,actions=output:3' )
		edgeS5[i].cmd(r'ovs-ofctl add-flow '+eS11[i]+' dl_dst=00:00:00:03:00:03,actions=output:4' )

	if i!=0:
		edgeS5[i].cmd(r'ovs-ofctl add-flow '+eS11[i]+' dl_dst=00:00:00:03:01:02,actions=output:3' )
		edgeS5[i].cmd(r'ovs-ofctl add-flow '+eS11[i]+' dl_dst=00:00:00:03:01:03,actions=output:4' )



    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()


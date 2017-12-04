from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class FatTree( Topo ):
    	
    def __init__(self):
	
    	"""Create a fat-tree network"""

    	net = Mininet( controller=RemoteController )
    	c0 = RemoteController( 'c0', ip='127.0.0.1', port=6633 )

    	info( '*** Adding controller ***\n' )
   	net.addController(c0 )

    	## Core switches
   	info(' *** Core switches ***\n')
    	cs_0 = net.addSwitch( 'cs0' )    
    	cs_1 = net.addSwitch( 'cs1' )
    	cs_2 = net.addSwitch( 'cs2' )
    	cs_3 = net.addSwitch( 'cs3' )

    	################################################## 
    	## Pod 0
    	info( '*** Pod - 0 ***\n' )
    	info( '*** Adding switches ***\n' )
   	edge_sw_0 = net.addSwitch( 'edge_sw_0' )
    	edge_sw_1 = net.addSwitch( 'edge_sw_1' ) 
    	aggr_sw_2 = net.addSwitch( 'aggr_sw_2' )
    	aggr_sw_3 = net.addSwitch( 'aggr_sw_3' )

    	info( '*** Adding hosts ***\n' )
    	# Lower left
    	h0 = net.addHost( 'h0', ip='10.0.0.2' )
    	h1 = net.addHost( 'h1', ip='10.0.0.3' )
    	# Lower right
    	h2 = net.addHost( 'h2', ip='10.0.1.2' )
    	h3 = net.addHost( 'h3', ip='10.0.1.3' )

    	info( '*** Creating links ***\n' )
    	net.addLink( h0, edge_sw_0 )
    	net.addLink( h1, edge_sw_0 )
    	net.addLink( h2, edge_sw_1 )
    	net.addLink( h3, edge_sw_1 )
    
    	net.addLink( edge_sw_0, aggr_sw_2)
    	net.addLink( edge_sw_0, aggr_sw_3)
    	net.addLink( edge_sw_1, aggr_sw_2)
    	net.addLink( edge_sw_1, aggr_sw_3)    
    
	net.addLink( cs_0, aggr_sw_2)
	net.addLink( cs_1, aggr_sw_2)

	net.addLink( cs_2, aggr_sw_3)
	net.addLink( cs_3, aggr_sw_3)

    	#################################################
    	## Pod 1
    	info( '*** Pod - 1 ***\n' )
    	info( '*** Adding switches ***\n' )
    	edge_sw_4 = net.addSwitch( 'edge_sw_4' )
    	edge_sw_5 = net.addSwitch( 'edge_sw_5' )
    	aggr_sw_6 = net.addSwitch( 'aggr_sw_6' )
    	aggr_sw_7 = net.addSwitch( 'aggr_sw_7' )

    	info( '*** Adding hosts ***\n' )
    	# Lower left
    	h4 = net.addHost( 'h4', ip='10.1.0.2' )
    	h5 = net.addHost( 'h5', ip='10.1.0.3' )
    	# Lower right   
    	h6 = net.addHost( 'h6', ip='10.1.1.2' )
    	h7 = net.addHost( 'h7', ip='10.1.1.3' )

    	info( '*** Creating links ***\n' )
    	net.addLink( h4, edge_sw_4 )
   	net.addLink( h5, edge_sw_4 )
    	net.addLink( h6, edge_sw_5 )
    	net.addLink( h7, edge_sw_5 )

    	net.addLink( edge_sw_4, aggr_sw_6)
    	net.addLink( edge_sw_4, aggr_sw_7)
    	net.addLink( edge_sw_5, aggr_sw_6)
    	net.addLink( edge_sw_5, aggr_sw_7)

	net.addLink( cs_0, aggr_sw_6)
        net.addLink( cs_1, aggr_sw_6)

        net.addLink( cs_2, aggr_sw_7)
        net.addLink( cs_3, aggr_sw_7) 

    	################################################
    	## Pod 2
    	info( '*** Pod - 2 ***\n' )
    	info( '*** Adding switches ***\n' )
    	edge_sw_8 = net.addSwitch( 'edge_sw_8' )
    	edge_sw_9 = net.addSwitch( 'edge_sw_9' )
    	aggr_sw_10 = net.addSwitch( 'aggr_sw_10' )
    	aggr_sw_11 = net.addSwitch( 'aggr_sw_11' )

    	info( '*** Adding hosts ***\n' )
    	# Lower left
    	h8 = net.addHost( 'h8', ip='10.2.0.2' )
   	h9 = net.addHost( 'h9', ip='10.2.0.3' )
    	# Lower right   
    	h10 = net.addHost( 'h10', ip='10.2.1.2' )
    	h11 = net.addHost( 'h11', ip='10.2.1.3' )

    	info( '*** Creating links ***\n' )
    	net.addLink( h8, edge_sw_8 )
    	net.addLink( h9, edge_sw_8 )
    	net.addLink( h10, edge_sw_9 )
    	net.addLink( h11, edge_sw_9 )

    	net.addLink( edge_sw_8, aggr_sw_10)
    	net.addLink( edge_sw_8, aggr_sw_11)
    	net.addLink( edge_sw_9, aggr_sw_10)
    	net.addLink( edge_sw_9, aggr_sw_11)

	net.addLink( cs_0, aggr_sw_10)
        net.addLink( cs_1, aggr_sw_10)

        net.addLink( cs_2, aggr_sw_11)
        net.addLink( cs_3, aggr_sw_11)

    	##############################################
    	## Pod 3
    	info( '*** Pod - 3 ***\n' )
    	info( '*** Adding switches ***\n' )
    	edge_sw_12 = net.addSwitch( 'edge_sw_12' )
    	edge_sw_13 = net.addSwitch( 'edge_sw_13' )
    	aggr_sw_14 = net.addSwitch( 'aggr_sw_14' )
    	aggr_sw_15 = net.addSwitch( 'aggr_sw_15' )
  
    	info( '*** Adding hosts ***\n' )
    	# Lower left
    	h12 = net.addHost( 'h12', ip='10.3.0.2' )
    	h13 = net.addHost( 'h13', ip='10.3.0.3' )
    	# Lower right   
    	h14 = net.addHost( 'h14', ip='10.3.1.2' )
    	h15 = net.addHost( 'h15', ip='10.3.1.3' )
  
    	info( '*** Creating links ***\n' )
    	net.addLink( h12, edge_sw_12 )
    	net.addLink( h13, edge_sw_12 )
    	net.addLink( h14, edge_sw_13 )
    	net.addLink( h15, edge_sw_13 )
  
    	net.addLink( edge_sw_12, aggr_sw_14)
    	net.addLink( edge_sw_12, aggr_sw_15)
    	net.addLink( edge_sw_13, aggr_sw_14)
    	net.addLink( edge_sw_13, aggr_sw_15) 

	net.addLink( cs_0, aggr_sw_14)
        net.addLink( cs_1, aggr_sw_14)

        net.addLink( cs_2, aggr_sw_15)
        net.addLink( cs_3, aggr_sw_15)

	net.build()
	net.start()
	CLI(net)
	net.stop()	

topos = { 'FatTree': ( lambda: FatTree() ) }


from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # hosts
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )
        
        # switches
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )

        # Add links
        self.addLink( h1, s1 )
        self.addLink( h2, s1 )
        self.addLink( s1, s2 )
        self.addLink( s2, s3, bw=5, delay='20ms', loss=10 )
        self.addLink( s3, s4, bw=15, delay='40ms', loss=2 )
        self.addLink( h3, s3 )
        self.addLink( h4, s4 )

topos = { 'topo': ( lambda: MyTopo() ) }

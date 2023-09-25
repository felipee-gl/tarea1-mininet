from mininet.topo import Topo

class MyTopo4( Topo ):
    "Simple topology example."

    def build( self ):

        # hosts
        h_Chile = self.addHost( 'h1' )
        h_Australia = self.addHost( 'h2' )
        
        # switches
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )

        # Add links
        self.addLink( h_Chile, s1 )
        self.addLink( s1, s2, bw=250, delay='150ms', loss=5 )
        self.addLink( s2, s3, bw=100, delay='70ms', loss=4 )
        self.addLink( s3, s4, bw=150, delay='200ms', loss=3 )
        self.addLink( h_Australia, s4 )

topos = { 'topo': ( lambda: MyTopo4() ) }

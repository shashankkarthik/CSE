
import pylab

def draw_graph( x, y ):
    '''Plot x vs. y (lists of numbers of same length)'''

    # Title for the graph and labels for the axes
    pylab.title( "Change in Global Mean Temperature" )
    pylab.xlabel( "Year" )
    pylab.ylabel( "Temperature Deviation" )

    # Create and display the plot
    pylab.plot( x, y )
    pylab.show()


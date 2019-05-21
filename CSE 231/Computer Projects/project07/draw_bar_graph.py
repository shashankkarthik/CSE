import pylab
def draw_bar_graph(x,y):
    '''Draw a bar graph of y values with labels from x where
       x is a list of strings; y is a list of values associated with each x'''
    number_of_bars = len(x)
    bar_width = 0.5
    # create a list (array) of indices for bars
    x_values = pylab.linspace(0,number_of_bars-1,number_of_bars)
    # associate a string label (tick) from x with each bar
    # orient the string to the middle of the bar, and rotate the label 45 degrees
    pylab.xticks(x_values+bar_width/2, x, rotation=45)
    
    # Title for the graph and labels for the axes
    pylab.title( "Inflation-adjusted Cost for Hearings" )
    pylab.ylabel( "Cost (in millions of 2015 dollars)" )
    
    pylab.bar(x_values,y,width=bar_width)
    pylab.show()
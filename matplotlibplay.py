import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

data = {'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60}

# For labels, we can specify custom formatting guidelines in the form of functions by using the ticker.FuncFormatter class.
# Below we'll define a function that takes an integer as input, and returns a string as an output.
def currency(x, pos):
    """The two argurments are the value and tick position"""
    if x > 1E6:
        s = '${:1.1f}M'.format(x*1e-6)
    else:
        s = '${:1.0f}K'.format(x*1e-3)
    return s

def lifecycleExample():
    # Data for the plot
    group_data = list(data.values())
    group_names = list(data.keys())
    group_mean = np.mean(group_data)

    # Create the plot
    fig, ax = plt.subplots(figsize = (20, 8))                   # "fig" is the canvas (figure) and "ax" is the visualization (axes) on the canvas 
    ax.barh(group_names, group_data)                            # Creates a bar graph for the instance of the axes
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment='right')  # We can pass in a list of customizations for the plot all at once rather than an attribute at a time
    #plt.style.use('fivethirtyeight')                           # 'fivethirtyeight' is the style to be used when plotting data. The style controls many things, such as color, linewidths, backgrounds, etc.


    # Add a vertical line, here we set the style in the function call
    ax.axvline(group_mean, ls='--', color='r')

    # Customize the plot
    formatter = FuncFormatter(currency)                 # We can then apply the currency formatter to the labels on our plot. 
    ax.xaxis.set_major_formatter(formatter)             # To do this, we'll use the xaxis attribute of our axis. This lets you perform actions on a specific axis on our plot.
    plt.rcParams.update({'figure.autolayout': True})    # We can tell Matplotlib to automatically make room for elements in the figures by setting the autolayout value of our rcParams.
    ax.set(xlim=[0, max(group_data)], xlabel='Total Revenue', ylabel='Company', title='Company Revenue')

    # Annotate new companies
    for group in [3, 5, 8]:
        ax.text(max(group_data)+1000, group, "New Company", fontsize=10, verticalalignment="center")

    plt.gca().xaxis.grid(True)  #Shows the x axis grid only
    plt.show()

def main():
    print('Hello World')

if __name__ == '__main__':
    lifecycleExample()
    main()


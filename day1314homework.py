
# put the imports first

# create a function that returns a list of random dice throws
# it should have two parameters
# - number of dice in each throw, default 4
# - number of throws, default 100

# even better would be a another function to which you give the list of dice throws and it 
# plots the histogram
# this function would have two parameters
# - the list of dice throws - no default
# - the name of the file to save the plot to - default - empty string
# if the file name is empty string, the plot should be shown on the screen

# use the first function to create a list of 1000 dice throws with 6 dice in each throw
# pass the result to 2nd function to plot the histogram and save it to a file
# BONUS: file name should have current date and time in it


# ideally you would then run them from main guard
# which means this file would be a module, that can be imported
from datetime import datetime
import random
import matplotlib.pyplot as plt
import numpy as np

def dice(n=4, t=100):
    itemss=[]
    # itemsumm=[]
    for m in range(t):
        for v in range(n):
            x = [random.randint(0, 7)]
            itemss.append(x)
        # itemsumm.append(tuple(itemss))  wanted to do with sum too but can't figure out yet where how to place itemsum  
    return itemss #, itemsumm
# item, itemsum = dice(4, 10)    

#made this by trial&error from different examples, can't find a normal (QUICKREAD....) list of modules/functions and param/args/attributes,
#e.g. I don't understand what specifically ax refers to, it seems eg plt.title() and ax.set_title() are interchangeable but are they?
def histo(x, fname='' ):
    fig,ax = plt.subplots()
    fig = plt.figure(figsize=(10,5))
    a = np.array(x)
    plt.hist(a, bins = range(0, 7, 1), color='green' ) # don't know how to center bins on 1,2,3,4,5,6
    plt.title("histogram of dice throws")
    plt.xticks([1,2,3,4,5,6])
    plt.xlabel('dice side instances')
    plt.ylabel('frequency')
 
    if fname == '':
        plt.show()
    else:
        # split_name = fname.split('.')
        # split_name.insert(2, str(datetime.now()))
        # fname = ''.join(split_name) 
        fig.savefig(fname, bbox_inches='tight', dpi=150)

dice(6,1000)
histo(dice(), 'lala.jpg')

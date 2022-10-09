# TODO
# 1. plot a graph of x and y
# x would be values from -10 to 10 (21 values)
# y would be the cube of x + 5

# you could use a different library than matplotlib but it is the most popular one
# will will explore other ones later on in the course

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
# x = np.linspace(0, 10, 100)
# y = 4 + 2 * np.sin(2 * x)
# x and y could be lists of values
x = list(range(-10, 10))
y = [(n +5)**3 for n in x]
# z = list(range(10))

# plot
fig, ax = plt.subplots() # i assume ax is the plot line item but unsure which aspect determines it's only one line, is it pyplot, is it plot

ax.plot(x, y, linewidth=10.0)

# fig, ax1 = plt.subplots()
# ax1.plot(3, z, linewidth=3.0)

plt.show()
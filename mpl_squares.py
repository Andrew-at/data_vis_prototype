#A Higgs
# SETI Data visualizer
#
""""visualization tool utilizing API data from Seti and/or local weather"""

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

plt.show()
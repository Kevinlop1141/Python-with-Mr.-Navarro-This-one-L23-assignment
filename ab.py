#Thank you so much
#https://www.geeksforgeeks.org/plotting-sine-and-cosine-graph-using-matloplib-in-python/
#They provided the ode in the bottom
#Because I did not ask Mr. Navvarro for code o~o

import numpy as np
import matplotlib.pyplot as plt

def Goodbye():
    # Creating x axis with range and y axis with Sine
    # Function for Plotting Sine Graph
    x = np.arange(0, 5*np.pi, 0.1)
    y = np.sin(x)

    # Plotting Sine Graph
    plt.plot(x, y, color='green')
    plt.show()

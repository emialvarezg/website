import numpy as np
import matplotlib.pyplot as plt
from pyscript import display
#para cosas de gráficas
#import networkx as nx
#import pydot
#from networkx.drawing.nx_pydot import graphviz_layout

display("prueba")

x=np.linspace(0,1,100)
y=x**2
fig = plt.plot(x,y)

display(fig,target="graf")

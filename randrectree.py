import numpy as np
import matplotlib.pyplot as plt
from pyscript import display, web, when, document
#para cosas de gráficas
import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout

#-------------------------------------------------------------------------------------------------------
def rectree(n):
    T = nx.Graph()
    T.add_node(1)
    for i in range(1,n):
        v = random.choice(list(T.nodes()))
        T.add_node(i+1)
        T.add_edge(v,i+1)
    return T

#-------------------------------------------------------------------------------------------------------

@when("click", "#sample")
def generate_tree(event):
    plt.close()
    document.getElementById("rrt").innerHTML = ""
    n = int(document.getElementById("num").value)
    R =  rectree(n)

    fig, ax = plt.subplots(figsize=(9, 9))
    pos = nx.spring_layout(R)
    #pos = graphviz_layout(R, prog="dot")
    nx.draw(R, pos, node_color='forestgreen', node_size=150, with_labels=True, edge_color='saddlebrown',font_color='white',font_size='8')
    display(fig,target="rrt")
  

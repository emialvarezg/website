import numpy as np
import matplotlib.pyplot as plt
from pyscript import display, web, when, document
#para cosas de gráficas
import networkx as nx
import random


#---------------------------------------------------------------------------------------------
def rwgraph(x,y,G):
    w=[x]
    while w[-1] not in y:
        w.append(random.choice(list(G.neighbors(w[-1]))))
    return w

def le(w):
    l=[]
    while 0 < len(w):
        ind = [i for i in range(len(w)) if w[0] == w[i]]
        l.append(w[max(ind)])
        m = max(ind)+1
        w = w[m:]
    return l


def ust(G):
    U = nx.Graph()
    U.add_nodes_from(list(G.nodes()))
    
    x = random.choice(list(G.nodes()))
    v = [x]
    while 0 < len([n for n in list(G.nodes()) if n not in v]):
        y = random.choice([n for n in list(G.nodes()) if n not in v])
        w = rwgraph(y,v,G)
        l = le(w)
        for i in range(len(l)-1):
            U.add_edge(l[i],l[i+1])
        v = v+l
    return U
#-----------------------------------------------------------------------------------------

@when("click", "#sub")
def generate_ust(event):
    plt.close()
    document.getElementById("ust").innerHTML = ""
    n = int(document.getElementById("num").value)
  
    L=nx.grid_2d_graph(n,n)
    U = ust(L)
    pos = {node: node for node in U.nodes()}

    fig, ax = plt.subplots(figsize=(9, 9))
    nx.draw(U,pos,node_size=10,edge_color='royalblue',node_color='royalblue')
    display(fig,target="ust")

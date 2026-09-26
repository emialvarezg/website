import numpy as np
import matplotlib.pyplot as plt
from pyscript import display, web, when, document
#para cosas de gráficas
import networkx as nx

def percolacion(n,p):
    L=nx.grid_2d_graph(n,n)
    for edge in L.edges():
        if np.random.uniform()>p:
            L.remove_edge(edge[0],edge[1])
    return L


@when("click", "#submit")
def generate_perc(event):
    plt.close()
    document.getElementById("perc").innerHTML = ""
    n = int(document.getElementById("num").value)
    p = float(document.getElementById("prob").value)
    color = bool(document.getElementById("col").value == 'True' or document.getElementById("col").value == 'true')

    L=percolacion(n,p)

    C = sorted(nx.connected_components(L), key=len, reverse=True)
    C0 = L.subgraph(C[0]).copy()
    
    fig2, ax2 = plt.subplots(figsize=(10, 10))
    
    pos = {node: node for node in L.nodes()}
    pos2 = {node: node for node in C0.nodes()}

    fig, ax = plt.subplots(figsize=(9, 9))
    nx.draw(L,pos,node_size=0,edge_color='cornflowerblue')
    if color == True:
        nx.draw(C0,pos2,node_size=0,edge_color='darkorange')
    display(fig,target="perc")

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

    L=percolacion(n,p)
    pos = {node: node for node in L.nodes()}

    fig, ax = plt.subplots(figsize=(10, 10))
    nx.draw(L,pos,node_size=0,edge_color='darkviolet')
    display(fig,target="perc")

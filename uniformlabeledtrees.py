import numpy as np
import matplotlib.pyplot as plt
from pyscript import display, web, when, document
#para cosas de gráficas
import networkx as nx
#import pydot
#from networkx.drawing.nx_pydot import graphviz_layout



def prufer(A):
    #definimos el árbol
    T = nx.Graph()

    #etiquetas disponibles
    et = [i+1 for i in range(len(A)+2)]

    #definimos los vértices
    T.add_nodes_from(et)

    #iteramos hasta que la secuencia esté vacía
    while len(A) > 0:
        #nos fijamos en las etiquetas restantes que no aparecen en la secuencia
        disp = [j for j in et if j not in A]
        #agregamos el primer elemento del la secuencia y la menor etiqueta disponible como arista
        T.add_edge(A[0],min(disp))
        #quitamos la etiqueta y la entrada de la secuencia que utilizamos
        A.remove(A[0])
        et.remove(min(disp))
        
    #finalmenta agregamos como arista las dos etiquetas restantes    
    T.add_edge(et[0],et[1])
    return T

@when("click", "#submit-btn")
def generate_tree(event):
    plt.close()
    document.getElementById("graf2").innerHTML = ""
    n = int(document.getElementById("num").value)
    S = [np.random.randint(1,n+1) for i in range(n-2)]
    G = prufer(S)

    fig2, ax2 = plt.subplots()
    pos = nx.kamada_kawai_layout(G)
    nx.draw(G, pos, node_color='forestgreen', node_size=150, with_labels=True, edge_color='saddlebrown')
    display(fig2,target="graf2")



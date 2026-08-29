import numpy as np
import matplotlib.pyplot as plt
from pyscript import display, when, document

display('prueba')

@when("click", "#gen")
def simular(event):
    plt.close()
    document.getElementById("bm").innerHTML = ""
    n=100000
    x=0
    b = [x]
    for i in range(n):
        x+= np.sqrt(1/n)*np.random.normal()
        b.append(x)
    t = [i/n for i in range(n+1)]
    
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.plot(t,b , linewidth = 0.5, color= 'cornflowerblue')
    
    display(fig,target="bm")

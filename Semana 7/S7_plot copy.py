import herramientas.s5_funciones as ds
import matplotlib.pyplot as plt
from pathlib import Path #importar la libreria para manejar rutas de archivos

ROOT=Path(__file__).resolve().parent
TXT=ROOT/"Datos"/"mediciones_200.txt"
temperatura=[]
with open(TXT, "r", encoding="utf-8") as f:
    for linea in f:
        temperatura.append(ds.volt_a_Temp_ECT(float(linea)))
        
figtitle="grafico comparativo de valores aleatorios"
plt.title(figtitle.upper(),fontdict={"fontsize": 12, "fontweight": "bold"})
plt.ylabel("Voltajes")
plt.xlabel("Tiempo")
plt.plot(temperatura,
         color="#2D30FB", 
         marker='o', 
         linestyle='--', 
         linewidth=1, 
         markersize=3,
         label="sensor 1")
plt.legend()
plt.grid()
plt.savefig("salidas/grafico_temperatura.pdf", 
            pad_inches=0.8, 
            dpi=300, 
            edgecolor="#000000",
            facecolor="#FAFBF7")
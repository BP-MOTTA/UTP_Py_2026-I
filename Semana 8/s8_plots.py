import herramientas.s5_funciones as ds
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path #importar la libreria para manejar rutas de archivos

ROOT=Path(__file__).resolve().parent
TXT=ROOT/"Datos"/"mediciones_200.txt"
vol=np.array([])
with open(TXT, "r", encoding="utf-8") as f:
    for linea in f:
        vol=np.append(vol, float(linea))
temp=ds.volt_a_Temp_ECT(vol)
x=np.arange(1, 31)

plt.title("Plot de mediciones")
plt.xlabel("Número de medición")
plt.ylabel("Valor")
plt.grid(True)
plt.plot(x,vol[:30],
         color="#E0497E", 
         marker='o', 
         markersize=3,
         label="sensor 1")
plt.savefig("grafico_plot.png", 
            pad_inches=0.8, 
            dpi=300, 
            edgecolor="#000000",
            facecolor="#FAFBF7")
plt.close()
# -------------------------
# 2. SCATTER
# -------------------------
plt.title("Scatter de mediciones")
plt.xlabel("Número de medición")
plt.ylabel("Valor")
plt.grid(True)
plt.scatter(temp[:30],vol[:30],
         color="#48B594", 
         marker='^', 
         s=20,
         label="sensor 1")
plt.savefig("grafico_scatter.png", 
            pad_inches=0.8, 
            dpi=300, 
            edgecolor="#000000",
            facecolor="#FAFBF7")
plt.close()
# -------------------------
# 3. HISTOGRAMA
# -------------------------
plt.title("Histograma de mediciones")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.grid(True)
plt.hist(temp[:30], 
         bins=10, 
         color="#E0BA49", 
         edgecolor="#000000", 
         alpha=0.7)
plt.savefig("grafico_histograma.png", 
            pad_inches=0.8, 
            dpi=300, 
            edgecolor="#000000",
            facecolor="#FAFBF7") 
plt.close()  
#------------------------#
# 4. BOX PLOT
#------------------------#
plt.title("Boxplot de mediciones")
plt.ylabel("Valor")
plt.grid(True)
plt.boxplot(temp[:30], 
            patch_artist=True, 
            boxprops=dict(facecolor="#6A996C"))
plt.savefig("grafico_boxplot.png", 
            pad_inches=0.8, 
            dpi=300, 
            edgecolor="#EF0202",
            facecolor="#FAFBF7") 
plt.close()  
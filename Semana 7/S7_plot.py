import herramientas.s5_funciones as ds
import matplotlib.pyplot as plt

x=ds.aleatorio(20)
y=ds.aleatorio(20)
suma=[x[i]+y[i] for i in range(len(x))]
figtitle="grafico comparativo de valores aleatorios"
plt.title(figtitle.upper(),fontdict={"fontsize": 12, "fontweight": "bold"})
plt.ylabel("Voltajes")
plt.xlabel("Tiempo")
plt.plot(x,
         color="#E0497E", 
         marker='o', 
         linestyle='--', 
         linewidth=1, 
         markersize=3,
         label="sensor 1")
plt.plot(y, color="#4994E0", 
         marker='o', 
         linestyle='--', 
         linewidth=1, 
         markersize=3,
         label="sensor 2")
plt.plot(suma, color="#49E076", 
         marker='o', 
         linestyle='-', 
         linewidth=3, 
         markersize=3,
         label="suma de sensores")
plt.legend()
plt.grid()
plt.show()
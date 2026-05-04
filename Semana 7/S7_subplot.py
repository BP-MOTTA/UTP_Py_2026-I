import herramientas.s5_funciones as ds
import matplotlib.pyplot as plt
import numpy as np
n=30
x=np.arange(1,n+1)
y1=np.sin(ds.aleatorio(n))
y2=np.cos(ds.aleatorio(n))
y3=y1+y2

fig, axs = plt.subplots(3, 1, figsize=(10, 12))
figtitle="graficos comparativos de funciones trigonométricas"
fig.suptitle(figtitle.upper(), fontdict={"fontsize": 14, "fontweight": "bold"})
axs[0].set_title("Seno", fontdict={"fontsize": 12, "fontweight": "bold"})
axs[0].set_ylim(-2, 2)
axs[0].plot(x, y1, color="#E0497E", marker='o', linestyle='--')
axs[1].set_title("Coseno", fontdict={"fontsize": 12, "fontweight": "bold"})
axs[1].set_ylim(-2, 2)
axs[1].plot(x, y2, color="#4994E0", marker='o', linestyle='--')
axs[2].set_title("Suma", fontdict={"fontsize": 12, "fontweight": "bold"})
axs[2].set_ylim(-2, 2)
axs[2].plot(x, y3, color="#49E076", marker='o', linestyle='--')
axs[2].set_xlabel("Tiempo")
fig.legend(["Seno", "Coseno", "Suma"], loc="upper right")
plt.show()
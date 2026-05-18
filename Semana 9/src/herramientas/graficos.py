from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def grafico_lineal(tiempo, voltaje, salida: Path, titulo: str):
    plt.figure(figsize=(9, 4))
    plt.plot(tiempo, voltaje,
             color="#000275", 
                marker='o', 
                markersize=3)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
    plt.title(titulo, fontdict={"fontweight": "bold"})
    plt.xlabel("Tiempo")
    plt.ylabel("Voltaje (V)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(salida, dpi=300)
    plt.close()

def grafico_lineal_umbral(tiempo, voltaje, umbral_v, salida: Path, titulo: str):
    # detectar puntos en alerta
    alerta_t = [t for t, v in zip(tiempo, voltaje) if v > umbral_v]
    alerta_v = [v for v in voltaje if v > umbral_v]

    plt.figure(figsize=(9, 4))

    # línea principal
    plt.plot(
        tiempo,
        voltaje,
        color="#0039acea",
        linestyle="-",
        label="Voltaje (V)"
    )

    # puntos de alerta
    plt.scatter(
        alerta_t,
        alerta_v,
        color="#f40404d2",
        label=f"Alertas (> {umbral_v} V)"
    )

    ax = plt.gca()

    # anotaciones sobre los puntos en alerta
    for t, v in zip(alerta_t, alerta_v):
        ax.annotate(
            f"{v:.2f} V",
            xy=(t, v),
            xytext=(0, 8),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=8
        )

    # línea horizontal del umbral
    plt.axhline(
        umbral_v,
        color="#fd9800d2",
        linestyle=":",
        label=f"Umbral {umbral_v} V"
    )

    ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))

    plt.title(titulo, fontdict={"fontweight": "bold"})
    plt.xlabel("Tiempo")
    plt.ylabel("Voltaje (V)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.savefig(salida, dpi=400)
    plt.close()

def histograma_voltaje(voltaje, salida: Path, titulo: str):
    plt.figure(figsize=(6, 4))
    plt.hist(voltaje, bins=30, edgecolor="black")
    plt.title(titulo, fontdict={"fontweight": "bold"})
    plt.xlabel("Voltaje (V)")
    plt.ylabel("Frecuencia")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(salida, dpi=300)
    plt.close()

def boxplot_voltaje_legacy(voltaje, salida: Path, titulo: str): #programa principal
    plt.figure(figsize=(6, 4))
    plt.boxplot(voltaje, vert=True)
    plt.title(titulo, fontdict={"fontweight": "bold"})
    plt.ylabel("Voltaje (V)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(salida, dpi=300)
    plt.close()
    
def boxplot_todos_los_archivos(listas_voltaje, etiquetas, salida: Path, titulo: str):
    plt.figure(figsize=(10, 5))
    plt.boxplot(listas_voltaje, labels=etiquetas, vert=True)
    plt.title(titulo, fontdict={"fontweight": "bold"})
    plt.xlabel("Archivos")
    plt.ylabel("Voltaje (V)")
    plt.grid(True)
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(salida, dpi=300)
    plt.close()

def histograma_voltaje(voltaje, salida: Path, titulo: str, umbral_v=None):
    if not voltaje:
        return

    promedio = sum(voltaje) / len(voltaje)
    vmin = min(voltaje)
    vmax = max(voltaje)

    plt.figure(figsize=(8, 4.8))

    n, bins, patches = plt.hist(
        voltaje,
        bins=20,
        edgecolor="black",
        linewidth=1.0,
        alpha=0.75
    )

    # línea del promedio
    plt.axvline(
        promedio,
        color="red",
        linestyle="--",
        linewidth=2,
        label=f"Promedio = {promedio:.3f} V"
    )

    # línea del umbral si existe
    if umbral_v is not None:
        plt.axvline(
            umbral_v,
            color="orange",
            linestyle=":",
            linewidth=2,
            label=f"Umbral = {umbral_v:.2f} V"
        )

    plt.title(titulo, fontdict={"fontweight": "bold", "fontsize": 12})
    plt.xlabel("Voltaje (V)")
    plt.ylabel("Frecuencia")
    plt.grid(True, linestyle="--", alpha=0.4)

    # pequeño cuadro de texto con estadísticas
    texto = (
        f"n = {len(voltaje)}\n"
        f"mín = {vmin:.3f} V\n"
        f"máx = {vmax:.3f} V"
    )

    plt.text(
        0.98, 0.95, texto,
        transform=plt.gca().transAxes,
        ha="right",
        va="top",
        fontsize=9,
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.8)
    )

    plt.legend()
    plt.tight_layout()
    plt.savefig(salida, dpi=300)
    plt.close()
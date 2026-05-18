from pathlib import Path
import json
from herramientas.lectura import obtener_archivos_csv, leer_datos_csv
from herramientas.graficos import (
    grafico_lineal,
    grafico_lineal_umbral,
    histograma_voltaje,
    boxplot_todos_los_archivos
)
from herramientas.analisis import analizar_valores

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "processed"
PLOTS_DIR = ROOT / "plots"
PLOTS_DIR.mkdir(parents=True, exist_ok=True)
STATICS_DIR = ROOT / "STATICS"
STATICS_DIR.mkdir(parents=True, exist_ok=True)
def main():
    archivos = obtener_archivos_csv(DATA_DIR)
    if not archivos:
        print("No se encontraron archivos CSV en data/processed")
        return

    todas_las_listas = []
    etiquetas = []
    for csv_path in archivos:
        tiempo, voltaje = leer_datos_csv(csv_path)
        #print(f"Leído: {csv_path.name} — filas válidas: {len(tiempo)}")
        todas_las_listas.append(voltaje)
        etiquetas.append(csv_path.stem)
        out1=PLOTS_DIR/f"plot_{csv_path.stem}.png"
        umbral=6
        maximo, minimo, promedio, desv = analizar_valores(voltaje)
        #salidas por json en formato diccionario
        resultados = {
        "n": len(tiempo),
        "min": minimo,
        "max": maximo,
        "promedio": promedio,
        "desviacion_estandar": desv,
        }

        grafico_lineal_umbral(tiempo,voltaje,umbral,out1,f"plot V_vs_t_{csv_path.stem}".upper())
        print("Guardado:", out1)
        #para histogramas
        out2=PLOTS_DIR/f"Histo_{csv_path.stem}.png"
        histograma_voltaje(voltaje,out2,f"Histograma para {csv_path.stem}".upper(),umbral)
        print("Guardado:", out2)
        out3 = STATICS_DIR / f"boxplot_{csv_path.stem}.json"
        with open(out3, "w", encoding="utf-8") as f:
            json.dump(resultados, f, indent=4, ensure_ascii=False)
        print("Archivo JSON generado correctamente.")

    if todas_las_listas:
        out4 = PLOTS_DIR / "boxplot_general_todos_los_archivos.png"
        boxplot_todos_los_archivos(
            todas_las_listas,
            etiquetas,
            out4,
            "Boxplot general de todos los archivos".upper()
        )
        print("Guardado:", out4)
        
if __name__ == "__main__":
    main()

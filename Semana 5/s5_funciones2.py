import herramientas.s5_funciones as ds
import herramientas.s5_analisis as da
from pathlib import Path #importar la libreria para manejar rutas de archivos
ROOT=Path(__file__).resolve().parent
TXT=ROOT/"Datos"/"mediciones_200.txt"
temperatura=[]
alertaT=[]
with open(TXT, "r", encoding="utf-8") as f:
    for linea in f:
        temperatura.append(ds.volt_a_Temp_ECT(float(linea)))
        alertaT.append(da.clasificacion(float(linea)))
maximo,minimo,promedio = da.analizar_valores(temperatura)
print(maximo,minimo,promedio)
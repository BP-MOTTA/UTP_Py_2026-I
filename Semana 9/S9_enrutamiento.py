from pathlib import Path
#enrutamiento de entrada
ROOT=Path(__file__).resolve().parents[1]
#parents[0] en la carpeta misma, partens[1] retrocede una carpeta
DATA_DIR=ROOT/"Semana 4"/"Datos"/"raw"
filename="T_2_18_05_26.csv"
CSV_PATH=DATA_DIR/filename
#verificador de existencia
if not CSV_PATH.exists():
    raise FileNotFoundError(f"No existe: {CSV_PATH}")

##comandos de extraccion de informacion 
#print(CSV_PATH)
#print(CSV_PATH.suffix)
#print(CSV_PATH.name) #parte final de la ruta
#print(CSV_PATH.stem) #archivo sin extension
#INFO_DIR=CSV_PATH.with_suffix(".png") #cambia la extension
#print(INFO_DIR)
#nombre=CSV_PATH.with_name(f"{CSV_PATH.stem.replace('limpio','procesado')}{CSV_PATH.suffix}")#with_name cambia el nombre por lo que esta en parentesis
#print(nombre)


#separacion por partes
TIPO,NIVEL,DIA,MES,A = CSV_PATH.stem.split("_")
print(TIPO)

CSV_PATH_OUT = CSV_PATH.with_name(f"{TIPO}_{DIA}_{MES}_Procesado{CSV_PATH.suffix}")
TITULO=(f"grafica Voltaje vs t del sensor{TIPO} del nivel{NIVEL}, fecha:{DIA}-{MES}")
print(TITULO)
print(CSV_PATH_OUT)

Umbral_V=5.1

nombre=(f"{TIPO}_{DIA}_{MES}_Procesado_umbral{Umbral_V}{CSV_PATH.suffix}")
print(nombre)
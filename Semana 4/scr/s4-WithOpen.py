from pathlib import Path #importar la libreria para manejar rutas de archivos
ROOT=Path(__file__).resolve().parent.parent
TXT=ROOT/"Datos"/"raw"/"mediciones_200_mixto.txt"
Salida=ROOT/"Datos"/"processed"/"mediciones_200_procesado_mayor5.txt"
Salida2=ROOT/"Datos"/"processed"/"mediciones_200_procesado_menores_igual5.txt"
Salida3=ROOT/"Datos"/"processed"/"mediciones_200.txt"
print(f"Ruta del programa {ROOT}")
print(f"Ruta del archivo de texto: {TXT}")
valores=[]
comentarios=0
with open(TXT, "r", encoding="utf-8") as f:
    for linea in f:
        #eliminar espacios en blancoy saltos de línea
        s=linea.strip()
        #eliminar los comentarios
        if not s or s.startswith("#"):
            comentarios+=1
            continue
        if not s or s.startswith("!"):
            comentarios+=1
            continue
        #convertir , a . para números decimales
        s=s.replace(",", ".")
        try:
            valores.append(float(s))
        except ValueError:
            print(f"Advertencia: No se pudo convertir '{s}' a un número. Línea ignorada.")
print(f"Valores leídos: {len(valores)}")
print(f"Comentarios ignorados: {comentarios}")


with open(Salida3, "w", encoding="utf-8") as f:
    for v in valores:
        f.write(f"{v}\n")

VMayor=[]
VMenor=[]
for v in valores:
    if v > 5:
        VMayor.append(v)
    else:
        VMenor.append(v)
print(f"Valores mayores a 5: {len(VMayor)}")
print(f"Valores menores o iguales a 5: {len(VMenor)}")

with open(Salida, "w", encoding="utf-8") as f:
    for v in VMayor:
        f.write(f"{v}\n")
with open(Salida2, "w", encoding="utf-8") as f: 
    for v in VMenor:
        f.write(f"{v}\n")

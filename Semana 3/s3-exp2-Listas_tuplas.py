import random as rd
#lista - Mutables
COD04524=["Juan",33,"Ingenieria Ambiental",975555675,True,0.35]
#listas = [0,1,2,3,4]
print(f"la edad de {COD04524[0]} es {COD04524[1]} años, estudio {COD04524[2]} y su numero de contacto es {COD04524[3]}")
print(f"hasta la fecha tiene una tasa de descuento de {COD04524[5]}")
#las listas son MUTABLES
COD04524[2]="Mg en Ingenieria Ambiental"
print(f"la edad de {COD04524[0]} es {COD04524[1]} años, estudio {COD04524[2]} y su numero de contacto es {COD04524[3]}")
print(f"hasta la fecha tiene una tasa de descuento de {COD04524[5]}")
#Tuplas - Inmutables
CODDUE=("Maria",45,"Administracion")
print(f"la edad de {CODDUE[0]} es {CODDUE[1]} años, estudio {CODDUE[2]}")

#mover datos dentro de una lista
List_numer = []
for i in range(10):
    List_numer.append(rd.random())
print(List_numer)
#algoritmo burbuja para ordenar una lista de mayor a menor
for i in range(len(List_numer)):
    for j in range(0, len(List_numer)-i-1):
        if List_numer[j] < List_numer[j+1]: #verificar si la ubicacion es mayor al siguiente
            List_numer[j], List_numer[j+1] = List_numer[j+1], List_numer[j] #si es mayor cambiar
print(List_numer)

List_numer2 = []
for i in range(10):
    List_numer2.append(rd.random())
List_numer2.sort(reverse=True)
print(List_numer2)
List_numer2.reverse()
print(List_numer2)

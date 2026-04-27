import csv
from datetime import datetime
from statistics import mean
from pathlib import Path #importo el comando path (busca el lugar del codigo)
ROOT=Path(__file__).resolve().parents[1]#busca el lugar donde esta guardado el codigo
IN_FILE=ROOT/"Datos"/"raw"/"voltajes_250_sucio.csv" #ruta de ingreso
OUT_FILE=ROOT/"Datos"/"processed"/"voltajes_250_limpio.csv" #ruta de salida
with open(IN_FILE, "r", encoding="utf-8") as fin, \
    open(OUT_FILE, "w", encoding="utf-8", newline="") as fout:
        reader=csv.DictReader(fin,delimiter=";") #lee el archivo csv y lo convierte en un diccionario
        writer=csv.DictWriter(fout,fieldnames=["Tiempo","voltaje","control"])
        writer.writeheader() #escribe el encabezado en el archivo de salida
        Total=Keps=0 #total de filas procesadas
        voltajes=[] #los voltajes almancenados.
        bad_ts=bad_value=0 #total de filas con timestamp no valido
        for row in reader:
            Total=1 #acumula una fila ya leida.
            ts_raw = row.get("timestamp", "").strip() #obtiene el valor del campo "Tiempo" y elimina espacios en blanco
            value_raw = row.get("value", "").strip() #obtiene el valor del campo "voltaje" y elimina espacios en blanco
            #limpiar datos
            value_raw = value_raw.replace(",", ".") #reemplaza las comas por puntos para los decimales
            value_low = value_raw.lower() #convierte el valor a minúsculas para facilitar la comparación
            if value_low in ("n/a", "na", "nan", "null", ""): #si el valor es nulo o no disponible, lo marca como inválido
                bad_value += 1
                continue
            try:
                value = float(value_raw) #intenta convertir el valor a un número flotante
            except ValueError:
                bad_value += 1
                continue
        #limpieza de datos de tiempo 
            ts_clean = None
            for fmt in ("%Y-%m-%dT%H:%M:%S", "%d/%m/%Y %H:%M:%S"):
                try:
                    dt = datetime.strptime(ts_raw, fmt)
                    ts_clean = dt.strftime("%Y-%m-%dT%H:%M:%S")
                    break
                except ValueError:
                    pass
                
            if ts_clean is None: #si no se pudo limpiar el timestamp, lo marca como inválido
                bad_ts += 1
                continue
            #verificar si el valor es mayor a 5V
            control="CUIDADO" if value >= 5 else "OK"
            voltajes.append(value) #almacena el voltaje limpio en la lista
            writer.writerow({"Tiempo": ts_clean, "voltaje": f"{value:.4f}", "control":control})
            Keps+=1 #acumula una fila procesada correctamente

#para los KPIs usando la salida del formato de diccionarios de python.
n=len(voltajes)
if n==0:
    print("No hay datos para calcular los KPIs.")
    KPIs={"n":0,"min":None,"max":None,"prom":None,"alertas":0,"alertas_pct":0}
else:
    alertas = sum(v >= 5 for v in voltajes) #conteo rapido de estructura repetitiva
    KPIs={
        'n': n,
        'min': min(voltajes),
        "max": max(voltajes),
        "prom":mean(voltajes),
        "alerts": alertas,
        "alerts_pct": 100.0 * alertas / n,
    }
#KPIs de calidad.
descartes_totales = bad_ts + bad_value            # equivale a (total - kept) con esta lógica
pct_descartadas = (descartes_totales / Total * 100.0) if Total else 0.0 #condiciones simples
if pct_descartadas > 30.0:
    print("Advertencia: el sensor tiene un mal funcionamiento.")

kpis_calidad = {
    "filas_totales": Total,
    "filas_validas": Keps,
    "descartes_timestamp": bad_ts,
    "descartes_valor": bad_value,
    "%descartadas": round(pct_descartadas, 2), # redondea a 2 decimales
}

# --- Salida/Verificación ---
print(f"Entrada:  {IN_FILE}")
print(f"Salida:   {OUT_FILE}")
print("\nKPIs de calidad:", kpis_calidad)
print("KPIs de voltaje:", {
    "n": KPIs["n"],
    "min": None if KPIs["min"] is None else round(KPIs["min"], 2),
    "max": None if KPIs["max"] is None else round(KPIs["max"], 2),
    "prom": None if KPIs["prom"] is None else round(KPIs["prom"], 2),
    "alerts": KPIs["alerts"],
    "alerts_pct": round(KPIs["alerts_pct"], 2),
})
import csv
from pathlib import Path
from datetime import datetime

def detectar_delimitador(path: Path) -> str:
    with path.open("r", encoding="utf-8", newline="") as f:
        head = f.readline()
    return ";" if head.count(";") > head.count(",") else ","

def parse_ts(s: str):
    s = (s or "").strip()
    for fmt in ("%Y-%m-%dT%H:%M:%S", "%d/%m/%Y %H:%M:%S"):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            pass
    return None

def obtener_archivos_csv(data_dir: Path):
    return list(data_dir.glob("*.csv"))

def leer_datos_csv(csv_path: Path):
    tiempo,voltaje = [],[]
    delim = detectar_delimitador(csv_path)
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter=delim)
        for row in reader:
            t = parse_ts(row.get("tiempo") or row.get("Timestamp"))
            if t is None:
                continue

            v_raw = row.get("voltaje") or row.get("Voltaje") or row.get("value")
            try:
                v = float(str(v_raw).replace(",", "."))
            except (TypeError, ValueError):
                continue

            tiempo.append(t)
            voltaje.append(v)

    return tiempo, voltaje


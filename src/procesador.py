import csv

class Analizador:
    def __init__(self, ruta_csv):
        self.ruta_csv = ruta_csv
        try:
            self.datos = self.leer_csv()
        except FileNotFoundError:
            self.datos = []
        except Exception:
            self.datos = []

    def leer_csv(self):
        datos = []
        with open(self.ruta_csv, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo, delimiter="|")
            for fila in lector:
                datos.append(fila)
        return datos

    def ventas_totales_por_provincia(self):
        if not self.datos:
            return {}

        totales = {}
        for fila in self.datos:
            try:
                provincia = fila["PROVINCIA"]
                total_venta = float(fila["TOTAL_VENTAS"])
            except (KeyError, ValueError):
                continue

            if provincia not in totales:
                totales[provincia] = total_venta
            else:
                totales[provincia] += total_venta

        return totales

    def ventas_por_provincia(self, nombre):
        totales = self.ventas_totales_por_provincia()
        return totales.get(nombre, 0.0)
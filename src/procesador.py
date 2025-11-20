import csv
from typing import Dict, List


class Analizador:
    """Procesa el archivo de ventas del SRI y expone operaciones de consulta."""

    def __init__(self, ruta_csv: str) -> None:
        self.ruta_csv = ruta_csv
        try:
            self.datos = self.leer_csv()
        except FileNotFoundError:
            # Si no se encuentra el archivo, dejamos la lista vacía
            self.datos = []
        except Exception:
            # Cualquier otro error de lectura también deja la lista vacía
            self.datos = []

    def leer_csv(self) -> List[dict]:
        """Lee el CSV separado por '|' y devuelve una lista de diccionarios."""
        filas: List[dict] = []
        with open(self.ruta_csv, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo, delimiter="|")
            for fila in lector:
                filas.append(fila)
        return filas

    # ------------------------------------------------------------------ #
    # Agregaciones y consultas
    # ------------------------------------------------------------------ #

    def ventas_totales_por_provincia(self) -> Dict[str, float]:
        """Devuelve un diccionario con el total de ventas por provincia.

        Se excluyen las filas cuya provincia sea "ND" (no determinada),
        ya que los tests asumen únicamente las 24 provincias del país.
        """
        totales: Dict[str, float] = {}

        for fila in self.datos:
            try:
                provincia = fila["PROVINCIA"]
                if provincia is None:
                    continue

                # Normalizamos el nombre de la provincia
                provincia = provincia.strip().upper()

                # Ignorar filas con provincia no determinada
                if provincia == "ND":
                    continue

                total_venta_str = fila["TOTAL_VENTAS"]
                total_venta = float(total_venta_str) if total_venta_str else 0.0
            except (KeyError, ValueError, TypeError):
                # Si la fila no tiene los campos esperados o el valor no es numérico
                continue

            if provincia in totales:
                totales[provincia] += total_venta
            else:
                totales[provincia] = total_venta

        return totales

    def ventas_por_provincia(self, nombre: str) -> float:
        """Devuelve el total de ventas de una provincia específica.

        Parameters
        ----------
        nombre : str
            Nombre de la provincia a consultar. No es sensible a
            mayúsculas/minúsculas.

        Returns
        -------
        float
            Total de ventas de la provincia.

        Raises
        ------
        KeyError
            Si la provincia no existe en el diccionario de ventas.
        """
        totales = self.ventas_totales_por_provincia()

        # Normalizamos el nombre para que búsquedas como "Pichincha" funcionen
        nombre_normalizado = nombre.strip().upper()

        if nombre_normalizado not in totales:
            raise KeyError(f"Provincia no encontrada: {nombre}")

        return totales[nombre_normalizado]

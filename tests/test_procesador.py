import unittest
from src.procesador import Analizador


def es_mayor_a_cinco_mil(valor_venta):
    """Convierte el valor a float y verifica si es mayor a 5000."""
    return float(valor_venta) > 5000


class TestAnalizador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # El archivo se asume relativo al directorio raíz del proyecto
        cls.analizador = Analizador("datos/sri_ventas_2024.csv")

    def test_ventas_totales_como_diccionario(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertIsInstance(resumen, dict)

    def test_ventas_totales_todas_las_provincias(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        total_provincias = len(resumen)
        # Asumiendo 24 provincias en el dataset
        self.assertEqual(total_provincias, 24)

    def test_ventas_totales_mayores_5k(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertTrue(all(es_mayor_a_cinco_mil(v) for v in resumen.values()))

    def test_ventas_por_provincia_inexistente(self):
        with self.assertRaises(KeyError):
            self.analizador.ventas_por_provincia("Narnia")

    def test_ventas_por_provincia_existente(self):
        # Pichincha debería existir y tener un total mayor a 0
        resultado = self.analizador.ventas_por_provincia("Pichincha")
        self.assertGreater(resultado, 0)


if __name__ == "__main__":
    unittest.main()

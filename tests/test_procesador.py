import unittest
import os
from src.procesador import Analizador

MOCK_CSV_PATH = "test_data_mock.csv"

MOCK_CSV_CONTENT = [
    "PROVINCIA|TOTAL_VENTAS",
    "Guayas|100.50",
    "Guayas|50.00",
    "Pichincha|200.00",
    "Azuay|75.25",
    "Azuay|25.00",
    "Loja|10.00",
    "Imbabura|5.00"
]

class TestAnalizador(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        with open(MOCK_CSV_PATH, "w", encoding="utf-8") as f:
            f.write("\n".join(MOCK_CSV_CONTENT))
        
        cls.analizador = Analizador(MOCK_CSV_PATH)
        cls.resumen_total = cls.analizador.ventas_totales_por_provincia()

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(MOCK_CSV_PATH):
            os.remove(MOCK_CSV_PATH)

    def test_1_numero_provincias_coherente(self):
        self.assertEqual(len(self.resumen_total), 5)

    def test_2_valores_totales_son_numericos_y_positivos(self):
        for total in self.resumen_total.values():
            self.assertIsInstance(total, (int, float))
            self.assertGreaterEqual(total, 0)
    
    def test_3_retorna_diccionario(self):
        self.assertIsInstance(self.resumen_total, dict)

    def test_4_provincias_inexistentes(self):
        ventas_cero = self.analizador.ventas_por_provincia("Galapagos")
        self.assertEqual(ventas_cero, 0.0)

    def test_5_valores_consultados_correctos(self):
        ventas_guayas = self.analizador.ventas_por_provincia("Guayas")
        self.assertAlmostEqual(ventas_guayas, 150.50, places=2)
        
        ventas_pichincha = self.analizador.ventas_por_provincia("Pichincha")
        self.assertAlmostEqual(ventas_pichincha, 200.00, places=2)
        
        ventas_azuay = self.analizador.ventas_por_provincia("Azuay")
        self.assertAlmostEqual(ventas_azuay, 100.25, places=2)

if __name__ == '__main__':
    unittest.main()
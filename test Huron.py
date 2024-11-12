import unittest
from boa_constrictor import BoaConstrictor
from ferret import Ferret



class TestFerret(unittest.TestCase):
    def setUp(self):
        # Configuración para los objetos de prueba de Hurón
        self.ferret = Ferret("Ferret1", 5.0, 3, "Argentina", 5.0)

    def test_hacer_sonido(self):
        # Verifica que el sonido del hurón es correcto
        self.assertEqual(self.ferret.do_sound(), "¡Eek Eek!")

    def test_calcular_flete(self):
        # Verifica que el cálculo de flete es correcto
        expected_freight = self.ferret.weight * self.ferret.taxes
        self.assertEqual(self.ferret.calculate_freight(), expected_freight)


if __name__ == "__main__":
    unittest.main()

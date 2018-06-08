import unittest
from code import impedido
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_caso_1(self):
        self.assertRaises( ValueError, impedido, "caso1.txt")

    def test_caso_2(self):
        self.assertEqual(impedido("caso2.txt"), "")

    def test_caso_3(self):
        self.assertRaises( ValueError, impedido, "caso3.txt")

    def test_caso_4(self):
        self.assertRaises( ValueError, impedido, "caso4.txt")

    # O caso 5 é igual ao caso 6 porque não é possível deixar de entrar no loop.
    # Devido à validação dos argumentos.
    def test_caso_5(self):
        self.assertEqual( impedido("caso5.txt"), "N\n")

    def test_caso_6(self):
        self.assertEqual( impedido("caso6.txt"), "Y\n")

    def test_caso_8(self):
        self.assertEqual( impedido("caso8.txt"), "N\nY\nN\n")

if __name__ == '__main__':
    unittest.main()
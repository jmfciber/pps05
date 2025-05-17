import unittest
from charfun import esPalindromo

class TestPalindromoPractica1(unittest.TestCase):
    def test_frase_palindromo(self):
        self.assertTrue(esPalindromo("Anita lava la tina"))

    def test_frase_no_palindromo(self):
        self.assertFalse(esPalindromo("Esto no es un palíndromo"))

    def test_cadena_vacia(self):
        self.assertTrue(esPalindromo(""))

    def test_solo_espacios(self):
        self.assertTrue(esPalindromo("   "))

    def test_caracteres_especiales_palindromo(self):
        self.assertTrue(esPalindromo("¿Acaso hubo búhos acá?"))
        self.assertTrue(esPalindromo("¡Salas!"))
        self.assertTrue(esPalindromo("123$#@321"))

    def test_caracteres_especiales_no_palindromo(self):
        self.assertFalse(esPalindromo("Esto no es@un*palíndromo..."))
        self.assertFalse(esPalindromo("¿Qué tal esto?"))

    def test_caracteres_especiales(self):
        self.assertTrue(esPalindromo("A man, a plan, a canal: Panama"))

    def test_mayusculas_minusculas(self):
        self.assertTrue(esPalindromo("AnItA LaVa La TiNa"))

    def test_numeros_palindromo(self):
        self.assertTrue(esPalindromo("12321"))

    def test_numeros_no_palindromo(self):
        self.assertFalse(esPalindromo("12345"))

    def test_palabras_repetidas_palindromo(self):
        self.assertTrue(esPalindromo("oso oso oso"))

    def test_palabras_repetidas_no_palindromo(self):
        self.assertFalse(esPalindromo("oso oso oso no"))

    def test_cadena_larga_palindromo(self):
        self.assertTrue(esPalindromo("a" * 1000 + "b" + "a" * 1000))

    def test_cadena_larga_no_palindromo(self):
        self.assertFalse(esPalindromo("a" * 1000 + "b" + "a" * 999 + "c"))

    def test_palindromo_con_acentos(self):
        self.assertTrue(esPalindromo("Árbol saca claros, sol acá sobrará"))

    def test_no_palindromo_con_acentos(self):
        self.assertFalse(esPalindromo("Este no es un texto palíndromo, aunque tenga acentos."))

    def test_palindromo_en_ruso(self):
        self.assertTrue(esPalindromo("А роза упала на лапу Азора"))

if __name__ == "__main__":
    unittest.main()


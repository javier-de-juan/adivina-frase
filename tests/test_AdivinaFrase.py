import sys, os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src.Main import jugar
from src.Exceptions.ExcepcionDeEntrada import ExcepcionDeEntrada
from src.Functions import obtener_numero_de_usuario, obtener_string_de_usuario
from src.JuegoFrase import JuegoFrase
from src.JuegoNumero import JuegoNumero
from src.JuegoPalabra import JuegoPalabra
from unittest.mock import patch
from unittest import TestCase


## coverage run -m pytest tests && coverage html src/Main.py

class AdivinaFrase(TestCase):

    @patch('src.Functions.get_input', return_value="3")
    def test_obtener_numero_de_usuario_ok(self, getInputMock):
        self.assertEqual(obtener_numero_de_usuario("Introduce un número"), 3)

    @patch('src.Functions.get_input', return_value="test")
    def test_obtener_string_de_usuario_ok(self, getInputMock):
        self.assertEqual(obtener_string_de_usuario("Introduce una palabra"), "test")

    @patch('src.Functions.get_secret', return_value="test")
    def test_obtener_string_secreto_de_usuario_ok(self, getInputMock):
        self.assertEqual(obtener_string_de_usuario("Introduce una palabra", True), "test")

    @patch('src.JuegoNumero.obtener_numero_de_usuario', return_value=4)
    def test_adivina_numero(self, getInputMock):
        juego_numero = JuegoNumero(4, 4)
        self.assertTrue(juego_numero.adivinar_numero())

    @patch('src.JuegoNumero.obtener_numero_de_usuario', return_value=3)
    def test_no_adivina_numero(self, getInputMock):
        juego_numero = JuegoNumero(4, 2)
        self.assertFalse(juego_numero.adivinar_numero())

    @patch('src.JuegoPalabra.obtener_string_de_usuario', return_value="e")
    def test_adivina_letra(self, getInputMock):
        juego_palabra = JuegoPalabra(4, 4)
        self.assertTrue(juego_palabra.adivinar_letra("el test"))

    @patch('src.JuegoPalabra.obtener_string_de_usuario', return_value="a")
    def test_no_adivina_letra(self, getInputMock):
        juego_palabra = JuegoPalabra(4, 2)
        self.assertFalse(juego_palabra.adivinar_letra("El test"))

    @patch('src.JuegoPalabra.obtener_string_de_usuario', return_value="test")
    def test_adivina_palabra(self, getInputMock):
        juego_palabra = JuegoPalabra(4, 4)
        self.assertTrue(juego_palabra.adivinar_palabra("el test"))

    @patch('src.JuegoPalabra.obtener_string_de_usuario', return_value="la")
    def test_no_adivina_palabra(self, getInputMock):
        juego_palabra = JuegoPalabra(4, 2)
        self.assertFalse(juego_palabra.adivinar_palabra("El test"))

    @patch('src.JuegoPalabra.obtener_string_de_usuario', side_effect=['r', 'frase'])
    def test_mostrar_frase(self, getInputMock):
        frase_a_adivinar = "mostrar frase"
        juego_frase = JuegoFrase(frase_a_adivinar, 2)
        juego_frase.adivinar_letra(frase_a_adivinar)
        juego_frase.adivinar_palabra(frase_a_adivinar)
        self.assertEqual('****r*r frase', juego_frase.mostrar_frase().strip())

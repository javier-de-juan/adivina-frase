import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src.JuegoPalabra import JuegoPalabra
from unittest.mock import patch
from unittest import TestCase


class AdivinaFrase(TestCase):

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

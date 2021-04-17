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


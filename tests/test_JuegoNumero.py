import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src.JuegoNumero import JuegoNumero
from unittest.mock import patch
from unittest import TestCase


class AdivinaFrase(TestCase):

    @patch('src.JuegoNumero.obtener_numero_de_usuario', return_value=4)
    def test_adivina_numero(self, getInputMock):
        juego_numero = JuegoNumero(4, 4)
        self.assertTrue(juego_numero.adivinar_numero())

    @patch('src.JuegoNumero.obtener_numero_de_usuario', return_value=3)
    def test_no_adivina_numero(self, getInputMock):
        juego_numero = JuegoNumero(4, 2)
        self.assertFalse(juego_numero.adivinar_numero())

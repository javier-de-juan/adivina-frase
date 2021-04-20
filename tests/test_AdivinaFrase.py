import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src.Main import jugar
from unittest.mock import patch
from unittest import TestCase


class AdivinaFrase(TestCase):

    @patch('src.Main.obtener_numero_de_usuario', return_value=1)
    @patch('src.JuegoNumero.obtener_numero_de_usuario', return_value=4)
    @patch('src.Main.obtener_string_de_usuario', return_value="probando modulo")
    def test_adivina_jugar(self, mock1, mock2, mock3):
        self.assertFalse(jugar())
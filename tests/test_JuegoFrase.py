import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src.JuegoFrase import JuegoFrase
from unittest.mock import patch
from unittest import TestCase


class AdivinaFrase(TestCase):

    @patch('src.JuegoPalabra.obtener_string_de_usuario', side_effect=['r', 'frase'])
    def test_mostrar_frase(self, getInputMock):
        frase_a_adivinar = "mostrar frase"
        juego_frase = JuegoFrase(frase_a_adivinar, 2)
        juego_frase.adivinar_letra(frase_a_adivinar)
        juego_frase.adivinar_palabra(frase_a_adivinar)
        self.assertEqual('****r*r frase', juego_frase.mostrar_frase().strip())

    @patch('src.JuegoFrase.obtener_string_de_usuario', return_value='adivino la frase')
    @patch('src.JuegoNumero.obtener_numero_de_usuario', return_value=4)
    @patch('src.JuegoFrase.obtener_numero_de_usuario', side_effect=[3, 2])
    def test_no_adivina_frase(self, mock_frase_intentada, mock_longitud, mock_opcion_deseada):
        frase_a_adivinar = "no adivino la frase"
        juego_frase = JuegoFrase(frase_a_adivinar, 1)
        self.assertFalse(juego_frase.adivinar_frase())

    @patch('src.JuegoNumero.obtener_numero_de_usuario', side_effect=[2, 9])
    def test_no_adivino_longitud(self, mock_obtener_numero_usuario):
        frase_a_adivinar = "adivino la frase"
        juego_frase = JuegoFrase(frase_a_adivinar, 2)
        self.assertFalse(juego_frase.adivinar_frase())

    @patch('src.JuegoPalabra.obtener_string_de_usuario', side_effect=['q', 'test'])
    @patch('src.JuegoFrase.obtener_string_de_usuario', return_value='adivino la frase')
    @patch('src.JuegoNumero.obtener_numero_de_usuario', return_value=4)
    @patch('src.JuegoFrase.obtener_numero_de_usuario', side_effect=[0, 1, 2])
    def test_no_adivina_nada(self, mock_strings_jp, mock_strings_jf, mock_numeros_jn, mock_numero_jf):
        frase_a_adivinar = "no adivino la frase"
        juego_frase = JuegoFrase(frase_a_adivinar, 2)
        self.assertFalse(juego_frase.adivinar_frase())

    @patch('src.JuegoPalabra.obtener_string_de_usuario', side_effect=['l', 'frase'])
    @patch('src.JuegoFrase.obtener_string_de_usuario', side_effect=['casi adivino la frase', 'adivino la frase'])
    @patch('src.JuegoNumero.obtener_numero_de_usuario', return_value=3)
    @patch('src.JuegoFrase.obtener_numero_de_usuario', side_effect=[0, 1, 2, 2])
    def test_adivino_todo(self, mock_strings_jp, mock_strings_jf, mock_numeros_jn, mock_numero_jf):
        frase_a_adivinar = "adivino la frase"
        juego_frase = JuegoFrase(frase_a_adivinar, 2)
        self.assertTrue(juego_frase.adivinar_frase())

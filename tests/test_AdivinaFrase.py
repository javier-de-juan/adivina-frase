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

    @patch('src.JuegoFrase.obtener_string_de_usuario', return_value='adivino la frase')
    @patch('src.JuegoNumero.obtener_numero_de_usuario', return_value=4)
    @patch('src.JuegoFrase.obtener_numero_de_usuario', return_value=2)
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

    def test_excepcion_no_es_un_numero(self):
        with self.assertRaises(ExcepcionDeEntrada):
            raise ExcepcionDeEntrada.no_es_un_numero("a")

    def test_excepcion_no_es_un_string(self):
        with self.assertRaises(ExcepcionDeEntrada):
            raise ExcepcionDeEntrada.no_es_un_string(5)

    def test_excepcion_longitud_invalida(self):
        with self.assertRaises(ExcepcionDeEntrada):
            raise ExcepcionDeEntrada.longitud_invalida("perro", "2")

    def test_excepcion_opcion_invalida(self):
        with self.assertRaises(ExcepcionDeEntrada):
            raise ExcepcionDeEntrada.opcion_invalida()

    @patch('src.AdivinaFrase.obtener_numero_de_usuario', return_value=1)
    @patch('src.JuegoNumero.obtener_numero_de_usuario', return_value=4)
    @patch('src.AdivinaFrase.obtener_string_de_usuario', return_value="probando modulo")
    def test_adivina_jugar(self, mock1, mock2, mock3):
        self.assertFalse(jugar())
import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src.Exceptions.ExcepcionDeEntrada import ExcepcionDeEntrada
from unittest import TestCase


class AdivinaFrase(TestCase):

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

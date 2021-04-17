import getpass
import logging
from src.Exceptions.ExcepcionDeEntrada import ExcepcionDeEntrada

# settings para hacer bonito el logging
logging.basicConfig(format='%(message)s', level=logging.INFO)
logging.basicConfig(format='%(message)s', level=logging.ERROR)
logging.basicConfig(format='%(message)s', level=logging.WARNING)


def get_input(pregunta):
    return input(pregunta)


def get_secret(pregunta):
    return getpass.getpass(pregunta)


def obtener_numero_de_usuario(pregunta):
    while True:
        try:
            numero = get_input(pregunta)

            if not numero.isnumeric():
                raise ExcepcionDeEntrada.no_es_un_numero(numero)

            return int(numero)
        except ExcepcionDeEntrada as excepcion:
            logging.error(excepcion)
            continue


def obtener_string_de_usuario(pregunta, secreto=False, longitud=False):
    while True:
        try:
            if secreto:
                string_de_usuario = get_secret(pregunta)
            else:
                string_de_usuario = get_input(pregunta)

            if longitud and longitud != len(string_de_usuario):
                raise ExcepcionDeEntrada.longitud_invalida(string_de_usuario, longitud)

            if string_de_usuario.isnumeric():
                raise ExcepcionDeEntrada.no_es_un_string(string_de_usuario)

            return string_de_usuario
        except ExcepcionDeEntrada as excepcion:
            logging.error(excepcion)
            continue

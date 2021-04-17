import sys
import os
import logging

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

if True:
    from src.Functions import obtener_string_de_usuario, obtener_numero_de_usuario
    from src.JuegoFrase import JuegoFrase

# settings para hacer bonito el logging
logging.basicConfig(format='%(message)s', level=logging.INFO)
logging.basicConfig(format='%(message)s', level=logging.ERROR)
logging.basicConfig(format='%(message)s', level=logging.WARNING)


def jugar():
    try:
        frase_a_adivinar = obtener_string_de_usuario("Introduzca la frase:", True)
        intentos = obtener_numero_de_usuario('Introduzca intentos permitidos:')
        juego = JuegoFrase(frase_a_adivinar, intentos)

        return juego.adivinar_frase()
    except KeyboardInterrupt:
        logging.info("""Juego interrumpido""")


if __name__ == '__main__':
    jugar()

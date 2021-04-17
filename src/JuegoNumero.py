import logging
from src.Juego import Juego
from src.Functions import obtener_numero_de_usuario
from src.Exceptions.ExcepcionDeJuego import ExcepcionDeJuego


class JuegoNumero(Juego):
    MENSAJE_ERROR_MENOR = 'Intento erróneo. La palabra a adivinar tiene menos letras.'
    MENSAJE_ERROR_MAYOR = 'Intento erróneo. La palabra a adivinar tiene más letras.'
    MENSAJE_EXITO = """Has acertado el número de letras!"""
    num_adivinar = None
    numeros_intentados = []

    def __init__(self, num_adivinar, num_intentos):
        super().__init__(num_intentos)
        self.num_adivinar = num_adivinar

    def adivinar_numero(self):
        try:
            while True:
                numero_intentado = obtener_numero_de_usuario('Adivina el número de palabras:')
                self.numeros_intentados.append(numero_intentado)

                if self.num_adivinar == numero_intentado:
                    logging.info(f"""Has acertado el número, son {self.num_adivinar} palabras!""")
                    return True

                self.intentos_restantes -= 1

                if self.num_adivinar < numero_intentado:
                    logging.warning(f"""Lo siento, la frase tiene menos palabras.
Te quedan {self.intentos_restantes} intentos disponibles""")
                elif self.num_adivinar > numero_intentado:
                    logging.warning(f"""Lo siento, la frase tiene más palabras.
Te quedan {self.intentos_restantes} intentos disponibles""")

                if 0 == self.intentos_restantes:
                    raise ExcepcionDeJuego.intentos_agotados_adivinando_numero_palabras(
                        self.num_intentos,
                        self.num_adivinar
                    )

        except ExcepcionDeJuego as excepcion:
            logging.warning(excepcion)

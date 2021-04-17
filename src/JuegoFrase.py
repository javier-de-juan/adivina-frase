import logging
from src.JuegoPalabra import JuegoPalabra
from src.Functions import obtener_numero_de_usuario, obtener_string_de_usuario
from src.Exceptions.ExcepcionDeEntrada import ExcepcionDeEntrada
from src.Exceptions.ExcepcionDeJuego import ExcepcionDeJuego

# settings para hacer bonito el logging
logging.basicConfig(format='%(message)s', level=logging.INFO)
logging.basicConfig(format='%(message)s', level=logging.ERROR)
logging.basicConfig(format='%(message)s', level=logging.WARNING)


class JuegoFrase(JuegoPalabra):
    frase_adivinar = None
    frases_intentadas = []
    ADIVINAR_LETRA = 0
    ADIVINAR_PALABRA = 1
    ADIVINAR_FRASE = 2

    def __init__(self, frase_adivinar, num_intentos):
        super().__init__(len(frase_adivinar.split()), num_intentos)
        self.frase_adivinar = frase_adivinar

    def __pedir_opcion_deseada(self):
        while True:
            try:
                opcion_deseada = obtener_numero_de_usuario("""0. Adivina letra
1. Adivina palabra
2. Adivina frase
Selecciona:""")
                if opcion_deseada not in [self.ADIVINAR_LETRA, self.ADIVINAR_PALABRA, self.ADIVINAR_FRASE]:
                    raise ExcepcionDeEntrada.opcion_invalida()

                return opcion_deseada

            except ExcepcionDeEntrada as excepcion:
                logging.error(excepcion)

    def adivinar_frase(self):
        if not super().adivinar_numero():
            return False

        try:
            while True:
                opcion_deseada = self.__pedir_opcion_deseada()

                if opcion_deseada == self.ADIVINAR_LETRA:
                    if self.adivinar_letra(self.frase_adivinar):
                        logging.info(
                            f"Intento correcto. "
                            f"Existe la letra. {self.mostrar_frase()}. {self.intentos_restantes} "
                            f"intentos disponibles."
                        )
                        continue

                    self.intentos_restantes -= 1

                    logging.warning(
                        f'Intento erróneo. '
                        f'No existe la letra. {self.mostrar_frase()}. '
                        f'{self.intentos_restantes} intentos disponibles')
                elif opcion_deseada == self.ADIVINAR_PALABRA:
                    if self.adivinar_palabra(self.frase_adivinar):
                        logging.info(
                            f'Intento correcto. '
                            f'Existe la palabra. {self.mostrar_frase()}. '
                            f'{self.intentos_restantes} intentos disponibles'
                        )
                        continue

                    self.intentos_restantes -= 1

                    logging.warning(
                        f'Intento erróneo. '
                        f'No existe la palabra. {self.mostrar_frase()}. '
                        f'{self.intentos_restantes} intentos disponibles')

                elif opcion_deseada == self.ADIVINAR_FRASE:
                    frase_intentada = obtener_string_de_usuario('Adivina la frase:', False)
                    self.frases_intentadas.append(frase_intentada)

                    if frase_intentada == self.frase_adivinar:
                        logging.info(f"""Has acertado la frase!
Los intentos de numero de palabras fueron los siguientes: {self.numeros_intentados}.
Los intentos de letras fueron los siguientes: {self.letras_intentadas}.
Los intentos de palabras fueron los siguientes: {self.palabras_intentadas}.
Los intentos de frases fueron los siguientes: {self.frases_intentadas}.""")
                        return True

                    self.intentos_restantes -= 1

                    print(
                        f'Intento erróneo. '
                        f'No es la frase correcta. {self.mostrar_frase()}. '
                        f'{self.intentos_restantes} intentos disponibles'
                    )

                if 0 == self.intentos_restantes:
                    raise ExcepcionDeJuego.intentos_agotados_adivinando_frase(
                        self.num_intentos, self.frase_adivinar,
                        self.numeros_intentados,
                        self.letras_intentadas,
                        self.palabras_intentadas,
                        self.frases_intentadas
                    )

        except ExcepcionDeJuego as excepcion:
            logging.warning(excepcion)
            return False

    def mostrar_frase(self):
        frase = ""

        for palabra in self.frase_adivinar.split():
            if palabra in self.palabras_intentadas:
                frase = frase + palabra
            else:
                for letra in palabra:
                    if letra in self.letras_intentadas:
                        frase = frase + letra
                    else:
                        frase = frase + "*"
            frase = frase + " "

        return frase

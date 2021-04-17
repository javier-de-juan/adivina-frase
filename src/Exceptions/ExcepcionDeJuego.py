class ExcepcionDeJuego(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

    @staticmethod
    def intentos_agotados_adivinando_numero_palabras(intentos, numero_a_adivinar):
        return ExcepcionDeJuego(f"""Has gastado tus {intentos} intentos y no has acertado el número de palabras.
El número de palabras eran {numero_a_adivinar}""")

    @staticmethod
    def intentos_agotados_adivinando_frase(num_intentos, frase_adivinar, numeros_intentados, letras_intentadas,
                                           palabras_intentadas, frases_intentadas):
        return ExcepcionDeJuego(f"""Has gastado tus {num_intentos} intentos y no has acertado la frase.
La frase a adivinar era '{frase_adivinar}'
Los intentos numero de palabras fueron los siguientes: {numeros_intentados}.
Los intentos de letras fueron los siguientes: {letras_intentadas}.
Los intentos de palabras fueron los siguientes: {palabras_intentadas}.
Los intentos de frases fueron los siguientes: {frases_intentadas}.
""")

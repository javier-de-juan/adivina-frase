from src.JuegoNumero import JuegoNumero
from src.Functions import obtener_string_de_usuario


class JuegoPalabra(JuegoNumero):
    letras_intentadas = []
    palabras_intentadas = []

    def __init__(self, numero_de_palabras, num_intentos):
        super().__init__(numero_de_palabras, num_intentos)

    def adivinar_letra(self, frase_adivinar):
        letra_intentada = obtener_string_de_usuario('Adivina una letra:', False, 1)
        self.letras_intentadas.append(letra_intentada)

        return True if letra_intentada in frase_adivinar else False

    def adivinar_palabra(self, frase_adivinar):
        palabra_intentada = obtener_string_de_usuario('Adivina la palabra:', False)
        self.palabras_intentadas.append(palabra_intentada)

        return True if palabra_intentada in frase_adivinar else False

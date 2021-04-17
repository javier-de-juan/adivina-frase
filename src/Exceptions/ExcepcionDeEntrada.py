class ExcepcionDeEntrada(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

    @staticmethod
    def no_es_un_numero(entrada):
        return ExcepcionDeEntrada(f'"{entrada}" no es un número.')

    @staticmethod
    def no_es_un_string(entrada):
        return ExcepcionDeEntrada(f'"{entrada}" no es un string válido.')

    @staticmethod
    def longitud_invalida(entrada, longitud):
        return ExcepcionDeEntrada(f'"{entrada}" no cumple con la longitud esperada de {longitud}.')

    @staticmethod
    def opcion_invalida():
        return ExcepcionDeEntrada("No has introducido una de las opciones indicadas")

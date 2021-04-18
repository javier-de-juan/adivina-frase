# Adivina frase

Juego interactivo que te permite pasar un buen rato con tus conocidos haciendo que intenten adivinar una frase que has escrito tú.

## Cómo hacer funcionar Adivina frase

### Prerequisitos

1. Debes tener instalado **Python 3**.

   Puedes checkear tu versión haciendo `python3 --version`.

2. Debes tener también **pip** instalado.

   Puedes checkear tu versión haciendo `pip3 --version`.

3. Instala **virtualenv** (si no lo tienes):

   ```sh
   pip3 install virtualenv
   ```

4. Crea un **entorno virtual** para el proyecto (la recomendación es hacerlo en la raíz de este proyecto):

   ```sh
   virtualenv venv
   ```

5. Activa el entorno virtual:

   ```sh
   source venv/bin/activate
   ```

6. Instala las dependencias:

   ```sh
   pip3 install -r requirements.txt
   ```

## Jugar a Adivina frase

Para jugar, ejecuta:

```sh
python3 src/Main.py
```

Serás preguntado por la frase que tiene que adivinar el jugador y el número de intentos de los que dispone.

La dinámica del juego es la siguiente:

1. El jugador debe adivinar el número de palabras que tiene la frase
    * Si el número introducido es menor al número de palabras, se le avisará y se le descontará un intento del número total.
    * Si el número introducido es mayor al número de palabras, se le avisará y se le descontará un intento del número total.
    * Si acierta el número de palabras, podrá continuar el juego.
2. El jugador podrá elegir qué hacer:
    * Adivinar una letra de la frase
    * Adivinar una palabra de la frase
    * Adivinar la frase
    > En el caso de que se adivine una letra o una palabra, se desbloquearán los caracteres adivinados mostrando la frase.
 Lo que aún no esté adivinado, será representado mediante asteriscos.
 En el caso de que el intento sea fallido, se descontará un intento del número total.
 Ya sea en el caso de agotar los intentos, o en el de adivinar la fase, el juego habrá acabado dando un pequeño informe 
 de los intentos realizados por tipo (número de palabras, letras, palabras y frases intentadas).

## Probando Adivina frase

### Calidad

Para ver la calidad del código, ejecuta

```sh
flake8 ./src
```

O, si quieres ver su complejidad ciclomática:

```sh
flake8 --max-complexity 8 --statistics ./src
```

### Tests

Para ejecutar los tests, desde la terminal en el path del proyecto ejecuta:

```sh
pytest tests 
```

Esto ejecutará los tests que probarán que el juego funciona correctamente.

### Cobertura

Actualmente, el porcentaje de código cubierto por tests se sitúa en el *91%*

Para poder ver la cobertura, ejecuta:

```sh
coverage run -m pytest tests && coverage html  --include "src/*" 
```

Si se accede a la carpeta `htmlcov` y se abre el archivo `index.html`, se podrá ver la cobertura existente por archivo
como se puede observar aquí:

![Imagen de cobertura de tests][cobertura]

[cobertura]: ./coverage.png "Cobertura de tests para Adivina Frase"

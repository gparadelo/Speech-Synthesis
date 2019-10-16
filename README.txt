PH: TP1
Grosso - Paradelo

Este trabajo practico consiste en un sintetizador de palabras basado en difonos para en el lenguaje L. Programado en Python y utilizando la herramienta Praat.


Para usarlo ejecutar el siguiente comando:

	python tts.py <palabra_a_sintetizar> <direccion_destino>

Por ejemplo:

	python tts.py EsemeketrEfe? /tmp/output.wav


Para producir prosodia de pregunta en caso de que la palabra de entrada termine en '?', se modifica la frecuencia alrededor de la sílaba acentuada para que sea mas agudo.


Se utilizo Praat 6.1.04


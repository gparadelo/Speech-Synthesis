1) Extracción del pitch track.

Dado un archivo de audio, primero extraemos su pitch track con este comando:
  praat extraer-pitch-track.praat IN OUT MINPITCH MAXPITCH
donde:
  IN es un archivo wav.
  OUT es el nombre del archivo a crear.
  MINPITCH y MAXPITCH son el rango tonal del hablante en Hz. Como guía, 
    puede usarse 50-300 para hombres y 75-500 para mujeres, aunque los
    resultados mejoran si se usa una mejor estimación para el hablante.
   
Ejemplo:
  praat extraer-pitch-track.praat 12345.wav 12345.PitchTier 50 300
Esto genera el archivo 12345.PitchTier.

-----  

2) Modificación del pitch track.

Este paso debe realizarse por fuera de Praat (ej: en Python).
Consiste en modificar los campos "value" del archivo .PitchTier con los
nuevos valores deseados.

-----

3) Resíntesis del audio con el nuevo pitch track.
   
Por último, resintetizamos el audio original, forzando el nuevo pitch
track, con este comando:
  praat reemplazar-pitch-track.praat IN1 IN2 OUT MINPITCH MAXPITCH
donde:
  IN1 es un archivo wav.
  IN2 es un archivo PitchTier.
  OUT es el nombre del archivo wav a crear.
  MINPITCH y MAXPITCH son el rango tonal del hablante en Hz.

Ejemplo:
  praat reemplazar-pitch-track.praat 12345.wav 12345-mod.PitchTier 12345-mod.wav 50 300
Esto genera el archivo 12345-mod.wav.

-----

Procesamiento del Habla - DC, FCEyN, UBA
Agustín Gravano
Septiembre 2019

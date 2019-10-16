import sys
import os
from subprocess import Popen, PIPE
import re
import numpy as np

PRAAT= '/usr/bin/praat'

diphone_folder = './difonos/'


# Sintetiza un string en lenguaje L, que puede ser pregunta
# y escribe el resutlado en el filename dado .
def synthesize(word, output_filename):
    is_interrogation = False

    if word[-1] == '?':
        word = word[:-1]
        is_interrogation = True

    diphones = diphone_list(word)

    if is_interrogation:
        transform_to_interrogation(diphones)

    concatenate(diphones, output_filename)


def main():
    synthesize(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()


def run_praat(script_file, args):
    args = [PRAAT, '--run', script_file, args]
    p = Popen(args, stdout=PIPE)
    p.wait()


# dada una lista de archivos de sonido (con difonos) y un path,
# usa praat para concatenar todos los difonos y grabar el resultado path.
def concatenate(filenames, output_name):

    script = ""
    for i, f in enumerate(filenames):
        script += "Read from file: \"" + f + "\"\n"
        script += "selectObject: \"Sound " + f[-6:-4] + "\"\n"
        script += "Rename: \"" + f[-6:-4] + str(i) + "\"\n"

    script += "selectObject: \"Sound " + filenames[0][-6:-4] + str(0) + "\"\n"
    for i, f in enumerate(filenames[1:]):
        script += "plusObject: \"Sound " + f[-6:-4] + str(i+1) + "\"\n"

    script += "Concatenate recoverably\n"
    script += "selectObject: \"Sound chain\"\n"
    script += "Write to WAV file: \"" + output_name + "\"\n"
    script += "Save as text file: \"" + output_name + ".TextGrid\"\n"

    with open("concatenar.praat", "w") as cf:
        cf.write(script)

    run_praat("concatenar.praat", "")


all_diphones = ["-e", "-E", "-f", "-k", "-m", "-s", "-t", "e-", "E-",
           "s-", "ee", "eE", "Ee", "EE", "fe", "fE", "ke", "kE",
           "me", "mE", "se", "sE", "te", "tE", "re", "rE", "ef",
           "Ef", "ek", "Ek", "em", "Em", "es", "Es", "et", "Et",
           "er", "Er", "fr", "kr", "tr", "sf", "sk", "st", "ss",
           "sm"]

wavsufix = ".wav"


# lista los nombres de los archivos de los difonos para una palabra.
def diphone_list(word):
    diphones = []
    word = "-" + word + "-"
    for i, _ in enumerate(word[:-1]):
        diphone = word[i:i+2]
        if diphone not in all_diphones:
            print("ERROR: invalid word. Try again.")
            sys.exit(1)
        diphones.append(diphone)
    # print(diphones)
    # agregar prefijo y sufijo
    return list(map(lambda s: diphone_folder + s + wavsufix, diphone_list))


pitch_start_range = 90
pitch_end_range = 300


def extract_pitch_track(filename):
    args = " "
    args += filename + ".wav " + filename + ".PitchTier " + str(pitch_start_range) + " " + str(pitch_end_range)
    run_praat("extraer-pitch-track.praat", args )


def replace_pitch_track(inputSound, inputPitch, outSound):
    args = " "
    args += inputSound + " " + inputPitch + " " + outSound + " " + str(pitch_start_range) + " " + str(pitch_end_range)
    run_praat("reemplazar-pitch-track.praat", args )


def modify_pitch_track( pitchTierIn, pitchTierOut, f=lambda p, t, pmin, pmax: 2*p ):
    with open(pitchTierIn, 'r') as inF:
        file = inF.read()

    file = file.split("\n")
    pmin = 300.0
    pmax = 0.0
    xmin = 5.0
    xmax = -1.9
    for line in file:
        if "number" in line:
            number = float(line[12:])
            if number < xmin:
                xmin = number
            if number > xmax:
                xmax = number
        elif "value" in line:
            pitch = float(line[12:])
            if pitch < pmin:
                pmin = pitch
            if pitch > pmax:
                pmax = pitch

    with open(pitchTierOut, "w") as outF:
        number = 0.0
        for line in file:
            if "number" in line:
                number = float(line[12:])
            elif "value" in line:
                pitch = float(line[12:])
                pitch = f(pitch, (number-xmin)/(xmax - xmin), pmin, pmax)
                line = "    value = " + str(pitch)
            outF.write(line + "\n")


def variar_pitch(inF, outF, f):
    extract_pitch_track( inF )

    modify_pitch_track( inF + ".PitchTier", outF + ".PitchTier", f )

    replace_pitch_track( inF + ".wav", outF + ".PitchTier", outF + ".wav" )


def f_ascendente_250(p, t, pmin, pmax):
    maximo = 250
    res = (np.log((2**(maximo/pmax)-2)*t + 2)/np.log(2))*p
    return res

def f_ascendente_300(p, t, pmin, pmax):
    maximo = 300
    res = (np.log((2**(maximo/pmax)-2)*t + 2)/np.log(2))*p
    return res

def f_ascendente250_300(p, t, pmin, pmax):
    maximo = 300
    minimo = 250

    res = (np.log((2**(maximo/pmax)-2**(minimo/250))*t + 2**(minimo/250))/np.log(2))*p
    return res


mitad = 230 #Hz
full = 300 #Hz


def leer_pitch_track(filename):
    with open(filename, 'r') as f:
        res = f.read()
    return res


def variar(lista_difonos, f):
    pitch_tracks = []
    for difono in lista_difonos:
        difono = diphone_folder + difono + ".wav"
        extract_pitch_track(difono)
        pitch_track = leer_pitch_track(difono)
        re.match()

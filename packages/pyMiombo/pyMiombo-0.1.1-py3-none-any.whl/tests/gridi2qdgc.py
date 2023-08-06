# WWF-Tanzania
# Author: Langen R. Mathew
# e-mail: lmathew@wwftz.org

import math
import os
# ==============================================================================================
def leftPad(number, targetLength):
    output = str(number) + ''
    while (len(output)< targetLength):
        output = '0' + output

    return output
# ==============================================================================================
# Which Cell
def which_cell(lata, lona, latb, lonb, latc, lonc):
    latd = latb + ((latc - latb) / 2)
    lond = lonb + ((lonc - lonb) / 2)
    qdgcname = ""
    late1 = ""
    lone1 = ""
    late2 = ""
    lone2 = ""

    if lata < latd and lona < lond:
        qdgcname = "A"
        late1 = latb
        lone1 = lonb
        late2 = latd
        lone2 = lond
    elif lata < latd and lona >= lond:
        qdgcname = "B"
        late1 = latb
        lone1 = lond
        late2 = latd
        lone2 = lonc
    elif lata >= latd and lona < lond:
        qdgcname = "C"
        late1 = latd
        lone1 = lonb
        late2 = latc
        lone2 = lond
    elif lata >= latd and lona >= lond:
        qdgcname = "D"
        late1 = latd
        lone1 = lond
        late2 = latc
        lone2 = lonc

    qdgcname = qdgcname + "," + str(late1) + "," + str(lone1) + "," + str(late2) + "," + str(lone2)
    return qdgcname
# ==============================================================================================
# QDGC 0
def gridi0qdgc(qdgclata, qdgclona):
    hemie = ""
    hemig = ""

    if qdgclata < 0:
        hemie = "S"
    else:
        hemie = "N"

    if qdgclona < 0:
        hemig = "W"
    else:
        hemig = "E"

    lata = abs(qdgclata)
    lona = abs(qdgclona)
    latb = math.trunc(lata)
    lonb = math.trunc(lona)

    if (latb < 180):
        latc1 = latb
        latc2 = latb + 1
    if (latb < 90):
        lonc1 = lonb
        lonc2 = lonb + 1

    if (hemie == "S"):
        latd1 = -1 * latc1
        latd2 = -1 * latc2
    else:
        latd1 = latc1
        latd2 = latc2

    if hemig == "W":
        lond1 = -1 * lonc1
        lond2 = -1 * lonc2
    else:
        lond1 = lonc1
        lond2 = lonc2

    qdgclatb = leftPad(latc1, 2)
    qdgclonb = leftPad(lonc1, 3)

    qdgcname1 = hemig + qdgclonb + hemie + qdgclatb
    return str(qdgcname1) + "," + str(latd1) + "," + str(lond1) + "," + str(latd2) + "," + str(lond2)
# ==============================================================================================
# QDGC 1
def gridi1qdgc(qdgclata, qdgclona):
    qdgc_f0a = gridi0qdgc(qdgclata, qdgclona)
    qdgc_f0b = qdgc_f0a.split(",")
    qdgc_f0c = qdgc_f0b[0]

    flatb = abs(float(qdgc_f0b[1])) * 3600
    flonb = abs(float(qdgc_f0b[2])) * 3600
    flatc = abs(float(qdgc_f0b[3])) * 3600
    flonc = abs(float(qdgc_f0b[4])) * 3600
    flata = abs(qdgclata) * 3600
    flona = abs(qdgclona) * 3600

    qdgc30min = which_cell(flata, flona, flatb, flonb, flatc, flonc)
    qdgc30mina = qdgc30min.split(",")
    qdgc30minb = qdgc30mina[0]
    lat30mina = float(qdgc30mina[1])
    lon30mina = float(qdgc30mina[2])
    lat30minb = float(qdgc30mina[3])
    lon30minb = float(qdgc30mina[4])

    if qdgclata < 0:
        latf1 = float(-1) * (lat30mina/3600)
        latf2 = -1 * (lat30minb/3600)
    else:
        latf1 = lat30mina/3600
        latf2 = lat30minb/3600

    if qdgclona < 0:
        lonf1 = -1 * (lon30mina/3600)
        lonf2 = -1 * (lon30minb/3600)
    else:
        lonf1 = lon30mina/3600
        lonf2 = lon30minb/3600

    return qdgc_f0c + qdgc30minb + "," + str(latf1) + "," + str(lonf1) + "," + str(latf2) + "," + str(lonf2)
# ==============================================================================================
# QDGC 2
def gridi2qdgc(qdgclata, qdgclona):
    qdgc_f0a = gridi1qdgc(qdgclata, qdgclona)
    qdgc_f0b = qdgc_f0a.split(",")
    qdgc_f0c = qdgc_f0b[0]

    flatb = abs(float(qdgc_f0b[1])) * 3600
    flonb = abs(float(qdgc_f0b[2])) * 3600
    flatc = abs(float(qdgc_f0b[3])) * 3600
    flonc = abs(float(qdgc_f0b[4])) * 3600
    flata = abs(qdgclata) * 3600
    flona = abs(qdgclona) * 3600

    qdgc30min = which_cell(flata, flona, flatb, flonb, flatc, flonc)
    qdgc30mina = qdgc30min.split(",")
    qdgc30minb = qdgc30mina[0]
    lat30mina = float(qdgc30mina[1])
    lon30mina = float(qdgc30mina[2])
    lat30minb = float(qdgc30mina[3])
    lon30minb = float(qdgc30mina[4])

    if qdgclata < 0:
        latf1 = float(-1) * (lat30mina/3600)
        latf2 = -1 * (lat30minb/3600)
    else:
        latf1 = lat30mina/3600
        latf2 = lat30minb/3600

    if qdgclona < 0:
        lonf1 = -1 * (lon30mina/3600)
        lonf2 = -1 * (lon30minb/3600)
    else:
        lonf1 = lon30mina/3600
        lonf2 = lon30minb/3600

    return qdgc_f0c + qdgc30minb + "," + str(latf1) + "," + str(lonf1) + "," + str(latf2) + "," + str(lonf2)
# ==============================================================================================
# QDGC 3
def gridi3qdgc(qdgclata, qdgclona):
    qdgc_f0a = gridi2qdgc(qdgclata, qdgclona)
    qdgc_f0b = qdgc_f0a.split(",")
    qdgc_f0c = qdgc_f0b[0]

    flatb = abs(float(qdgc_f0b[1])) * 3600
    flonb = abs(float(qdgc_f0b[2])) * 3600
    flatc = abs(float(qdgc_f0b[3])) * 3600
    flonc = abs(float(qdgc_f0b[4])) * 3600
    flata = abs(qdgclata) * 3600
    flona = abs(qdgclona) * 3600

    qdgc30min = which_cell(flata, flona, flatb, flonb, flatc, flonc)
    qdgc30mina = qdgc30min.split(",")
    qdgc30minb = qdgc30mina[0]
    lat30mina = float(qdgc30mina[1])
    lon30mina = float(qdgc30mina[2])
    lat30minb = float(qdgc30mina[3])
    lon30minb = float(qdgc30mina[4])

    if qdgclata < 0:
        latf1 = float(-1) * (lat30mina/3600)
        latf2 = -1 * (lat30minb/3600)
    else:
        latf1 = lat30mina/3600
        latf2 = lat30minb/3600

    if qdgclona < 0:
        lonf1 = -1 * (lon30mina/3600)
        lonf2 = -1 * (lon30minb/3600)
    else:
        lonf1 = lon30mina/3600
        lonf2 = lon30minb/3600

    return qdgc_f0c + qdgc30minb + "," + str(latf1) + "," + str(lonf1) + "," + str(latf2) + "," + str(lonf2)
# ==============================================================================================
# QDGC 4
def gridi4qdgc(qdgclata, qdgclona):
    qdgc_f0a = gridi3qdgc(qdgclata, qdgclona)
    qdgc_f0b = qdgc_f0a.split(",")
    qdgc_f0c = qdgc_f0b[0]

    flatb = abs(float(qdgc_f0b[1])) * 3600
    flonb = abs(float(qdgc_f0b[2])) * 3600
    flatc = abs(float(qdgc_f0b[3])) * 3600
    flonc = abs(float(qdgc_f0b[4])) * 3600
    flata = abs(qdgclata) * 3600
    flona = abs(qdgclona) * 3600

    qdgc30min = which_cell(flata, flona, flatb, flonb, flatc, flonc)
    qdgc30mina = qdgc30min.split(",")
    qdgc30minb = qdgc30mina[0]
    lat30mina = float(qdgc30mina[1])
    lon30mina = float(qdgc30mina[2])
    lat30minb = float(qdgc30mina[3])
    lon30minb = float(qdgc30mina[4])

    if qdgclata < 0:
        latf1 = float(-1) * (lat30mina/3600)
        latf2 = -1 * (lat30minb/3600)
    else:
        latf1 = lat30mina/3600
        latf2 = lat30minb/3600

    if qdgclona < 0:
        lonf1 = -1 * (lon30mina/3600)
        lonf2 = -1 * (lon30minb/3600)
    else:
        lonf1 = lon30mina/3600
        lonf2 = lon30minb/3600

    return qdgc_f0c + qdgc30minb + "," + str(latf1) + "," + str(lonf1) + "," + str(latf2) + "," + str(lonf2)
# ==============================================================================================
# QDGC 5
def gridi5qdgc(qdgclata, qdgclona):
    qdgc_f0a = gridi4qdgc(qdgclata, qdgclona)
    qdgc_f0b = qdgc_f0a.split(",")
    qdgc_f0c = qdgc_f0b[0]

    flatb = abs(float(qdgc_f0b[1])) * 3600
    flonb = abs(float(qdgc_f0b[2])) * 3600
    flatc = abs(float(qdgc_f0b[3])) * 3600
    flonc = abs(float(qdgc_f0b[4])) * 3600
    flata = abs(qdgclata) * 3600
    flona = abs(qdgclona) * 3600

    qdgc30min = which_cell(flata, flona, flatb, flonb, flatc, flonc)
    qdgc30mina = qdgc30min.split(",")
    qdgc30minb = qdgc30mina[0]
    lat30mina = float(qdgc30mina[1])
    lon30mina = float(qdgc30mina[2])
    lat30minb = float(qdgc30mina[3])
    lon30minb = float(qdgc30mina[4])

    if qdgclata < 0:
        latf1 = float(-1) * (lat30mina/3600)
        latf2 = -1 * (lat30minb/3600)
    else:
        latf1 = lat30mina/3600
        latf2 = lat30minb/3600

    if qdgclona < 0:
        lonf1 = -1 * (lon30mina/3600)
        lonf2 = -1 * (lon30minb/3600)
    else:
        lonf1 = lon30mina/3600
        lonf2 = lon30minb/3600

    return qdgc_f0c + qdgc30minb + "," + str(latf1) + "," + str(lonf1) + "," + str(latf2) + "," + str(lonf2)
# ==============================================================================================
# WWF-Tanzania
# Author: Langen R. Mathew
# e-mail: lmathew@wwftz.org

import math
import os
# ==============================================================================================
# Hemisphere - South & North
def SouthNorth(foo):
    sn = 0
    if foo[4:5] == "S":
        sn = -1
    else:
        sn = 1
    return sn
# ---------------------------------------------------
# Hemisphere - East & West
def EastWest(foo):
    ew =0
    if foo[0:1] == "W":
        ew = -1
    else:
        ew = 1
    return ew
# ==============================================================================================
# QDGC 0
def qdgc0gridi(gridi0qdgc):
    gridiZero = gridi0qdgc[0:7]
    hemie = SouthNorth(gridi0qdgc)
    hemig = EastWest(gridi0qdgc)

    lata = hemie * float(gridi0qdgc[5:7])
    lona = hemig * float(gridi0qdgc[1:4])
    latb = hemie * (float(gridi0qdgc[5:7]) + 1)
    lonb = hemig * (float(gridi0qdgc[1:4]) + 1)

    jira = [lata,lona,latb,lonb]
    return jira
# ==============================================================================================
# QDGC 1
def qdgc1gridi(gridi1qdgc):
    gridiZero = qdgc0gridi(gridi1qdgc[0:7])
    gridiOne = gridi1qdgc[7:8]
    hemie = SouthNorth(gridi1qdgc)
    hemig = EastWest(gridi1qdgc)

    LatA = float(abs(gridiZero[0]))
    LonA = float(abs(gridiZero[1]))
    LatB = float(abs(gridiZero[2]))
    LonB = float(abs(gridiZero[3]))

    #Cell 1 Determination
    if gridiOne == "A":
        LatA = hemie * LatA
        LonA = hemig * LonA
        LatB = hemie * (LatB + 0.5)
        LonB = hemig * (LonB + 0.5)
    if gridiOne == "B":
        LatA = hemie * (LatA + 0.5)
        LonA = hemig * (LonA + 0.5)
        LatB = hemie * (LatB + 1)
        LonB = hemig * (LonB + 1)
    if gridiOne == "C":
        LatA = hemie * (LatA + 0.5)
        LonA = hemig * (LonA + 0.5)
        LatB = hemie * LatB
        LonB = hemig * LonB
    if gridiOne == "D":
        LatA = hemie * (LatA + 1)
        LonA = hemig * (LonA + 1)
        LatB = hemie * (LatB + 0.5)
        LonB = hemig * (LonB + 0.5)

    jira = [LatA, LonA, LatB, LonB]
    return jira
# ==============================================================================================
# QDGC 2
def qdgc2gridi(gridi2qdgc):
    gridiOne = qdgc1gridi(gridi2qdgc)
    gridiTwo = gridi2qdgc[8:9]
    hemie = SouthNorth(gridi2qdgc)
    hemig = EastWest(gridi2qdgc)

    LatA = float(abs(gridiOne[0]))
    LonA = float(abs(gridiOne[1]))
    LatB = float(abs(gridiOne[2]))
    LonB = float(abs(gridiOne[3]))

    #Cell Level 2 Determination
    if gridiTwo == "A":
        LatA = hemie * LatA
        LonA = hemig * LonA
        LatB = hemie * (LatB + 0.25)
        LonB = hemig * (LonB + 0.25)
    if gridiTwo == "B":
        LatA = hemie * (LatA + 0.25)
        LonA = hemig * (LonA + 0.25)
        LatB = hemie * (LatB + 0.5)
        LonB = hemig * (LonB + 0.5)
    if gridiTwo == "C":
        LatA = hemie * (LatA + 0.25)
        LonA = hemig * (LonA + 0.25)
        LatB = hemie * LatB
        LonB = hemig * LonB
    if gridiTwo == "D":
        LatA = hemie * (LatA + 0.5)
        LonA = hemig * (LonA + 0.5)
        LatB = hemie * (LatB + 0.25)
        LonB = hemig * (LonB + 0.25)

    jira = [LatA, LonA, LatB, LonB]
    return jira
# ==============================================================================================
# QDGC 3
def qdgc3gridi(gridi3qdgc):
    gridiTwo = qdgc1gridi(gridi3qdgc)
    gridiThree = gridi3qdgc[9:10]
    hemie = SouthNorth(gridi3qdgc)
    hemig = EastWest(gridi3qdgc)

    LatA = float(abs(gridiTwo[0]))
    LonA = float(abs(gridiTwo[1]))
    LatB = float(abs(gridiTwo[2]))
    LonB = float(abs(gridiTwo[3]))

    #Cell Level 3 Determination
    if gridiThree == "A":
        LatA = hemie * LatA
        LonA = hemig * LonA
        LatB = hemie * (LatB + 0.125)
        LonB = hemig * (LonB + 0.125)
    if gridiThree == "B":
        LatA = hemie * (LatA + 0.125)
        LonA = hemig * (LonA + 0.125)
        LatB = hemie * (LatB + 0.25)
        LonB = hemig * (LonB + 0.25)
    if gridiThree == "C":
        LatA = hemie * (LatA + 0.125)
        LonA = hemig * (LonA + 0.125)
        LatB = hemie * LatB
        LonB = hemig * LonB
    if gridiThree == "D":
        LatA = hemie * (LatA + 0.25)
        LonA = hemig * (LonA + 0.25)
        LatB = hemie * (LatB + 0.125)
        LonB = hemig * (LonB + 0.125)

    jira = [LatA, LonA, LatB, LonB]
    return jira
# ==============================================================================================
# QDGC 4
def qdgc4gridi(gridi4qdgc):
    gridiThree = qdgc1gridi(gridi4qdgc)
    gridiFour = gridi4qdgc[9:10]
    hemie = SouthNorth(gridi4qdgc)
    hemig = EastWest(gridi4qdgc)

    LatA = float(abs(gridiThree[0]))
    LonA = float(abs(gridiThree[1]))
    LatB = float(abs(gridiThree[2]))
    LonB = float(abs(gridiThree[3]))

    #Cell Level 3 Determination
    if gridiFour == "A":
        LatA = hemie * LatA
        LonA = hemig * LonA
        LatB = hemie * (LatB + 0.0625)
        LonB = hemig * (LonB + 0.0625)
    if gridiFour == "B":
        LatA = hemie * (LatA + 0.0625)
        LonA = hemig * (LonA + 0.0625)
        LatB = hemie * (LatB + 0.125)
        LonB = hemig * (LonB + 0.125)
    if gridiFour == "C":
        LatA = hemie * (LatA + 0.0625)
        LonA = hemig * (LonA + 0.0625)
        LatB = hemie * LatB
        LonB = hemig * LonB
    if gridiFour == "D":
        LatA = hemie * (LatA + 0.125)
        LonA = hemig * (LonA + 0.125)
        LatB = hemie * (LatB + 0.0625)
        LonB = hemig * (LonB + 0.0625)

    jira = [LatA, LonA, LatB, LonB]
    return jira
# ==============================================================================================
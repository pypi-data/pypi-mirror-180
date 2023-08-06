# WWF-Tanzania
# Author: Langen R. Mathew
# e-mail: lmathew@wwftz.org

import math
import os

# ==============================================================================================
# QDGC 0
def qdgc0gridi(gridi0qdgc):
    gridiZero = gridi0qdgc[0:7]
    hemie = 0
    hemig = 0

    if gridi0qdgc[4:5] == "S":
        hemie = -1
    else:
        hemie = 1

    if gridi0qdgc[0:1] == "W":
        hemig = -1
    else:
        hemig = 1

    print(gridi0qdgc[1:4])
    lata = hemie * float(gridi0qdgc[5:7])
    lona = hemig * float(gridi0qdgc[1:4])
    latb = hemie * (float(gridi0qdgc[5:7]) + 1)
    lonb = hemig * (float(gridi0qdgc[1:4]) + 1)

    return str(lata) + "," + str(lona) + "," + str(latb) + "," + str(lonb)
# ==============================================================================================
# QDGC 1
def qdgc1gridi(gridi1qdgc):
    gridi0qdgc = gridi1qdgc[0:7]
    gridiOne = gridi1qdgc[7:8]
    print(gridiOne)
    #----------------------------------
    hemie = 0
    hemig = 0
    LatA = 0
    LonA = 0
    LatB = 0
    LonB = 0

    #Hemisphere
    if gridi0qdgc[4:5] == "S":
        hemie = -1
    else:
        hemie = 1

    if gridi0qdgc[0:1] == "W":
        hemig = -1
    else:
        hemig = 1

    #Cell 1 Determination
    if gridiOne == "A":
        LatA = hemie * float(gridi0qdgc[5:7])
        LonA = hemig * float(gridi0qdgc[1:4])
        LatB = hemie * (float(gridi0qdgc[5:7]) + 0.5)
        LonB = hemig * (float(gridi0qdgc[1:4]) + 0.5)
    if gridiOne == "B":
        LatA = hemie * (float(gridi0qdgc[5:7]) + 0.5)
        LonA = hemig * (float(gridi0qdgc[1:4]) + 0.5)
        LatB = hemie * (float(gridi0qdgc[5:7]) + 1)
        LonB = hemig * (float(gridi0qdgc[1:4]) + 1)
    if gridiOne == "C":
        LatA = hemie * (float(gridi0qdgc[5:7]) + 0.5)
        LonA = hemig * (float(gridi0qdgc[1:4]) + 0.5)
        LatB = hemie * (float(gridi0qdgc[5:7]))
        LonB = hemig * (float(gridi0qdgc[1:4]))
    if gridiOne == "D":
        LatA = hemie * (float(gridi0qdgc[5:7]) + 1)
        LonA = hemig * (float(gridi0qdgc[1:4]) + 1)
        LatB = hemie * (float(gridi0qdgc[5:7]) + 0.5)
        LonB = hemig * (float(gridi0qdgc[1:4]) + 0.5)

    return str(LatA) + "," + str(LonA) + "," + str(LatB) + "," + str(LonB)
# ==============================================================================================
# QDGC 2
def qdgc2gridi(gridi2qdgc):
    gridi0qdgc = gridi2qdgc[0:7]
    gridiOne = gridi2qdgc[7:8]
    gridiTwo = gridi2qdgc[8:9]
    print(gridiTwo)
    #----------------------------------
    hemie = 0
    hemig = 0
    LatA = 0
    LonA = 0
    LatB = 0
    LonB = 0

    #Hemisphere
    if gridi0qdgc[4:5] == "S":
        hemie = -1
    else:
        hemie = 1

    if gridi0qdgc[0:1] == "W":
        hemig = -1
    else:
        hemig = 1

    #Cell Level 1 Determination
    if gridiOne == "A":
        LatA = float(gridi0qdgc[5:7])
        LonA = float(gridi0qdgc[1:4])
        LatB = float(gridi0qdgc[5:7]) + 0.5
        LonB = float(gridi0qdgc[1:4]) + 0.5
    if gridiOne == "B":
        LatA = float(gridi0qdgc[5:7]) + 0.5
        LonA = float(gridi0qdgc[1:4]) + 0.5
        LatB = float(gridi0qdgc[5:7]) + 1
        LonB = float(gridi0qdgc[1:4]) + 1
    if gridiOne == "C":
        LatA = float(gridi0qdgc[5:7]) + 0.5
        LonA = float(gridi0qdgc[1:4]) + 0.5
        LatB = float(gridi0qdgc[5:7])
        LonB = float(gridi0qdgc[1:4])
    if gridiOne == "D":
        LatA = float(gridi0qdgc[5:7]) + 1
        LonA = float(gridi0qdgc[1:4]) + 1
        LatB = float(gridi0qdgc[5:7]) + 0.5
        LonB = float(gridi0qdgc[1:4]) + 0.5

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

    return str(LatA) + "," + str(LonA) + "," + str(LatB) + "," + str(LonB)
# ==============================================================================================
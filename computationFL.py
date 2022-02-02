
import numpy as np


def AOV(sensorWidth,focla_Length):
    val = 2 * np.arctan( sensorWidth / (2*focla_Length))

    return val

def FOV( aov, distOfSub):
    val = 2 * ( np.tan(aov/2)*distOfSub)



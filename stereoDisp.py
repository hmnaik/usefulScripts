import numpy as np
import matplotlib as mplot

# a program to compute the stereo stat for the depth measurement

# All measurement in mm

b = 5 * 1000 # dist btwn camera
z = 300 * 1000 # target distance

deltaZ = 0.1 * 1000 # depth resolution required
f = 35 # focal length

deltaD = deltaZ * (f*b)/(z*z)

print ("delta D " , deltaD)
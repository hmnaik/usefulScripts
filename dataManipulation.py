import numpy as np

def manip(x):
    alpha = -255/8000
    beta = 255
    return round((x*alpha) + beta)

def inmanip(x):
    return round((x-255)*(-8000/255))

# Define a matrix
img = [ 500, 510, 700, 710, 720, 730, 1000,2000,3000, 7000,7010, 7020 ]

mapped = list(map(manip,img))

invmapped = list(map(inmanip,mapped))

print(img , mapped , invmapped)





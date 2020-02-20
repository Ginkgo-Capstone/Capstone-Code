# Meteorological Preprocessor
# PCLI site-specific
# Written by Kyle Heyblom, 02/19/20

temp = 275.9
month = 1
udir = 298
B0Win = 0.22
B0Spr = 0.29
B0Sum = 0.28
B0Fal = 0.32
z0WIN = [[1,0.157],
        [20,0.008],
        [75,0.005],
        [175,0.011],
        [205,0.195],
        [240,0.092],
        [270,0.166],
        [300,0.357],
        [340,0.157]]
z0SPR = [[1,0.208],
        [20,0.009],
        [75,0.005],
        [175,0.013],
        [205,0.268],
        [240,0.124],
        [270,0.226],
        [300,0.443],
        [340,0.208]]
z0SUM = [[1,0.239],
        [20,0.01],
        [75,0.005],
        [175,0.014],
        [205,0.403],
        [240,0.204],
        [270,0.273],
        [300,0.457],
        [340,0.239]]
z0FAL = [[1,0.235],
        [20,0.01],
        [75,0.005],
        [175,0.014],
        [205,0.403],
        [240,0.204],
        [270,0.273],
        [300,0.452],
        [340,0.235]]


from math import *
from densityf import densityf
from bowenf import bowenf
from surfrf import surfrf

# Set site parameters
lat = 43.5017 #latitude
long = 79.6117 #longitude
timezone = 5 #timezone
spres = 1003.0 #surface pressure
cp = 1004.0 #specific heat capacity

# Calculate air density
rho = densityf(temp,spres)

# Set Bowen ratio based on season
B0 = bowenf(month,B0Win,B0Spr,B0Sum,B0Fal)

# Set surface roughness based on wind direction and season
z0 = surfrf(udir,month,z0WIN,z0SPR,z0SUM,z0FAL)



# Meteorological Preprocessor
# PCLI site-specific
# Written by Kyle Heyblom, Ginkgo Solutions
# Completed: Feb. 20/20

###SBL draft input
##month = 1
##yday = 1
##hour = 2
##temp = 275.9
##u = 6.7
##udir = 298
##cc = 2
##zim_p = 3593

#CBL draft input
month = 1
yday = 1
hour = 13
temp = 274.9
u = 4.1
udir = 3
cc = 9 ###ASSUMED###
zic = 370 ###ASSUMED###
zim_p = 1068

zref = 10
B0WIN = 0.22
B0SPR = 0.29
B0SUM = 0.28
B0FAL = 0.32
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
rnoonWIN = 0.27
rnoonSPR = 0.13
rnoonSUM = 0.13
rnoonFAL = 0.13


from math import *
from densityf import densityf
from bowenf import bowenf
from surfrf import surfrf
from solelevf import solelevf
from albedof import albedof
from critsolelevf import critsolelevf
from stabilityflagf import stabilityflagf
from heatfluxCBLf import heatfluxCBLf
from ustarCBLf import ustarCBLf
from wstarf import wstarf
from ustarSBLf import ustarSBLf
from monubSBLf import monubSBLf
from heatfluxSBLf import heatfluxSBLf
from mmixheightf import mmixheightf

# Set site parameters
lat = 43.5017 #latitude
long = 79.6117 #longitude
timezone = 5 #timezone
spres = 1003.0 #surface pressure
cp = 1004.0 #specific heat capacity

# Calculate air density
rho = densityf(temp,spres)

# Set Bowen ratio based on season
B0 = bowenf(month,B0WIN,B0SPR,B0SUM,B0FAL)

# Set surface roughness based on wind direction and season
z0 = surfrf(udir,month,z0WIN,z0SPR,z0SUM,z0FAL)

# Calculate solar elevation angle
solang = solelevf(lat,long,timezone,yday,hour)

# Calculate albedo
r = albedof(solang,month,rnoonWIN,rnoonSPR,rnoonSUM,rnoonFAL)

# Calculate critical solar elevation angle
critang = critsolelevf(cc,temp,solang,month,rnoonWIN,rnoonSPR,rnoonSUM,rnoonFAL)

# Determine whether convective (CBL) or stable (SBL) boundary layer
# 1 = CBL; 0 = SBL
stabflag = stabilityflagf(solang,critang)


if stabflag == 1:

    # -------- CBL Paramters -------- #

    # Calculate heat flux from cloud cover
    H = heatfluxCBLf(solang,cc,r,temp,B0)

    # Calculate surface friction velocity and Monin-Obukhov length
    ustar, L = ustarCBLf(u,zref,z0,rho,cp,temp,H) ###Remember to add max min caps from verify functions###

    # Calculate turbulent velocity scale
    wstar = wstarf(H,zic,rho,cp,temp) ###zic is assumed here###

elif stabflag == 0:

    # -------- SBL Paramters -------- #

    # Calculate surface friction velocity and temperature scale
    ustar, thetastar = ustarSBLf(u,zref,z0,temp,solang,critang,rho,cp)

    # Calculate Monin-Obukhov length
    L = monubSBLf(temp,thetastar,ustar)

    # Calculate heat flux
    H = heatfluxSBLf(rho,cp,ustar,thetastar)


# Calculate mechanical mixing height
zim = mmixheightf(ustar,zim_p)



    



    


    

    






















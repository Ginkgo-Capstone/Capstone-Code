def mmixheightf(ustar,zim_p):

    from math import exp

    zie = 2400*ustar**1.5

    if zim_p == -999:
        zim_p = zie

    beta = 2
    tau = zim_p/(beta*ustar)

    zim = zim_p*exp(-3600/tau)+zie*(1-exp(-3600/tau))

    if zim > 4000:
        zim = 4000

    return zim

    
    

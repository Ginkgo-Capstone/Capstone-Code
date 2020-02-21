def densityf(temp,pres):

    RD = 287.04
    rho = pres*100.0 / (RD*temp)

    if rho < 0.75:
        rho = 0.75

    return rho
    

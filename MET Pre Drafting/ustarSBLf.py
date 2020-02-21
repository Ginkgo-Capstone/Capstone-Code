def ustarSBLf(u,zref,z0,temp,solang,critang,rho,cp):

    from math import exp
    from math import log
    from math import sqrt
    from math import acos
    from math import cos

    k = 0.4 #von Karman constant
    g = 9.80655 #acceleration due to gravity
    betaM = 4.7

    CD = k / log((zref-5*z0)/z0)

    thetastar = 0.08

    if solang > 0 and solang < critang:
        thetastar = thetastar*(1-(solang/critang)**2)

    u0 = (betaM*(zref-4*z0)*g*thetastar / temp)**0.5

    chek = (2*u0/((CD**0.5)*u))**2

    ustar = (CD*u/2) * ((1 + exp(-1*chek/2)) / (1 - exp(-2/sqrt(chek))))

    ucrit = 2*u0/sqrt(CD)
    ustarcrit = CD*ucrit/4

    ustar = max(ustar,ustarcrit)

    if chek > 1:
        thetastar = thetastar*u/ucrit

    HLIM = -64
    XLIMIT = -HLIM/(rho*cp) #kinematic heat flux

    if ustar*thetastar > XLIMIT:

        AA = -CD*u
        BB = 0.0
        CC = betaM*(zref-5*z0)*g*XLIMIT*CD / temp

        A3 = AA/3
        AP = BB - AA*A3
        BP = 2*A3**3-A3*BB+CC
        AP3 = AP/3
        BP2 = BP/2
        TROOT = BP2*BP2+AP3*AP3*AP3

        flag = 0
        if TROOT > 0:
            TR = sqrt(TROOT)
            TEST = -BP2 + TR
            BSV = -BP2 - TR

            if TEST < 0:
                ustar = -9
                flag = 1
            else:
                APP = TEST**(1/3)

            if BSV != 0 and flag == 0:
                BPP = BSV**(1/3)
                ustar = APP+BPP-A3
                flag = 1
            elif flag == 0:
                ustar = APP-A3
        elif flag == 0:
            CM = 2*sqrt(-AP3)
            ALPHA = acos(BP/(AP3*CM))/3
            ustar = CM*cos(ALPHA)-A3

        if ustar != -9:
            thetastar = XLIMIT/ustar
        else:
            thetastar = -HLIM / (rho*cp*ustar)

    return ustar, thetastar





            
            
        
                










        

    

    

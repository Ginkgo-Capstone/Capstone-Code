def ustarCBLf(u,zref,z0,rho,cp,temp,H):

    from math import log
    from math import atan
    from math import pi

    k = 0.4 #von Karman constant
    g = 9.80655 #acceleration due to gravity

    errTol = 0.01
    iters = 0

    psiMref = 0
    psiM0 = 0
    Lold  = -9999

    ustar = k*u / (log(zref/z0)-psiMref+psiM0)
    L = -rho*cp*temp*(ustar**3)/(k*g*H)

    while abs(Lold-L) > abs(errTol*L) and iters < 1000:
        iters = iters + 1

        Lold = L

        mu = (1-16*zref/L)**0.25
        mu0 = (1-16*z0/L)**0.25

        psiMref = 2*log((1+mu)/2) + log((1+mu**2)/2) - 2*atan(mu) + pi/2
        psiM0 = 2*log((1+mu0)/2) + log((1+mu0**2)/2) - 2*atan(mu0) + pi/2

        ustar = k*u / (log(zref/z0)-psiMref+psiM0)
        L = -rho*cp*temp*(ustar**3)/(k*g*H)

    if L > 8888:
        L = 8888
    elif L < -8888:
        L = -8888

    return ustar, L

        

        
        
        

    
    

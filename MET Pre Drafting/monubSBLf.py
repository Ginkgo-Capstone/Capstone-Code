def monubSBLf(temp,thetastar,ustar):

    
    k = 0.4 #von Karman constant
    g = 9.80655 #acceleration due to gravity

    Ladj = 1100*ustar**2
    L = (temp*ustar**2) / (k*g*thetastar) 
    L = max(L,Ladj)

    if L > 8888:
        L = 8888
    elif L < -8888:
        L = -8888

    return L

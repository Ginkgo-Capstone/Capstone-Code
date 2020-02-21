def wstarf(H,zic,rho,cp,temp):

    g = 9.80655 #acceleration due to gravity

    wstar = (g*H*zic / (rho*cp*temp))**(1/3)

    return wstar

    

def albedof(solang,month,rnoonWIN,rnoonSPR,rnoonSUM,rnoonFAL):

    from math import exp

    a = -0.1

    if month == 12 or month == 1 or month == 2:
        b = -0.5*(1-rnoonWIN)**2
        r = rnoonWIN + (1-rnoonWIN)*exp(a*solang+b)
        return r
    elif month == 3 or month == 4 or month == 5:
        b = -0.5*(1-rnoonSPR)**2
        r = rnoonSPR + (1-rnoonSPR)*exp(a*solang+b)
        return r
    elif month == 6 or month == 7 or month == 8:
        b = -0.5*(1-rnoonSUM)**2
        r = rnoonSUM + (1-rnoonSUM)*exp(a*solang+b)
        return r
    elif month == 9 or month == 10 or month == 11:
        b = -0.5*(1-rnoonFAL)**2
        r = rnoonFAL + (1-rnoonFAL)*exp(a*solang+b)
        return r
    else:
        r = -999
        return r

    

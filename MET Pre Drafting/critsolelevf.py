def critsolelevf(cc,temp,solang,month,rnoonWIN,rnoonSPR,rnoonSUM,rnoonFAL):

    from math import sin
    from math import asin
    from math import degrees

    from albedof import albedof
    
    c1 = 5.31e-13
    c2 = 60
    SB = 5.67e-8

    critang_old = 0
    critang = solang
    iters = 0
    errTol = 0.01
    
    while abs(critang_old-critang) > abs(errTol*critang) and iters <= 20:

        iters = iters + 1
        critang_old = critang

        r = albedof(critang,month,rnoonWIN,rnoonSPR,rnoonSUM,rnoonFAL)

        critang = asin( 1/990 * ((-c1*temp**6+SB*temp**4-c2*cc/10)/((1-r)*(1-0.75*(cc/10)**3.4)) + 30) )

        if sin(critang) <= 0.0:
            critang = 0.0
        elif sin(critang) > 1.0:
            critang = 92
        else:
            critang = degrees(critang)

    return critang
            

def heatfluxCBLf(solang,cc,r,temp,B0):

    from math import sin
    from math import asin
    from math import radians

    c1 = 5.31e-13
    c2 = 60
    c3 = 1.12
    SB = 5.67e-8

    R0 = 990*sin(radians(solang))-30

    if solang < asin(radians(30/990)):
        R0 = 0

    R = R0*(1-0.75*(cc/10)**3.4)

    T1 = (1-r)*R
    T2 = c1*temp**6
    T3 = -SB*temp**4
    T4 = c2*(cc/10)
    T5 = c3

    Rn = (T1+T2+T3+T4)/T5

    H = 0.9*Rn/(1+1/B0)

    return H

def surfrf(udir,month,z0WIN,z0SPR,z0SUM,z0FAL):

    if month == 12 or month == 1 or month == 2:

        for i in range(len(z0WIN)):
            if i == len(z0WIN)-1:
                z0 = z0WIN[i][1]
                return z0
            elif udir >= z0WIN[i][0] and udir < z0WIN[i+1][0]:
                z0 = z0WIN[i][1]
                return z0

    elif month == 3 or month == 4 or month == 5:

        for i in range(len(z0SPR)):
            if i == len(z0SPR)-1:
                z0 = z0SPR[i][1]
                return z0
            elif udir >= z0SPR[i][0] and udir < z0SPR[i+1][0]:
                z0 = z0SPR[i][1]
                return z0
    
    elif month == 6 or month == 7 or month == 8:

        for i in range(len(z0SUM)):
            if i == len(z0SUM)-1:
                z0 = z0SUM[i][1]
                return z0
            elif udir >= z0SUM[i][0] and udir < z0SUM[i+1][0]:
                z0 = z0SUM[i][1]
                return z0
        
    elif month == 9 or month == 10 or month == 11:

        for i in range(len(z0FAL)):
            if i == len(z0FAL)-1:
                z0 = z0FAL[i][1]
                return z0
            elif udir >= z0FAL[i][0] and udir < z0FAL[i+1][0]:
                z0 = z0FAL[i][1]
                return z0
            
    else:
        z0 = -999
        return z0

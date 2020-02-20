def surfrf(udir,month,z0WIN,z0SPR,z0SUM,z0FAL):

    if month == 12 or month == 1 or month == 2:

        for i in range(2,len(z0WIN)+1):
            if i == len(z0WIN)+1:
                z0 = z0WIN[len(z0WIN)][1] ##INDEXING IS FUCKED
                break
            elif udir >= z0WIN[i-1][1] and udir < z0WIN[i][1]:
                z0 = z0WIN[i-1][1]
                break
        return z0

    elif month == 3 or month == 4 or month == 5:

        for i in range(1,len(z0SPR)):
            if i == len(z0SPR):
                z0 = z0SPR[len(z0SPR)-1][1]
                break
            elif udir >= z0SPR[i-1][1] and udir < z0SPR[i][1]:
                z0 = z0SPR[i-1][1]
                break
        return z0

    elif month == 6 or month == 7 or month == 8:

        for i in range(2,len(z0SUM)+1):
            if i == len(z0SUM)+1:
                z0 = z0SUM[len(z0SUM)][1]
                break
            elif udir >= z0SUM[i-1][1] and udir < z0SUM[i][1]:
                z0 = z0SUM[i-1][1]
                break
        return z0

    elif month == 9 or month == 10 or month == 11:

        for i in range(2,len(z0FAL)+1):
            if i == len(z0FAL)+1:
                z0 = z0FAL[len(z0FAL)][1]
                break
            elif udir >= z0FAL[i-1][1] and udir < z0FAL[i][1]:
                z0 = z0FAL[i-1][1]
                break
        return z0
    
    else:
        z0 = -999
        return z0

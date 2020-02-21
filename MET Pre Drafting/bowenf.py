def bowenf(month,B0Win,B0Spr,B0Sum,B0Fal):

    if month == 12 or month == 1 or month == 2:
        B0 = B0Win
        return B0
    elif month == 3 or month == 4 or month == 5:
        B0 = B0Spr
        return B0
    elif month == 6 or month == 7 or month == 8:
        B0 = B0Sum
        return B0
    elif month == 9 or month == 10 or month == 11:
        B0 = B0Fal
        return B0
    else:
        B0 = -999
        return B0

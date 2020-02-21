def solelevf(lat,long,timezone,yday,hour):

    from math import sin
    from math import cos
    from math import radians
    from math import degrees
    from math import atan2
    from math import sqrt

    TEMPZ  = 15.0*timezone - long

    # Set previous hour
    if hour == 24:
        hour_p = 1
        yday_p = y_day - 1
    else:
        hour_p = hour - 1
        yday_p = yday


    ## Calculate solar elevation angle for previous hour ##
    
    # Determine the fraction of a year for this date.
    dayNUM_p = (yday_p-1)*360.0/365.242

    # Account for ellipticity of earth's orbit.
    sigma_p = 279.9348 + (dayNUM_p) + 1.914827*sin(radians(dayNUM_p)) - 0.079525*cos(radians(dayNUM_p)) + 0.019938*sin(radians(2*dayNUM_p)) - 0.00162*cos(radians(2*dayNUM_p))

    # Determine time(hrs) of meridian passage
    AMM_p = 12.0 + 0.12357*sin(radians(dayNUM_p)) - 0.004289*cos(radians(dayNUM_p)) + 0.153809*sin(radians(2*dayNUM_p)) + 0.060783*cos(radians(2*dayNUM_p))

    # Determine solar hour angle(in radians)
    HI_p = (15.0 * (hour_p-AMM_p) + TEMPZ)
    ALFSN_p = sin(radians(lat))*sin(radians(23.44383))*sin(radians(sigma_p)) + sqrt(1.0-sin((radians(23.44383))*sin(radians(sigma_p)))**2)*cos(radians(lat))*cos(radians(HI_p))
    elevang_p = degrees(atan2(ALFSN_p,sqrt(1.0-ALFSN_p**2))) #degrees


    ## Calculate solar elevation angle for current hour ##
    
    # Determine the fraction of a year for this date.
    dayNUM = (yday-1)*360.0/365.242

    # Account for ellipticity of earth's orbit.
    sigma = 279.9348 + (dayNUM) + 1.914827*sin(radians(dayNUM)) - 0.079525*cos(radians(dayNUM)) + 0.019938*sin(radians(2*dayNUM)) - 0.00162*cos(radians(2*dayNUM))

    # Determine time(hrs) of meridian passage
    AMM = 12.0 + 0.12357*sin(radians(dayNUM)) - 0.004289*cos(radians(dayNUM)) + 0.153809*sin(radians(2*dayNUM)) + 0.060783*cos(radians(2*dayNUM))

    # Determine solar hour angle(in radians)
    HI = (15.0 * (hour-AMM) + TEMPZ)
    ALFSN = sin(radians(lat))*sin(radians(23.44383))*sin(radians(sigma)) + sqrt(1.0-sin((radians(23.44383))*sin(radians(sigma)))**2)*cos(radians(lat))*cos(radians(HI))
    elevang_c = degrees(atan2(ALFSN,sqrt(1.0-ALFSN**2))) #degrees


    elevang = (elevang_p+elevang_c)/2

    return elevang

def is_leap(year):
    if year%4==0:
        if year%100==0 and year%400!=0:
            leap = False
        else:
            leap = True
    else:
        leap = False
    # Write your logic here
    
    return leap

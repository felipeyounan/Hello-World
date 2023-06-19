def is_leap(year):
    leap = False
    biyf = year % 4
    biyc = year % 100
    biyq = year % 400
    if 1900 <= year <= 10**5:
        if biyf == 0:
            if biyc == 0:
                if biyq == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    return leap
year=int(input())
print(is_leap(year))

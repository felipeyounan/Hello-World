days = 29
rest = days % 7
while rest >= 0:
    days = days + 1
    rest = days % 7
    if rest == 0:
        week = days / 7
        #print(week)
        break
print(week)
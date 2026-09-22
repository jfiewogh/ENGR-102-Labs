sex = "F"
age = 40
cho = 105
smo = "N"
hdl = 60
sbp = 100
med = "N"

if sex == "F":
    points = 0
    if age < 35:
        points += -7
    elif age < 40:
        points += -3
    elif age < 45:
        points += 0
    elif age < 50:
        points += 3
    elif age < 55:
        points += 6
    elif age < 60:
        points += 8
    elif age < 65:
        points += 10
    elif age < 70:
        points += 12
    elif age < 75:
        points += 14
    else:
        points += 16

    if cho < 160:
        points += 0
    elif cho < 200:
        if age < 40:
            points += 4
        elif age < 50:
            points += 3
        elif age < 60:
            points += 2
        elif age < 70:
            points += 1
        else:
            points += 1
    elif cho < 240:
        if age < 40:
            points += 8
        elif age < 50:
            points += 6
        elif age < 60:
            points += 4
        elif age < 70:
            points += 2
        else:
            points += 1
    elif cho < 280:
        if age < 40:
            points += 11
        elif age < 50:
            points += 8
        elif age < 60:
            points += 5
        elif age < 70:
            points += 3
        else:
            points += 2
    else:
        if age < 40:
            points += 13
        elif age < 50:
            points += 10
        elif age < 60:
            points += 7
        elif age < 70:
            points += 4
        else:
            points += 2

    points += -1

    print(points)
else:
    points = 0





    print(points)
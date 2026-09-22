def print_risk(sex, age, cho, smo, hdl, sbp, med):
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

        if smo == "Y":
            if age < 40:
                points += 9
            elif age < 50:
                points += 7
            elif age < 60:
                points += 4
            elif age < 70:
                points += 2
            else:
                points += 1 

        if hdl < 40:
            points += 2
        elif hdl < 50:
            points += 1
        elif hdl < 60:
            points += 0
        else:
            points += -1

        if med == "Y":
            if sbp < 120:
                points += 0
            elif sbp < 130:
                points += 3
            elif sbp < 140:
                points += 4
            elif sbp < 160:
                points += 5
            else:
                points += 6
        else:
            if sbp < 120:
                points += 0
            elif sbp < 130:
                points += 1
            elif sbp < 140:
                points += 2
            elif sbp < 160:
                points += 3
            else:
                points += 4

        if points < 9:
            print("<1")
        elif points < 13:
            print("1")
        elif points < 15:
            print("2")
        elif points < 16:
            print("3")
        elif points < 17:
            print("4")
        elif points < 18:
            print("5")
        elif points < 19:
            print("6")
        elif points < 20:
            print("8")
        elif points < 21:
            print("11")
        elif points < 22:
            print("14")
        elif points < 23:
            print("17")
        elif points < 24:
            print("22")
        elif points < 25:
            print("27")
        else:
            print(">30")
    else:
        points = 0

        if age < 35:
            points += -9
        elif age < 40:
            points += -4
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
            points += 11
        elif age < 75:
            points += 12
        else:
            points += 13

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
                points += 0
        elif cho < 240:
            if age < 40:
                points += 7
            elif age < 50:
                points += 5
            elif age < 60:
                points += 3
            elif age < 70:
                points += 1
            else:
                points += 0
        elif cho < 280:
            if age < 40:
                points += 9
            elif age < 50:
                points += 6
            elif age < 60:
                points += 4
            elif age < 70:
                points += 2
            else:
                points += 1
        else:
            if age < 40:
                points += 11
            elif age < 50:
                points += 8
            elif age < 60:
                points += 5
            elif age < 70:
                points += 3
            else:
                points += 1

        if smo == "Y":
            if age < 40:
                points += 8
            elif age < 50:
                points += 5
            elif age < 60:
                points += 3
            elif age < 70:
                points += 1
            else:
                points += 1 

        if hdl < 40:
            points += 2
        elif hdl < 50:
            points += 1
        elif hdl < 60:
            points += 0
        else:
            points += -1

        if med == "Y":
            if sbp < 120:
                points += 0
            elif sbp < 130:
                points += 1
            elif sbp < 140:
                points += 2
            elif sbp < 160:
                points += 2
            else:
                points += 3
        else:
            if sbp < 120:
                points += 0
            elif sbp < 130:
                points += 0
            elif sbp < 140:
                points += 1
            elif sbp < 160:
                points += 1
            else:
                points += 2

        if points < 0:
            print("<1")
        elif points < 5:
            print("1")
        elif points < 7:
            print("2")
        elif points < 8:
            print("3")
        elif points < 9:
            print("4")
        elif points < 10:
            print("5")
        elif points < 11:
            print("6")
        elif points < 12:
            print("8")
        elif points < 13:
            print("10")
        elif points < 14:
            print("12")
        elif points < 15:
            print("16")
        elif points < 16:
            print("20")
        elif points < 17:
            print("25")
        else:
            print(">30")

with open("lab 5/david/tyr_test_cases.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

    for i, line in enumerate(lines, start=1):
        parts = line.split(" ")
        sex = parts[0].split(":")[-1]
        age = int(parts[1].split(":")[-1])
        cho = int(parts[2].split(":")[-1])
        smo = parts[3].split(":")[-1]
        hdl = int(parts[4].split(":")[-1])
        sbp = int(parts[5].split(":")[-1])
        med = parts[6].split(":")[-1]

        print(i, end=". ")
        print_risk(sex, age, cho, smo, hdl, sbp, med)
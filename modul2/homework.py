# 20P
# 1) Prove "and" operation takes precedence over "or" operation by setting
# parentheses in the following expression (False or False and True or True)

#01: True and (True or False) = True and True or True and False = True or True = True
#02: False and (True or False) = False and True or False and False = False or False = False
#03: True or (True and False) = True or False = True
#04: True or (True or False) = True or True = True
#05: False or (True and False) = False or False = False
#06: False or (True or False) = False or True = True
print(True and (True or True))
print(True and (True or False))
print(True and (False or True))
print(True and (False or False))
print(True and (True and True))
print(True and (True and False))
print(True and (False and True))
print(True and (False and False))
print(True or (True or True))
print(True or (True or False))
print(True or (False or True))
print(True or (False or False))
print(True or (True and True))
print(True or (True and False))
print(True or (False and True))
print(True or (False and False))


print(False and (True or True))
print(False and (True or False))
print(False and (False or True))
print(False and (False or False))
print(False and (True and True))
print(False and (True and False))
print(False and (False and True))
print(False and (False and False))
print(False or (True or True))
print(False or (True or False))
print(False or (False or True))
print(False or (False or False))
print(False or (True and True))
print(False or (True and False))
print(False or (False and True))
print(False or (False and False))




# 40P
# 2) Get from input two different times in the format dd:hh:mm:ss and print
# the difference in seconds between them. The convert the result back to the initial
# format and print that also
# dd is number of days
# hh is number of hours (00-23)
# mm is number od minutes (00-59)
# ss is number of seconds (00-59)

input1 = input("Introduceti input1: ")
input2 = input("Introduceti input2: ")
day1 = int(input1[0:2])
hour1 = int(input1[3:5])
minute1 = int(input1[6:8])
second1 = int(input1[9:])
day2 = int(input2[0:2])
hour2 = int(input2[3:5])
minute2 = int(input2[6:8])
second2 = int(input2[9:])
if ((hour1 > 23) or (hour1 < 0)) or ((hour2 > 23) or (hour2 < 0)) or ((minute1 > 59) or (minute1 < 0)) or ((minute2 > 59) or (minute2 < 0)) or ((second1 > 59) or (second1 < 0)) or ((second2 > 59) or (second2 < 0)):
    print("Nu ati respectat cerinta din enunt")
else:
    minute1_sec = minute1 * 60
    minute2_sec = minute2 * 60
    hour1_sec = hour1 * 60 * 60
    hour2_sec = hour2 * 60 * 60
    day1_sec = day1 * 24 * 60 * 60
    day2_sec = day2 * 24 * 60 * 60
    input1_sec = day1_sec + hour1_sec + minute1_sec + second1
    input2_sec = day2_sec + hour2_sec + minute2_sec + second2
    diff_sec = input2_sec - input1_sec
    print(diff_sec)
    if diff_sec < 0:
        print("nu se poate calcula diferenta")
    else:
        return_day = diff_sec // (24 * 60 * 60)
        print("Zile diferenta: ", return_day)
        remaining_seconds01 = diff_sec - (24 * 60 * 60) * return_day
        print(remaining_seconds01)
        return_hour = remaining_seconds01 // (60 * 60)
        print("Ore diferenta: ", return_hour)
        remaining_seconds02 = remaining_seconds01 - (60 * 60) * return_hour
        print(remaining_seconds02)
        return_minutes = remaining_seconds02 // 60
        print("Minute diferenta: ", return_minutes)
        remaining_seconds03 = remaining_seconds02 - (60 * return_minutes)
        print("Secunde diferenta: ", remaining_seconds03)
        if remaining_seconds03<10:
            if return_minutes<10:
                if return_hour<10:
                    if return_day<10:
                        print(f"0{return_day}:0{return_hour}:0{return_minutes}:0{remaining_seconds03}")
                    else:
                        print(f"{return_day}:0{return_hour}:0{return_minutes}:0{remaining_seconds03}")
                else:
                    if return_day<10:
                        print(f"0{return_day}:{return_hour}:0{return_minutes}:0{remaining_seconds03}")
                    else:
                        print(f"{return_day}:{return_hour}:0{return_minutes}:0{remaining_seconds03}")
            else:
                if return_hour<10:
                    if return_day<10:
                        print(f"0{return_day}:0{return_hour}:{return_minutes}:0{remaining_seconds03}")
                    else:
                        print(f"{return_day}:0{return_hour}:{return_minutes}:0{remaining_seconds03}")
                else:
                    if return_day<10:
                        print(f"0{return_day}:{return_hour}:{return_minutes}:0{remaining_seconds03}")
                    else:
                        print(f"{return_day}:{return_hour}:{return_minutes}:0{remaining_seconds03}")
        else:
            if return_minutes<10:
                if return_hour<10:
                    if return_day<10:
                        print(f"0{return_day}:0{return_hour}:0{return_minutes}:{remaining_seconds03}")
                    else:
                        print(f"{return_day}:0{return_hour}:0{return_minutes}:{remaining_seconds03}")
                else:
                    if return_day<10:
                        print(f"0{return_day}:{return_hour}:0{return_minutes}:{remaining_seconds03}")
                    else:
                        print(f"{return_day}:{return_hour}:0{return_minutes}:{remaining_seconds03}")
            else:
                if return_hour<10:
                    if return_day<10:
                        print(f"0{return_day}:0{return_hour}:{return_minutes}:{remaining_seconds03}")
                    else:
                        print(f"{return_day}:0{return_hour}:{return_minutes}:{remaining_seconds03}")
                else:
                    if return_day<10:
                        print(f"0{return_day}:{return_hour}:{return_minutes}:{remaining_seconds03}")
                    else:
                        print(f"{return_day}:{return_hour}:{return_minutes}:{remaining_seconds03}")

# 40P
# Calculate the diagonal of a rectangle with sides 10 and 15
a = 10
b = 15
print("The diagonal of a rectangle with sides 10 and 15 is: ", (a**2 + b**2)**0.5)




score = float(input("Input your score: "))
way = input("Input letter(L) or PF(PF): ")

if  way == 'Letter':
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
       grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print("Your grade is {}".format(grade))

elif way == 'PF':
    if score >= 90:
        print("PD(Pass with Distinction)")
    elif score >= 60:
        print("Pass")
    else:
        print("Fail")
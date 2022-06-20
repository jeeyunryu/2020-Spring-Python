n1 = int(input("숫자 1: "))
n2 = int(input("숫자 2: "))
n3 = int(input("숫자 3: "))
n4 = int(input("숫자 4: "))
n5 = int(input("숫자 5: "))
n6 = int(input("숫자 6: "))
n7 = int(input("숫자 7: "))

if n1 == n2 == n3 == n4 == n5 == n6 == n7:
    print("동일한 수")

else:
    if n1 > n2:
        max = n1
        max2 = n2
    else:
        max = n2
        max2 = n1
    if max > n3:
        if max2 > n3:
            max2 = max2
        else:
            max2 = n3
    else:
        max2 = max
        max = n3
    if max > n4:
        if max2 > n4:
            max2 = max2
        else:
            max2 = n4
    else:
        max2 = max
        max = n4
    if max > n5:
        if max2 > n5:
            max2 = max2
        else:
            max2 = n5
    else:
        max2 = max
        max = n5
    if max > n6:
        if max2 > n6:
            max2 = max2
        else:
            max2 = n6
    else:
        max2 = max
        max = n6
    if max > n7:
        if max2 > n7:
            max2 = max2
        else: 
            max2 = n7
    else:
        max2 = max
        max = n7

    print("두번째로 큰 수는", max2, "입니다.")

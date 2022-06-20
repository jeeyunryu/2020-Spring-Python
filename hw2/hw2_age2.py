year = int(input('출생년도를 입력하시오: '))
month = int(input('태어난 달을 입력하시오: '))
if (month <= 3) :
    age = 2020 - year + 1
if (not(month <= 3)) :
    age = 2020 - year

print(age, '세')
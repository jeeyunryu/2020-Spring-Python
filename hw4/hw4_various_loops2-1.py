sum = 0
for num in range(1000):
    if num%2 == 0:
        sum = sum + num

print("1과 1000사이의 모든 짝수의 합계는 {:d}입니다." .format(sum))
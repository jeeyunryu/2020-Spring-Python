n = int(input("정수를 입력하시오: "))
total=0

while n>0:
    total=total+(n%10)
    n = n//10

print("결과는 {}입니다.".format(total))
n1 = int(input("첫번째 정수를 입력하세요: "))
n2 = int(input("두번째 정수를 입력하세요: "))
sum = n1

for i in range(n2):
    print(sum, end=' ') 
    sum = n1 + 2**(i+1)
    if i<n2-1:
        print(",", end=' ')
    else: 
        print(" ")
i = int(input("정수를 입력 하시오: "))
product = 1

if i>0:
    print("결과는")
    for j in range(i):
        j = j+1
        product = product*j
        print("{}! = {}".format(j, product), end='')
        if j==i:
            print("\n")
        else:
            print(", ", end='')

  
else:
    print("양의 정수가 아니기 떄문에 계산 할 수 없습니다.")

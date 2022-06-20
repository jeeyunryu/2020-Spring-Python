n = 0
while n<2 or n>15:
    n = int(input("출력 할 단 수를 입력하시오: "))
    if n<2 or n>15:
         print("2~15 값 중 정수를 입력하세요. {}은 처리할 수 없습니다!".format(n))

for i in range(2, n+1):
    for j in range(1, 10):
        print("{}*{}={}".format(i, j, i*j))
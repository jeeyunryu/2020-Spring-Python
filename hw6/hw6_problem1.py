n = []
for i in range(10):
    n.append(int(input("{}번째 수를 입력하시오: ".format(i+1))))
print("정렬 전: [", end='')
for i in range(10):
    if i <9:
        print("{},".format(n[i]), end=' ')
    else: 
        print("{}".format(n[i]), end='')
print("]")

for i in range(10):
    for j in range(9-i):
        if n[j]>n[j+1]:
            t = n[j]
            n[j] = n[j+1]
            n[j+1] = t
print("정렬 후: {}".format(n))
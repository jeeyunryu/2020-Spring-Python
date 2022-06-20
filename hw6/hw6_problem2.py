n = []


for i in range(30):
    n.append(int(input("{}번째 수를 입력하시오: ".format(i+1))))
print("[", end='')
for i in range(30):
    if i <29:
        print("{},".format(n[i]), end=' ')
    else: 
        print("{}".format(n[i]), end='')
print("]")

print("가장 많이 반복된 수와 빈도수: ", end='')

m_count=0
for i in range(30):
    count = 0
    for j in range(i,30):
        if n[i]==n[j]:
            count = count +1
            if count > m_count:
                m_count = count
                rn = []
                rn.append(n[i])
            elif count == m_count:
                rn.append(n[i])
for i in range(len(rn)):
    j = len(rn)-1
    if rn[i]==rn[j]:
        print("{}, {}회".format(rn[i], m_count), end=' ')
    else: 
        print("{}, {}회,".format(rn[i], m_count), end=' ')
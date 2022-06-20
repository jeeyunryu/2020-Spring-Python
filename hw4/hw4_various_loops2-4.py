fst = int(input("첫번쨰 정수를 입력하시오: "))
snd = int(input("두번째 정수를 입력하시오: "))
sum = 0
j = 0

if fst < snd:
    n1 = fst
    n2 = snd
else:
    n1 = snd
    n2 = fst

for i in range(n1+1, n2):
    if i%2 == 1:
        sum = sum + i
        j = j + 1
print(sum/j)

    
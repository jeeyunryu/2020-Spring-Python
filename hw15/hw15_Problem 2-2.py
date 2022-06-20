infile = open('sample.txt','r')

list = infile.readlines()
list2 = []

for i in list:
    list2.append(i[4:-1])


alphabet = []
for i in list2:
    if i[0] not in alphabet:
        alphabet.append(i[0])
alphabet.sort()


count = []
for i in range(len(alphabet)):
    num = 0
    for j in list2:
        if alphabet[i] == j[0]:
            num = num + 1
    count.append(num)


CountName = dict(zip(alphabet, count))
print(CountName)
infile.close()


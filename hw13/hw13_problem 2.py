list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def crypt(str):
    list2 = []
    for i in range(len(str)):
        if str[i].isupper():
            ls = str[i].lower()

            for j in range(26):
                if ls == list[j]:
                    if j!=1 and j%2 == 0:
                        ls = list[j+1]
                        list2.append(ls.upper())
                    else:
       
                        ls = list[j-1]
                        list2.append(ls.upper())
                    break
        elif str[i].islower():
            ls = str[i]
            for j in range(26):
                if ls == list[j]:
                    if j!=1 and j%2 == 0:
                        ls = list[j+1]
                        list2.append(ls)
                    else:
                        ls = list[j-1]
                        list2.append(ls)
                    break
        elif str[i] == ' ':
            list2.append(' ')
    print(''.join(list2))

def decrypt(str):
    list3 = []
    for i in range(len(str)):
        if str[i].isupper():
            ls = str[i].lower()
            for j in range(26):
                if ls == list[j]:
                    if j!=1 and j%2 == 0:
                        ls = list[j+1]
                        list3.append(ls.upper())
                    else:
                        ls = list[j-1]
                        list3.append(ls.upper())
                    break
        elif str[i].islower():
            ls = str[i]
            for j in range(26):
                if ls == list[j]:
                    if j!=1 and j%2 == 0:
                        ls = list[j+1]
                        list3.append(ls)
                    else:
                        ls = list[j-1]
                        list3.append(ls)
                    break
        elif str[i] == ' ':
            list3.append(' ')
    print(''.join(list3))
crypt('Abc')
decrypt('Bad')
crypt('Zoo Park')
decrypt('Ypp Obql')

                    
           


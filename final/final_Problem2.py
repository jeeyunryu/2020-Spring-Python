d = {2:('A', 'B', 'C'), 3:('D', 'E', 'F'), 4:('G', 'H', 'I'), 5:('J', 'K', 'L'), 6:('M', 'N', 'O'), 7:('P', 'Q', 'R', 'S'), 8:('T', 'U', 'V'), 9:('W', 'X', 'Y', 'Z')}

ten = False

while ten == False:
    string = input('10자리 문자열을 입력하시오: ')
    if len(string) != 10:
        print('10개로 구성된 문자열이 아니다')
    else:
        break

string.upper()
list = []

for i in range(len(string)):
    for key in d.keys():
        if string[i] in d[key]:
            list.append(key)

list.insert(3, '-')
list.insert(7, '-')

for i in range(len(list)):
        print('{}'.format(list[i]), end='')
   

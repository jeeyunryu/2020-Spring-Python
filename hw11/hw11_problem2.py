import random
comp_list=random.sample(range(0, 10), 4)
print(comp_list)
count=0
strike=0

def check_list(listname, input_num):
    if input_num not in listname:
        listname.append(input_num)
    return listname

while strike != 4:
    list = []

    while len(list) < 4:
        input_num = int(input('Input a number: '))
        if input_num < 0 or input_num > 9:
            print('Please input a number from 0 to 9')
        else:
            check_list(list, input_num)

    strike = 0
    ball=0
    for i in range(0, 4):
        if comp_list[i] == list[i]:
            strike = strike + 1
        if list[i] in comp_list:
            ball=ball+1
    print('{}-strike, {}-ball'.format(strike, ball-strike))

    count=count+1


if count==1:
    print('You win! {}st try..'.format(count))
elif count==2:
    print('You win! {}nd try..'.format(count))
elif count==3:
    print('You win! {}rd try..'.format(count))
else:
    print('You win! {}th try..'.format(count))





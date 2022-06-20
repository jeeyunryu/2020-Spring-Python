list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


import random
list1 = []
list2 = []
list1 = random.sample(list, 10)
list2 = random.sample(list, 10)



def bubble(listname):
    for i in range(len(listname)):
        for j in range(len(listname)-1):
            if listname[j] > listname[j+1]:
                temp = listname[j]
                listname[j] = listname[j+1]
                listname[j+1] = temp
    return listname
print('list1= {}'.format(bubble(list1)))
print('list2 = {}'.format(bubble(list2)))

def merge(list1, list2):
    count = 0
 
    for i in range(10):
        for j in range(10):
            if list1[i] == list2[j]:
                count=count+1
    result=[]
    list1.sort()
    list2.sort()
    i = 0
    j = 0
    while i<10 and j <10:
        if list1[i] > list2[j]:
            result.append(list2[j])
            j = j + 1
        elif list2[j] > list1[i]:
            result.append(list1[i])
            i = i + 1
        else:
            result.append(list1[i])
            i = i + 1
            j = j + 1
                
    

    return result, count
        
print(merge(list1, list2))

testlist1 = [1, 2, 3, 4, 5]
testlist2 = [6, 7, 8]
index1=[]
index2=[]
newlist=[]
list1=[]
list2=[]
num=0
test1=[]
test2=[]
duplicate=False
for i in range(len(testlist1)):
    for j in range(len(testlist2)):
        if testlist1[i]==testlist2[j]:
           if testlist1[i]!=num:
               duplicate=True
    
if duplicate==False:
    print("no duplicate elements")
    print("List1= {}".format(testlist1))
    print("List2= {}".format(testlist2))
elif duplicate:
    print("양쪽 모두 존재하는 값: ", end='')
    for i in range(len(testlist1)):
        for j in range(len(testlist2)):
            if testlist1[i]==testlist2[j]:
                if testlist1[i]!=num:
                    num=testlist1[i] 
                    newlist.append(num)
    newlist.sort()

    for i in newlist:
        if newlist.index(i) !=(len(newlist)-1):
            print("{}, ".format(i), end='')
        else:
            print("{}".format(i), end='')

    for i in range(len(newlist)):
        for j in range(len(testlist1)):
            if newlist[i]==testlist1[j]:
                index1.append(j)
                index1.sort()

    for i in range(len(newlist)):
        for j in range(len(testlist2)):
            if newlist[i]==testlist2[j]:
                index2.append(j)
                index2.sort()

    print("\nIndex 값: {}, {}".format(index1, index2))

    for i in range(len(testlist1)):
        exist = False
        for j in range(len(newlist)):
            if newlist[j]==testlist1[i]:
                exist = True
                break
        if not exist:
            test1.append(testlist1[i])
    print("List1: {}".format(test1))

    for i in range(len(testlist2)):
        exist =False
        for j in range(len(newlist)):
            if newlist[j]==testlist2[i]:
                exist=True
                break
        if not exist:
            test2.append(testlist2[i])
    print("List2: {}".format(test2))


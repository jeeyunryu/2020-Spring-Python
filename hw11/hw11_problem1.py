def mergeSort(l1, l2):
    l1.sort()
    l2.sort()
    list=[]

    i=0
    j=0
    while i != len(l1) and j != len(l2):
        if l1[i] < l2[j]:
            list.append(l1[i])
            i = i + 1
        elif l1[i] > l2[j]:
            list.append(l2[j])
            j = j + 1
        elif l1[i] == l2[j]:
            list.append(l1[i])
            i = i + 1
            j = j + 1
    
    return list


list1=[2, 5, 5, 11, 19]
list2=[3, 3, 5, 7, 13, 17, 17, 23]
print(mergeSort(list1, list2))


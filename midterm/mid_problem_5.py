sam1=[1, 53, 19, 5, 21, -12, -3, 32, 11, 25]
sam2=[1, 5, 10, 12, -3, 23, 19, 20, 55]

for i in range(len(sam1)):
    for j in range(len(sam2)):
        if sam1[i]==sam2[j]:
            sam2.pop(j)

sam=sam1+sam2


def bubble_S(listname):
    for i in range(len(listname)-1):
        for j in range(i+1, len(listname)):
            if listname[i]>listname[j]:
                temp=listname[i]
                listname[i]=listname[j]
                listname[j]=temp
    print(listname)


bubble_S(sam)

def facto(num):
    
    list=[]
    for i in range(1, num+1):
        mul=1
        for j in range(1, i+1):
            mul=mul*j
        list.append(mul)
    print(list)
            
facto(10)
facto(17)

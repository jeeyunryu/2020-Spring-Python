chem=input('화학식을 입력하시오: ')
list=[]

for i in range(len(chem)):
    a=0
    if chem[i].isalpha():
        if chem[i+1].isdigit():
            s=chem[i]
            if s=='O':
                a=15.9994
            if s=='S':
                a=32.066
            if s=='C':
                a=12.011
            if s=='H':
                a=1.00794
            if s=='N':
                a=14.00674
            product=a*float(chem[i+1])
            list.append(product)
            
        else:
            s=chem[i]
            if s=='O':
                a=15.9994
            if s=='S':
                a=32.066
            if s=='C':
                a=12.011
            if s=='H':
                a=1.00794
            if s=='N':
                a=14.00674
            product=a
            list.append(product)
print(list)

sum=0
for i in list:
    sum=sum+i


print("{} 분자량은 {}".format(chem, sum))

list=[]
otherlist=[]
length=len(list)-1
index=[]

max=0
sum=0

for i in range(10):
    list.append(int(input("{}번째 수를 입력하시오: ".format(i+1))))  
print("\n리스트: ", list)

otherlist.append(list[length])
list.pop(length)
list=otherlist+list
print("오른쪽으로 한 칸씩 이동: {}".format(list))

list.pop(4)
list.pop(4)
print("중간에 위치한 2개의 element 제거: {} ".format(list))

for i in range(len(list)):
    if list[i]>max:
        max=list[i]
print("전체 element 중 가장 큰 수: {} ".format(max))

duplicated=False
for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i]==list[j]:
            duplicated=True
    if duplicated:
        print("중복 여부 체크: exist duplicate elements")
        break
if duplicated==False:
        print("중복 여부 체크: no duplicate elements", end='')
         
if duplicated: 
    print("중복되는 Index: ", end='')
    for i in range(len(list)):
        index=[]
        for j in range(i+1, len(list)):
            if list[i]==list[j]: 
                index.append(i)
                index.append(j)
        if len(index)>1:
            print(index, end='')
             

for i in list:
    sum=sum+i
n=sum/len(list)
print("\n저장된 값들의 합계, 평균: {}, {}".format(sum, n))



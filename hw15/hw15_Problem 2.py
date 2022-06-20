infile = open('sample.txt', 'r')
outfile = open('result_sample1.txt', 'w')

list = infile.readlines()

list2 = []

for i in list:
    list2.append(i[:-1])
    


    
for i in range(len(list2)):
    count = 0
    upper = 0
    lower = 0
    for j in range(len(list2[i])):
        if list2[i][j].isalpha():
            count = count + 1
            if list2[i][j].isupper():
                upper = upper + 1
            else:
                lower = lower + 1
    outfile.write(list2[i])
    outfile.write('{}, {}, {}\n'.format(count, upper, lower))
                
                
    
                





infile.close()
outfile.close()

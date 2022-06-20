def CountFile(filename):
    try:
        infile = open(filename, 'r')

        count = 0
        cwos = 0
        cws = 0
        countlines = 0

        list = infile.readlines()
        countlines = int((len(list)+1)/2)

        for i in range(len(list)):
            lst2 = []
            list2 = list[i].split()
            count = count + len(list2)

        for i in range(len(list)):
           cwos = cwos + len( list[i].replace(' ', ''))
        cwos = cwos - len(list)

        for i in range(len(list)):
            cws = cws + len(list[i])
        cws =cws - len(list)
         
        print('단어 수: {}'.format(count))
        print('문자 수(공백제외): {}'. format(cwos))
        print('문자 수(공백포함): {}'.format(cws))
        print('줄 수: {}'.format(countlines))

        infile.close()

    except IOError:
        print('Error: can\'t find file or read data')
    
CountFile('poem2.txt')
    

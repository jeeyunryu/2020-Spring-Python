def countVowels(string):
    count=0
    for i in range(len(string)):
        s=string[i]
        if s=='a' or s=='A' or s=='e' or s=='E' or s=='i' or s=='I' or s=='o' or s=='O' or s=='u' or s=='U':
            count=count+1
    print('모음의 총 개수: {}'.format(count))

countVowels("she sElls seashells by thE seashore")
countVowels("I am Groot!")

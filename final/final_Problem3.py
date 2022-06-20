# 소수 확인하기

def isprime(num):

    prime=True

    for i in range(2,num):

        if num%i==0:

            prime=False

            break
    if prime:
        print('소수입니다')
    else:
        print('소수가 아닙니다')

# def what( s1, s2):

# s1, s2는 문자열 s2는 한 글자 문자열로

#지정하여, s1에 s2가 존재하면 그 위치를

#모두 리스트로 만들어서 출력

def what(s1,s2):

    n=[]

    for i in range (len(s1)):

        if s1[i]==s2:

            n.append(i)

    if len(n) != 0:
        print(n)
    else:
        print ('[-1]')


# def fact(n):

# 재귀함수로 코딩, 1!, 2!, 3!, ……..n! 값을

# 리스트로 만들어서 return 한다

def fact(n):
    list = []

    if n == 1:

        list = [1]

    else :

        factorial = fact(n-1)

        product  = n * list[-1]

        list.append(product)

        return list

print(fact(5))

#‘poem.txt’ 파일을 읽어서, 각 단어로 구성

#된 리스트를 생성하고 각 줄마다 몇 개의

#단어로 구성되었는지 확인한다. 

#“numofWord.txt” 에 단어 개수를 저장한 #후 출력하시오.

P = open('poem.txt')

N = open('numofWord.txt', 'a')

P1 = P.readlines()
print(P1)

for p in range(len(P1)):

    P2 = P1[p].split(' ')

    N.write(str(len(P2)))

    N.write('\n')

N.close()
P.close()

# 암호화, 복호화 문제

def code(word):

    diction = {\'A\' : \'M\', \'a\' : \'m\', \'B\' : \'N\', \'b\' : \'n\', \'C\' : \'O\', \'c\' : \'o\', \'D\' : \'V\', \'d\' : \'v\', \'E\' : \'W\', \'e\' : \'w\', \'F\' : \'X\', \'f\' : \'x\', \'G\' : \'P\', \'g\' : \'p\', \'H\' : \'Q\', \'h\' : \'q\', \'I\' : \'R\', \'i\' : \'r\', \'J\' : \'S\', \'j\' : \'s\', \'K\' : \'T\', \'k\' : \'t\', \'L\' : \'U\', \'l\' : \'u\', \'M\' : \'A\', \'m\' : \'a\', \'N\' : \'B\', \'n\' : \'b\', \'O\' : \'C\', \'o\' : \'c\', \'P\' : \'G\', \'p\' : \'g\', \'Q\' : \'H\', \'q\' : \'h\', \'R\' : \'I\', \'r\' : \'i\', \'S\' : \'D\', \'s\' : \'d\', \'T\' : \'E\', \'t\' : \'e\', \'U\' : \'F\', \'u\' : \'f\', \'V\' : \'L\', \'v\' : \'l\', \'W\' : \'Y\', \'w\' : \'y\', \'X\' : \'Z\', \'x\' : \'z\', \'Y\' : \'J\', \'y\' : \'j\', \'Z\' : \'K\', \'z\' : \'k\'}

    code=""

    for alpha in word:
        for key in diction.keys()
            if alpha in diction[key]:
                code = code + diction[key]
    return code


word=input("문자열을 입력하세요:")

word2 = code(word)

if word == code(word2):

    print (\'"\',word,\'"은"\',codeB(word2),\'" 동일하다!!\')

else:

    print ("암호화가 제대로 되지 않음.")



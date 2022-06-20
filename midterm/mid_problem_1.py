def prime(n):
    list=[]

    if n<=1 or n<0:
        print('처리할 수 없습니다.')
        return()

    prime_number=True

    for i in range(2, n):
        if n%i==0:
            prime_number=False
            break
    if prime_number:
        print('소수입니다')

    else:
        for i in range(1, n+1):
            if n%i==0:
                list.append(i)
        print(list)

prime(3)
prime(8)
prime(-2)

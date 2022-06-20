def numDigit(n):
    import math
    integer = len(str(math.trunc(n)))
    decimal = len(str(n)) - integer -1

    print('정수 자리 수 {}, 소수 자리 수 {}'.format(integer, decimal))
   
    
    

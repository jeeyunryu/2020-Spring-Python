def middle(string):
    if len(string)%2==0:
        print(string[len(string)//2-1], end='')
        print(string[len(string)//2])
    else:
        print(string[(len(string)+1)//2])


middle('middle')
middle('miDdle')
        

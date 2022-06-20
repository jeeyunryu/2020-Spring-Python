str=input()

if str[len(str)-1]=='y':
    str=str[:-1]
    str=str+'ies'
    print(str)

elif str[len(str)-1]=='f':
    str=str[:-1]
    str=str+'ves'
    print(str)

elif str[len(str)-1]=='s'or str[len(str)-1]=='ch'or str[len(str)-1]=='sh':
    str=str+'es'
    print(str)

else:
    str=str+'s'
    print(str)
    



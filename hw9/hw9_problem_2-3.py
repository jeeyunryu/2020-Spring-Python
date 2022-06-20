def reverse(string):
    for i in range(1, len(string)+1):
        s=string[len(string)-i]
        if i==len(string):
            print(s)
        else:
            print(s, end='')


reverse('hello')
reverse('Python')

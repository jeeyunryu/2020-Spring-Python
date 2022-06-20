def vowelchar(str):
    for i in range(len(str)):
        if str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u':
            print(str[i], end='')

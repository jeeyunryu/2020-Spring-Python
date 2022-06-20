def sorted(a, b, c, d):
    sorted = True
    if a > b:
        if b > c:
            if c > d:
                sorted = True
            else:
                sorted = False
        else:
            sorted = False
    else:
        if b < c:
            if c < d:
                sorted = True
            else:
                sorted = False
        else:
            sorted = False


    if sorted:
        print('True')
    else:
        print('False')

def Ispal(string1):
    backward = True
    string1 = string1.lower()
    
    delimiter = ' '
    string1 = string1.split(delimiter)
    string1 = string1.join()
    
    for i in range(len(string1)/2):
        if string1[i] != string1[len(string1)-1-i]:
            backward = False

    
    if backward:
        return True
    else: 
        return False
    
    
Ispal(input())

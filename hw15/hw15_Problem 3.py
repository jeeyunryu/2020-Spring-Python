from tkinter import *
root = Tk()
string = StringVar()


txt = Entry(root, textvariable=string)
txt.pack()

def click():
    text = string.get()
    text = text.lower()
        

    list = []
    for i in range(len(text)):
        if text[i].isalpha():
            list.append(text[i])
    text2 = ''.join(list)
        
            
    list2 = []
    for i in range(len(list)):
        list2.append(list[len(list)-i-1])
    text3 = ''.join(list2)
   

    
    if text2 != text3:
        backword = False
    else:
        backword = True
    
    if backword == True:
        lbl = Label(root, text='TRUE')
        lbl.pack()
    elif backword == False:
        lbl2 = Label(root, text='FALSE')
        lbl2.pack()
    
    
btn = Button(root, text='BUTTON', command=click)
btn.pack()





from tkinter import *
root = Tk()

label = Label(root, text='키')
label.pack()

entry = Entry(root)
entry.pack()

label2 = Label(root, text='몸무게')
label2.pack()

entry2 = Entry(root)
entry2.pack()

def bmi():
    height = int(entry.get()) * 0.01
    weight = int(entry2.get())

    bmi = weight / (height * height)

    if bmi < 25:
        label4 = Label(root, text='정상')
        label4.pack()
    elif bmi < 30:
        label4 = Label(root, text='과체중')
        label4.pack()
    elif bmi < 40:
        label4 = Label(root, text='비만')
        label4.pack()
    else:
        label4 = Label(root, text='고도비만')
        label4.pack()
        
button = Button(root, text='calculate', command=bmi)
button.pack()

root.mainloop()

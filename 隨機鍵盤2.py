from tkinter import *
import random
from tkinter import messagebox

L = []
def count(btn):
    global L
    a = btn['text']
    
    if a == 'C':
        L = []
    
    elif a == 'OK':
        if L == [1, 2, 3, 4]:
            messagebox.showinfo('恭喜你', "密碼正確")
        else:
            L = []
            messagebox.showinfo('超可悲', "密碼錯誤")
    
    else:
        L.append(a)
    
    num.set(L)


if __name__ == '__main__':
    root = Tk()
    root.title("Tic Tac Toe")
    root.geometry("300x500+200+100")
    num  = StringVar()
    num.set(0)
    
    lab1 = Label(root, text="", 
                    font=("Arial", 20),
                    width=18, height=2,
                    bg='#fff',
                    relief=SUNKEN,
                    textvariable=num,
                    justify=RIGHT, anchor=E)
    lab1.grid(row=0, column=0, columnspan=4, sticky=NSEW,  padx=6, pady=4)
    
    btn_labs = random.sample(range(0, 10), 10)
    btn_labs.insert(9, 'C')
    btn_labs.insert(11, 'OK')
    
    btns = []
    
    for i in range(4):
        for j in range(3):
            btns.append(Button(root, text=btn_labs[i*3+j],
                                    width=3, height=2,
                                    font=("Arial, 20")))
            
            btns[-1].config(command=lambda btn=btns[-1]: count(btn))
            btns[-1].grid(row=i+1, column=j, sticky=NSEW, padx=18, pady=14)
    
    root.mainloop()
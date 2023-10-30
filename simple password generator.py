from tkinter import *
import random
window=Tk()
window.configure(bg='powder blue')
window.title("Password generator")
def create():
    max_len=12
    digits=['0','1','2','3','4','5','6','7','8','9']
    lowercase=['a','b','c','d','e','f','g','h','i','j','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    uppercase=['A','B','C','D','E','F','G','H','I','J','K','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    splchar=['@','#','$','%','=',':','?','.','/','|','~','>','*','(',')','<']
    combined=digits+lowercase+uppercase
    rdigit=random.choice(digits)
    rlc=random.choice(lowercase)
    ruc=random.choice(uppercase)
    rspcl=random.choice(splchar)
    temp=rdigit+rlc+ruc+rspcl
    for i in range(max_len-4):
        temp=temp+random.choice(combined)
    password=''
    for i in temp:
        password=password+i
    e.insert(0,password)
def clear():
    e.delete(0,END)
e=Entry(window,width=30,font=("arial",16),justify=RIGHT)
e.pack()
b=Button(window,text="Generate",width=20,height=2,command=create)
b.pack()
clr=Button(window,text="Clear",width=20,height=2,command=clear)
clr.pack()
window.geometry("300x150") 
window.mainloop()

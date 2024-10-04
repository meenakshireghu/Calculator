from tkinter import *
root =Tk()

root.title("Calculator")
root.geometry("400x400") 


scvalue = StringVar()#intialization
scvalue.set("")#setting intial value of scvalue as an empty string
screen = Entry(root, textvar=scvalue,font="arial 40 bold")
screen.pack(fill=X,ipadx=10,ipady=10,padx=10,pady=10)

def click(event):
    global scvalue
    text= event.widget.cget("text")
    
    if text=="=":
        if scvalue.get().isdigit():#checks whether the cureent value consists of only digits
            value=int(scvalue.get())#converts into int
        else:
            try:
                value=eval(screen.get())#evalutes the experssion
            except Exception as e:
                print(e)
                value="Error"
                          
        scvalue.set(value) #updates the screen with the calculated value or error
        screen.update() # refresh the screen to reflect the updated value
        
    elif text=="AC":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
    
          
    
f=Frame(root,bg="grey")
b=Button(f,text="(",padx=10,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text=")",padx=10,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)


b=Button(f,text="%",padx=10,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)


b=Button(f,text="AC",padx=10,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)
f.pack()


f=Frame(root,bg="grey")
b=Button(f,text="7",padx=10,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)


b=Button(f,text="8",padx=10,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)


b=Button(f,text="9",padx=10,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)


b=Button(f,text="/",padx=10,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)
f.pack()


f=Frame(root,bg="grey")
b=Button(f,text="4",padx=10,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)


b=Button(f,text="5",padx=10,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)



b=Button(f,text="6",padx=10,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)


b=Button(f,text="*",padx=10,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
f.pack()


f=Frame(root,bg="grey")
b=Button(f,text="1",padx=10,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)


b=Button(f,text="2",padx=10,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="3",padx=10,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="-",padx=10,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="0",padx=10,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)


b=Button(f,text=".",padx=10,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)


b=Button(f,text="=",padx=10,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="+",padx=10,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
f.pack()



root.mainloop()
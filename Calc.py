from tkinter import *
import math as m
root = Tk()
root.title("Scientific Calculator")
root.configure(background="light green")
e = Entry(root,width=28,relief=RIDGE, fg="White", bg="Black",font=('Helvetica',30,'bold'),bd=30,justify=RIGHT)
e.grid(row=0,column=0,columnspan=5,padx=5,pady=20) #padx padding along x axis

def click(to_print):
    old = e.get()
    e.delete(0,END)
    e.insert(0,old+to_print)
    return

def sc(event):
    key = event.widget
    text = key['text']
    no = e.get()
    result=''
    if text=='deg':
        result = str(m.degrees(float(no)))

    if text=='sin' :
        result = str(m.sin(float(no)))

    if text=='cos' :
        result = str(m.cos(float(no)))

    if text=='tan' :
        result = str(m.tan(float(no)))

    if text=='lg' :
        result = str(m.log10(float(no)))

    if text=='ln' :
        result = str(m.log(float(no)))

    if text=='sqrt' :
        result = str(m.sqrt(float(no)))

    if text=='x!' :
        result = str(m.factorial(float(no)))

    if text=='1/x' :
        result = str(1/(float(no)))

    if text=='pi' :
        if no=="" :
            result = str(m.pi)
        else :
            result = str(float(no) * m.pi)

    if text=='e' :
        if no=="" :
            result = str(m.e)
        else :
            result = str(m.e ** float(no))

    e.delete(0,END)
    e.insert(0,result)

def clear():
    e.delete(0,END)
    return

def bkspa():
    current = e.get()
    length = len(current)-1  #len is calculating length of string
    e.delete(length,END)

def evaluate():
    ans = e.get()
    ans = eval(ans) # eval function evaluate the expression tha we have entered in the panel
    e.delete(0,END)
    e.insert(0,ans)


lg = Button(root,text="lg",relief=RIDGE,fg="White", bg="Black",width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
lg.bind("<Button-1>",sc)
lg.grid(row=1,column=0)
ln = Button(root,text="ln",relief=RIDGE,fg="White", bg="Black",width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
ln.bind("<Button-1>",sc)
ln.grid(row=1,column=1)
par1 = Button(root,text="(",relief=RIDGE,fg="White", bg="Black",command=lambda:click("("),width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
par1.grid(row=1,column=2)
par2 = Button(root,text=")",relief=RIDGE,fg="White", bg="Black",command=lambda:click(")"),width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
par2.grid(row=1,column=3)
dot = Button(root,text=".",relief=RIDGE,fg="White", bg="Black",command=lambda:click("."),width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
dot.grid(row=1,column=4)


expb = Button(root,text="^",relief=RIDGE,fg="White", bg="Black",width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
expb.grid(row=2,column=0)
degb = Button(root,text="deg",relief=RIDGE,fg="White", bg="Black",width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
degb.bind("<Button-1>",sc)
degb.grid(row=2,column=1)
sinb = Button(root,text="sin",relief=RIDGE,fg="White", bg="Black",width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
sinb.bind("<Button-1>",sc)
sinb.grid(row=2,column=2)
cosb = Button(root,text="cos",relief=RIDGE,fg="White", bg="Black",width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
cosb.bind("<Button-1>",sc)
cosb.grid(row=2,column=3)
tanb = Button(root,text="tan",relief=RIDGE,fg="White", bg="Black",width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
tanb.bind("<Button-1>",sc)
tanb.grid(row=2,column=4)


sqrtb = Button(root,text="sqrt",relief=RIDGE,fg="White", bg="Black",width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
sqrtb.bind("<Button-1>",sc)
sqrtb.grid(row=3,column=0)
clrb = Button(root,text="C",relief=RIDGE,fg="White", bg="Black",command=lambda:clear(),width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
clrb.grid(row=3,column=1) #clrb -> clear
back = Button(root,text="bksp",relief=RIDGE,fg="White", bg="Black",command=lambda:bkspa(),width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
back.grid(row=3,column=2)
modb = Button(root,text="mod",relief=RIDGE,fg="White", bg="Black",width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
modb.bind("<Button-1>",sc)
modb.grid(row=3,column=3)
divideb = Button(root,text="/",relief=RIDGE,fg="White", bg="Black",command=lambda:click("/"),width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
divideb.grid(row=3,column=4)


fact = Button(root,text="x!",relief=RIDGE,fg="White", bg="Black",width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
fact.bind("<Button-1>",sc)
fact.grid(row=4,column=0)
seven = Button(root,text="7",relief=RIDGE,fg="White", bg="Black",command=lambda:click("7"),width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
seven.grid(row=4,column=1)
eight = Button(root,text="8",relief=RIDGE,fg="White", bg="Black",command=lambda:click("8"),width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
eight.grid(row=4,column=2)
nine = Button(root,text="9",relief=RIDGE,fg="White", bg="Black",command=lambda:click("9"),width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
nine.grid(row=4,column=3)
mulb = Button(root,text="*",relief=RIDGE,fg="White", bg="Black",command=lambda:click("*"),width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
mulb.grid(row=4,column=4)


invb = Button(root,text="1/x",relief=RIDGE,fg="White", bg="Black",width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
invb.bind("<Button-1>",sc)
invb.grid(row=5,column=0)
four = Button(root,text="4",relief=RIDGE,fg="White", bg="Black",command=lambda:click("4"),width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
four.grid(row=5,column=1)
five = Button(root,text="5",relief=RIDGE,fg="White", bg="Black",command=lambda:click("5"),width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
five.grid(row=5,column=2)
six = Button(root,text="6",relief=RIDGE,fg="White", bg="Black",command=lambda:click("6"),width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
six.grid(row=5,column=3)
subb = Button(root,text="-",relief=RIDGE,fg="White", bg="Black",command=lambda:click("-"),width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
subb.grid(row=5,column=4)


pib = Button(root,text="pi",relief=RIDGE,fg="White", bg="Black",width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
pib.bind("<Button-1>",sc)
pib.grid(row=6,column=0)
one = Button(root,text="1",relief=RIDGE,fg="White", bg="Black",command=lambda:click("1"),width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
one.grid(row=6,column=1)
two = Button(root,text="2",relief=RIDGE,fg="White", bg="Black",command=lambda:click("2"),width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
two.grid(row=6,column=2)
three = Button(root,text="3",relief=RIDGE,fg="White", bg="Black",command=lambda:click("3"),width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
three.grid(row=6,column=3)
addb = Button(root,text="+",relief=RIDGE,fg="White", bg="Black",command=lambda:click("+"),width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
addb.grid(row=6,column=4)


e_b = Button(root,text="e",relief=RIDGE,fg="White", bg="Black",width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
e_b.bind("<Button-1>",sc)
e_b.grid(row=7,column=1)
zero = Button(root,text="0",relief=RIDGE,fg="White", bg="Black",command=lambda:click("0"),width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
zero.grid(row=7,column=2)
equal = Button(root,text="=",relief=RIDGE,fg="White", bg="Black",command=lambda:evaluate(),width=6,height=1,bd=4,font=('Helvetica',20,'bold'))
equal.grid(row=7,column=3)

"""scientfic buttons : function sc
number and mathematical buttons : function click
equal button : function evaluate
backspace button : bksps function"""
# l=Label(root, text="Title", bg="light green")
# l.pack()
root.mainloop()
import pyttsx3
import tkinter as tk
from tkinter import *
import math
import sys
from time import strftime

def stop():
	 del sys.modules[strftime]
	 
			
def clock():
	
	e=entry_field.get()
	def time():
		string=strftime("%H : %M : %S")
		label.config(text=string)
		label.after(1000, time)
	label=Button(root,bg="black",fg="white",font="arial 10 bold",command=lambda:stop())
	label.place(x=200,y=15)
	time()
		

error="syntax error"
#functionality

	
def ln():
	ln="In"
	entry_field.insert(0,ln)
def exp():
	a=math.e
	entry_field.insert(0,a)
def eqn():
	eqn="1: simultaneous             2: quadratic"
	entry_field.insert(0,eqn)
def pi():
	pi="pi"
	entry_field.insert(0,pi)
def sqrt():
	sqrt="sqrt"
	entry_field.insert(0,sqrt)
def shft():
	s="s"
	entry_field.insert(0,s)
def click(no):
	e=entry_field.get()
	entry_field.delete(0,END)
	entry_field.insert(0,e+no)
def ac():
	entry_field.delete(0,END)
def delete():
	e=entry_field.get()
	e=e[0:len(e)-1]
	entry_field.delete(0,END)
	entry_field.insert(0,e)
def solve():
		try:
			e=entry_field.get()
			e=eval(e)
			entry_field.delete(0,END)
			entry_field.insert(0,e)
		except:
			entry_field.delete(0,END)
			entry_field.insert(0,error)
def deg():
	e=entry_field.get()
	e=math.degrees(eval(e))
	entry_field.delete(0,END)
	entry_field.insert(0,e)
def rad():
	e=entry_field.get()
	e=math.radians(eval(e))
	entry_field.delete(0,END)
	entry_field.insert(0,e)
def log():
	e=entry_field.get()
	if e[:1]=="°":
		log="log^-1"
		entry_field.delete(0,END)
		entry_field.insert(0,log)
	#log="log"
	#entry_field.insert(0,log)
def sin():
	e=entry_field.get()
	if e[:1]=="s":
		sin="(sin^-1)"
		e=e[1:]
		entry_field.delete(0,END)
		entry_field.insert(0,sin+e)
	else:
		sin="sin"
		entry_field.insert(0,sin)
	
def cos():
	cos="cos"
	entry_field.insert(0,cos)
def tan():
	tan="tan"
	entry_field.insert(0,tan)
def equal():
	e=entry_field.get()
	if e[0:3]=="sin":
		e=e[3:]
		e=math.sin(math.radians(eval(e)))
		e=format(e,".15f")
		entry_field.delete(0,END)
		entry_field.insert(0,e)
	elif e[0:3]=="cos":
		e=e[3:]
		e=math.cos(math.radians(eval(e)))
		e=format(e,".15f")
		entry_field.delete(0,END)
		entry_field.insert(0,e)
	elif e[0:3]=="tan":
		e=e[3:]
		e=math.tan(math.radians(eval(e)))
		e=format(e,".15f")
		entry_field.delete(0,END)
		entry_field.insert(0,e)
	elif e[0:3]=="log":
		e=e[3:]
		e=math.log10(eval(e))
		entry_field.delete(0,END)
		entry_field.insert(0,e)
	elif e[0:4]=="sqrt":
		e=e[4:]
		e=math.sqrt(eval(e))
		entry_field.delete(0,END)
		entry_field.insert(0,e)
	elif e[len(e)-1:len(e)]=="%":
		e=e[:len(e)-1]
		e=eval(e)/100
		entry_field.delete(0,END)
		entry_field.insert(0,e)
	elif e[0:8]=="(sin^-1)":
		e=e[8:]
		e=math.degrees(math.sinh(eval(e)))
		#e=round(e)
		entry_field.delete(0,END)
		entry_field.insert(0,e)
	elif e[:6]=="log^-1":
		e=e[6:]
		e=math.logh(e)
		entry_field.delete(0,END)
		entry_field.insert(0,e)
	try:
		if e[:2]=="In":
			e=e[2:]
			e=math.log2(eval(e))
			entry_field.delete(0,END)
			entry_field.insert(0,e)
			return
	except:pass
		
	try:
	  if e[:2]=="pi":
		    e=eval(e[2:])
		    e=math.pi*e
		    entry_field.delete(0,END)
		    entry_field.insert(0,e)
		    return
	except:
		   if e[:2]=="pi":
		   	entry_field.delete(0,END)
		   	a=math.pi
		   	entry_field.insert(0,a)
	try:
		e=entry_field.get()
		e=eval(e)
		entry_field.delete(0,END)
		entry_field.insert(0,e)	
	except:
		entry_field.delete(0,END)
		entry_field.insert(0,error)	
root=Tk()



root.title("calculator")
root.geometry("1280x720+50+80")
root.resizable(True,True)

#entry field
root.config(bg="white")
entry_field=Entry(root,bg="blue",fg="black",bd="0",width="30",font="arial 10 bold",highlightthickness="0")
entry_field.grid(row=0,column=0,pady=0,columnspan=5)
entry_field=Entry(root,bg="blue",fg="black",bd="0",width="30",font="arial 10 bold",highlightthickness="0")
entry_field.grid(row=1,column=0,pady=0,columnspan=5)
#row1
#i=Button(root,bg="blue",fg="white",text="shift",width="4",command=lambda:shft())
#i.grid(row=1,column=0)
#shift=Button(root,bg="maroon",fg="white",text="alpha",width="4")
#shift.grid(row=1,column=1,padx=3)
#shift=Button(root,bg="black",fg="white",text="Eqn",width="4",command=lambda:eqn())
#shift.grid(row=1,column=2)
#shift=Button(root,bg="black",fg="white",text="clock",width="4",command=lambda:clock())
#shift.grid(row=1,column=3)
#shift=Button(root,bg="black",fg="white",text="games",width="4")
#shift.grid(row=1,column=4)


#row2

i=Button(root,bg="green",fg="white",text="solve",width="4",command=lambda: solve())
i.grid(row=2,column=0,pady=10)
shift=Button(root,bg="black",fg="white",text="pi",width="4",command=lambda:pi())
shift.grid(row=2,column=1)
shift=Button(root,bg="black",fg="white",text="deg",width="4",command=lambda: deg())
shift.grid(row=2,column=2)
shift=Button(root,bg="black",fg="white",text="In",width="4",command=lambda:ln())
shift.grid(row=2,column=3)
shift=Button(root,bg="black",fg="white",text="fomuli",width="4")
shift.grid(row=2,column=4)





#row3

shift=Button(root,bg="black",fg="white",text="log",width="4",command=lambda: log())
shift.grid(row=3,column=0)
shift=Button(root,bg="black",fg="white",text="rad",width="4",command=lambda:rad())
shift.grid(row=3,column=1)
shift=Button(root,bg="black",fg="white",text="sin",width="4",command=lambda: sin())
shift.grid(row=3,column=2)
shift=Button(root,bg="black",fg="white",text="cos",width="4",command=lambda:cos())
shift.grid(row=3,column=3)
shift=Button(root,bg="black",fg="white",text="tan",width="4",command=lambda:tan())
shift.grid(row=3,column=4)



#alpha
shift=Label(root,bg="maroon",fg="white",text="a",width="3",font="arial 5 bold")
shift.place(x=150,y=415)
shift=Label(root,bg="maroon",fg="white",text="b",width="3",font="arial 5 bold")
shift.place(x=360,y=415)
shift=Label(root,bg="maroon",fg="white",text="c",width="3",font="arial 5 bold")
shift.place(x=575,y=415)
shift=Label(root,bg="maroon",fg="white",text="d",width="3",font="arial 5 bold")
shift.place(x=790,y=415)


#row4
shift=Button(root,bg="black",fg="white",text="e",width="4",command=lambda:exp())
shift.grid(row=4,column=0,pady=10)
shift=Button(root,bg="black",fg="white",text="sqrt",width="4",command=lambda:sqrt())
shift.grid(row=4,column=1)
shift=Button(root,bg="black",fg="white",text="^",width="4",command=lambda:click("**"))
shift.grid(row=4,column=2)
shift=Button(root,bg="black",fg="white",relief="ridge",text="(",width="4",command=lambda:click("("))
shift.grid(row=4,column=3)
shift=Button(root,bg="black",fg="white",text=")",width="4",command=lambda:click(")"))
shift.grid(row=4,column=4)

#row3^-1
shift=Label(root,bg="blue",fg="white",text="logh",width="3",font="arial 5 bold")
shift.place(x=150,y=358)
shift=Label(root,bg="blue",fg="white",text="sinh",width="3",font="arial 5 bold")
shift.place(x=577,y=358)
shift=Label(root,bg="blue",fg="white",text="cosh",width="3",font="arial 5 bold")
shift.place(x=788,y=358)
shift=Label(root,bg="blue",fg="white",text="tanh",width="3",font="arial 5 bold")
shift.place(x=1000,y=358)


#row5
shift=Button(root,bg="silver",fg="white",text="7",width="4",command=lambda: click("7"))
shift.grid(row=5,column=0,pady=0)
shift=Button(root,bg="silver",fg="white",text="8",width="4",command=lambda: click("8"))
shift.grid(row=5,column=1)
shift=Button(root,bg="silver",fg="white",text="9",width="4",command=lambda: click("9"))
shift.grid(row=5,column=2)
shift=Button(root,bg="orange",fg="white",text="AC",width="4",command=lambda: ac())
shift.grid(row=5,column=3,padx=3)
shift=Button(root,bg="orange",fg="white",text="DEL",width="4",command=lambda: delete())
shift.grid(row=5,column=4)

#row6

shift=Button(root,bg="silver",fg="white",text="4",width="4",command=lambda:click("4"))
shift.grid(row=6,column=0,pady=10)
shift=Button(root,bg="silver",fg="white",text="5",width="4",command=lambda:click("5"))
shift.grid(row=6,column=1)
shift=Button(root,bg="silver",fg="white",text="6",width="4",command=lambda:click("6"))
shift.grid(row=6,column=2)
shift=Button(root,bg="black",fg="white",text="*",width="4",command=lambda:click("*"))
shift.grid(row=6,column=3)
shift=Button(root,bg="black",fg="white",text="÷",width="4",command=lambda:click("/"))
shift.grid(row=6,column=4)

#row7

shift=Button(root,bg="silver",fg="white",text="1",width="4",command=lambda:click("1"))
shift.grid(row=7,column=0,pady=0)
shift=Button(root,bg="silver",fg="white",text="2",width="4",command=lambda:click("2"))
shift.grid(row=7,column=1)
shift=Button(root,bg="silver",fg="white",text="3",width="4",command=lambda:click("3"))
shift.grid(row=7,column=2)
shift=Button(root,bg="black",fg="white",text="+",width="4",command=lambda:click("+"))
shift.grid(row=7,column=3)
shift=Button(root,bg="black",fg="white",text="-",width="4",command=lambda:click("-"))
shift.grid(row=7,column=4)

#row8
shift=Button(root,bg="black",fg="white",text=".",width="4",command=lambda:click("."))
shift.grid(row=8,column=0,pady=10)
shift=Button(root,bg="silver",fg="white",text="0",width="4",command=lambda:click("0"))
shift.grid(row=8,column=1)
shift=Button(root,bg="black",fg="white",text="ans",width="4",command=lambda:ans())
shift.grid(row=8,column=2)
shift=Button(root,bg="black",fg="white",text="%",width="4",command=lambda:click("%"))
shift.grid(row=8,column=3)
shift=Button(root,bg="green",fg="white",text="=",width="4",command=lambda: equal())
shift.grid(row=8,column=4)

mainloop()
	
		
				
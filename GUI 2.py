import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title("GUI 2")
win.geometry("400x400")
l1=tk.Label(win,text="Admission Form")
l1.place(x=150,y=10)
l2=tk.Label(win,text="First Name")
l2.place(x=80,y=30)
e2=tk.Entry(win)
e2.place(x=150,y=30)
l3=tk.Label(win,text="Adress")
l3.place(x=80,y=50)
e3=tk.Entry(win)
e3.place(x=150,y=50)
l4=tk.Label(win,text="Courses")
l4.place(x=80,y=70)
LC=['BA','BSC','BED','LLB','BALLB']
c=ttk.Combobox(win,values=LC)
c.set("Pick your course")
c.place(x=150,y=70)
l5=tk.Label(win,text="Gender")
l5.place(x=80,y=90)
values={"r1":"Male","r2":"Female","r3":"Others"}
rv1=tk.Radiobutton(win,text="Male",value=values["r1"])
rv1.place(x=147,y=90)
rv2=tk.Radiobutton(win,text="Female",value=values["r2"])
rv2.place(x=207,y=90)
rv3=tk.Radiobutton(win,text="Others",value=values["r3"])
rv3.place(x=267,y=90)
l6=tk.Label(win,text="Domicile Of")
l6.place(x=80,y=110)
v1="Yes"
v2="NO"
dv1=tk.Radiobutton(win,text="Yes",value=v1)
dv1.place(x=147,y=110)
dv2=tk.Radiobutton(win,text="No",value=v2)
dv2.place(x=207,y=110)
l6a=tk.Label(win,text="J&K")
l6a.place(x=80,y=125)

win.mainloop()


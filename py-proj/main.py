from tkinter import *


def launchClock():
     import proj
     proj.pain()
def launchTimer():
    import tm
    tm.tm()   


selection=Tk()
selection.title("CLOCK")
selection.config(bg="teal")
selection.geometry("250x200")

start=Button(selection,text="Set Alarm",font=('comic sans',20),command=launchClock)
start.grid(row=2,column=2,columnspan=2,padx=10,pady=5)
start1=Button(selection,text="Set Timer",font=('comic sans',20),command=launchTimer)
start1.grid(row=4,column=2,columnspan=2,padx=10,pady=5)

selection.mainloop()
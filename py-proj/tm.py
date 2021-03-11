import time
from tkinter import *
from tkinter import messagebox
from pygame import mixer
 
def tm():
    # creating Tk window
    timer = Tk()
  
    # setting geometry of tk window
    timer.geometry("300x250")
  
    # title bar.
    timer.title("Time Counter")
    timer.config(bg="light blue")

    #start mixer
    mixer.init()

    
    # Declaration of variables
    hour=StringVar()
    minute=StringVar()
    second=StringVar()
  
    # setting the default value as 0
    hour.set("00")
    minute.set("00")
    second.set("00")

  
    # Use of Entry class to take input from the user
    hourEntry= Entry(timer, width=3, font=("Arial",18),bg="white",fg="black",textvariable=hour)
    hourEntry.place(x=80,y=20)
  
    minuteEntry= Entry(timer, width=3, font=("Arial",18),bg="white",fg="black",textvariable=minute)
    minuteEntry.place(x=130,y=20)
  
    secondEntry= Entry(timer, width=3, font=("Arial",18),bg="white",fg="black",textvariable=second)
    secondEntry.place(x=180,y=20)
  
  
    def submit():
    
        # the input provided by the user is
        # stored in here :temp
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    
        while temp >-1:
         
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins,secs = divmod(temp,60) 
  
        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 110*60 = 6600 => 1hr :
        # 50min: 0sec)
            hours=0
            if mins >60:
             
            # divmod(firstvalue = temp//60, secondvalue 
            # = temp%60)
                hours, mins = divmod(mins, 60)
         
        # using format () method to store the value up to 
        # two decimal places
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))
  
        # updating the GUI window after decrementing the
        # temp value every time
            timer.update()
            time.sleep(1)
  
        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
            if (temp == 0):
                mixer.music.load('timer.mp3')
                mixer.music.play()
                messagebox.showinfo("Time Countdown", "Time's up ")
            
                mixer.music.stop()
         
        # after every one sec the value of temp will be decremented
        # by one
            temp -= 1
 
        # button widget
    btn = Button(timer, text='Set Time Countdown', bd='5',bg="white",fg="black",command= submit)
    btn.place(x = 70,y = 120)
  
    timer.mainloop()
print("timer")
tm()

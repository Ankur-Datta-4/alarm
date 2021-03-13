#PROGRAM TO SET AN ALARM AT A USER-DEFINED TIME


from tkinter import *
from PIL import ImageTk,Image
import datetime
import time
from pygame import mixer
import threading
from tkinter import messagebox


def Main():
    

    #Tkinter window definition
    clock = Tk()    
    clock.title("Python Clock by Team U2")
    clock.geometry("600x350")

    #initialising the alarm tune to played whenever alarm is triggered
    mixer.init()

    #PART-A: Python Logic component


    #thread defining function: whenever an alarm is set, a th is the
    #function where the time is taken note
    def th():
        t1=threading.Thread(target=tickerRing,args=())
        if(timeValidator(hourEntry.get(), minuteEntry.get(), secondEntry.get()) and greater()):
            msg_sub=messagebox.showinfo("Alarm status","Alarm succesfully set!")
            t1.start()
        else:
           msg_sub=messagebox.showinfo("Alarm status","InValid input:") 

    #tickerRing function controls the functionality of the alarm. 
    #It sets the clock ticking, checking at every instance if the user_input_time==CurrentTime
    #Alarm rings continuously on reaching the specified time
    def tickerRing():
        a=hourEntry.get()+":"+minuteEntry.get()+":"+secondEntry.get()
        AlarmT=a
        CurrentTime=time.strftime("%H:%M:%S")

        while AlarmT!=CurrentTime:
            #time.sleep(1)
            CurrentTime=time.strftime("%H:%M:%S")
     
   
            if AlarmT==CurrentTime:
                mixer.music.load('alarm.mp3')
                mixer.music.play()
                msg=messagebox.showinfo('RING RING!!',f'{msgi.get()}')
                
        
                if msg=='ok':
                    mixer.music.stop()

   
        
    #TIMEVALIDATOR 1: checks if all the input lies in the correct range 
    def timeValidator(h,m,s):
        valid=False
        if(int(h) in range(0,24)):
            if(int(m) in range(0,60) and int(s) in range(0,60)):
                valid=True
        return valid
    
    
    #TIMEVALIDATOR 2: greater function checks if the user_input_time is less than the current time,
    #if so, it returns false::
    
    #this is called in the thread allocating function th
    def greater():
        userTime=hourEntry.get()+":"+minuteEntry.get()+":"+secondEntry.get()
        CurrentTime=time.strftime("%H:%M:%S")
        if(userTime<CurrentTime):
            return False
        else:
            return True

     #GUI Definition component

    #Defining regions in the tkinter window
    
    header=Frame(clock)
    header.place(x=5,y=5)

    head=Label(clock,text="SET THE TIME",font=('comic sans',20))
    head.pack(fill=X)


    panel = Frame(clock)
    panel.place(x=5,y=70)


     #4-clock image: if the clock image is fetchable, it'll display, otherwise
    #it prints "Image not found on the console"
    try:
        
        clock.iconbitmap('clock_derp.ico')
        my_img=ImageTk.PhotoImage(Image.open('clock_derp.ico'))
        img=Label(panel,image=my_img)
        img.grid(rowspan=4,column=0)

    except:
        print("Image not found")
        
        #5: Defining Label
    addTime = Label(panel,text = "Alarm Time \n(Hr:Min:Sec)",font=('comic sans',18))
    addTime.grid(row=0,column=1,padx=10,pady=5)



        #obtaining the time from the user 
    hour=StringVar()
    minute=StringVar()
    second=StringVar()


    hour.set("00")
    minute.set("00")
    second.set("00")
    
    hourEntry= Entry(panel, width=2, font=("Arial",18),bg="white",fg="black",textvariable=hour)
    hourEntry.place(x=320,y=20)
  
    minuteEntry= Entry(panel, width=2,font=("Arial",18),bg="white",fg="black",textvariable=minute)
    minuteEntry.place(x=360,y=20)
  
    secondEntry= Entry(panel, width=2, font=("Arial",18),bg="white",fg="black",textvariable=second)
    secondEntry.place(x=400,y=20)

        ################

 



    msg=Label(panel,text="Message",font=('comic sans',20))
    msg.grid(row=1,column=1,columnspan=2,padx=10,pady=5)


    #defining entry region for message obtained from the user for the alarm
    msgi=Entry(panel,font=('comic sans',15),width=25)
    msgi.grid(row=2,column=1,columnspan=2,padx=10,pady=5)

    #button to set the alarm
    start=Button(panel,text="Set Alarm",font=('comic sans',20),command=th)
    
    #Whenever the alarm is set a thread is allocated to the program with the
    #help of the threading module
    start.grid(row=3,column=1,columnspan=2,padx=10,pady=5)

    clock.mainloop()


print("FUNCTION CALLED")

Main()
        



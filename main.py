from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
nr=0
times=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_button():
    window.after_cancel(times)
    canvas.itemconfig(timer,text="00:00")
    label.config(text="TIMER",background="white",fg=RED)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_button():
    global nr
    nr+=1
    label.config(text="WORK", fg="blue",background=GREEN)
    count_down(int(entry.get())*60)
    if(nr%2== 0):
        label.config(text="Break", fg="break")
        count_down(5*60)
 
  
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min=math.floor(count/60)
    sec=count%60
    
    if(count%60==0):
        sec=str(count%60)+"0"
    elif(count%60 < 10):
        sec="0"+str(count%60)
    canvas.itemconfig(timer,text=f"{min}:{str(sec)}")
    if count > 0:
        global times
        times=window.after(1000, count_down, count-1)
    else:
        start_button()

        

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.config(padx=100,pady=40,background=GREEN)
canvas=Canvas(width=300,height=300,bg=GREEN,highlightthickness=0)  # highlightthickness e pentru a nu mai fi afisata marginea de la canvas
photo=PhotoImage(file="tomato.png")
entry=Entry(background=GREEN)
entry.place(x=90,y=50)
label_entry=Label(text="Minutes:",background=GREEN)
label_entry.place(x=30,y=50)
canvas.create_image(150,170,image=photo)
timer=canvas.create_text(150,160, text="00:00",font=(FONT_NAME,20,'bold'),fill="white")
canvas.pack()
label=Label(text="TIMER",fg=RED,highlightthickness=0,background="white",font=(FONT_NAME,20,'bold'))
label.place(x=115,y=5)

button_start=Button(text="Start",highlightthickness=0,background=GREEN,command=start_button)
button_start.place(x=30,y=250)

button_reset=Button(text="Reset",highlightthickness=0,background=GREEN,command=reset_button)
button_reset.place(x=230,y=250)







window.mainloop()
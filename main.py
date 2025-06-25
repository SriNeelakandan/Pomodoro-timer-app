from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = ("Courier",35,"bold")
WORK_MIN = 25
SHORT_BREAK_MIN =5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text = "00:00")
    timer_label.config(text="Timer")
    tick_label.config(text="")
    global reps
    reps =0
   
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps%2 ==0 and reps !=0:
        timer_label.config(text="BREAK",fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
    elif reps == 8:
        timer_label.config(text="BREAK",fg=RED)
        countdown(LONG_BREAK_MIN * 60)
    else:
        timer_label.config(text="WORK",fg=GREEN)
        countdown(WORK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
"""
For this ,there present after function present in Tk
after is a method that takes an amount of time that it should wait and after that time, it calls a particular function
window.after(time in milliseconds,function name,*args)
"""
def countdown(count):
    # We have to use canvas text which ia timer display
    # timer_text , How can we modify its value
    # canvas.itemconfig(canvas created text)
    count_minutes = count // 60
    count_seconds = count % 60

    if count_seconds <10:
        count_seconds= f"0{count_seconds}"
    canvas.itemconfig(timer_text,text = f"{count_minutes}:{count_seconds}")

    # How to display as 5:00, for that we need to learn dynamic typing
    if count>0:
        global timer
        timer =window.after(1000,countdown,count-1)
    else:
        start_timer()
        marks = ""
        # If we have completed 4 reps, it means
        # WORK + BREAK  - One session
        # WORK + BREAK - Another session 
        # So totally two sessions, which means reps /2 
        # but we got fractions, to avoid that we use 
        # floor // operator
        work_session=reps //2
        for _ in range(work_session):
            marks += "✔"
        tick_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(bg=YELLOW)
window.config(padx=100,pady=50)
# def say(thing):
#     print(thing)
#window.after(1000,say,"Neels") # thing = Neels
"""
We have done title the window , set the background color
we need to make our image present in the background
For that, we use canvas widget
Canvas Widget: It allows you to layer things
one on the top of the others

In our program ,we need image first and text on top of that image
"""

# Creation of canvas object with width and height

canvas = Canvas(width=200,height=224,bg =YELLOW,highlightthickness=0)
# I have changed the background color of window and Image
# But the white border line is visible - How to avoid that ?
# By using highlightthickness = 0 as a keyword argument in canvas definition
# Attach image by knowing their position through x and y coordinates
# canvas.create_image(100,112)
# We cannot add our image in canvas create itself
# Canvas didnot expect the image there, they need image objects
# for that, we use photo image , this creates image object by reading the file
tomato_image= PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_image)
canvas.grid(row=1,column=1)

# Image is createdusing canvas and displayed

# Lets create text

timer_text = canvas.create_text(105,130,text="00:00",fill="white",font=FONT_NAME)

timer_label = Label(text="Timer",font=FONT_NAME,fg=GREEN,bg = YELLOW)
timer_label.grid(row=0,column=1)
timer_label.config(padx=10)

tick_label = Label(fg = GREEN,bg = YELLOW)
tick_label.config(pady=20)
tick_label.grid(row=4,column=1)
# colors can be searched by website - color Hunt

start_button = Button(text="Start",command=start_timer,highlightthickness=0)
start_button.grid(row=4,column=0)



reset_button = Button(text="Reset",command=reset_timer,highlightthickness=0)
reset_button.grid(row=4,column=2)
window.mainloop()
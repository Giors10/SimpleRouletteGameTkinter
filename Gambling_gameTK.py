import tkinter as tk
from tkinter import messagebox
import random
from ctypes import windll
import math
from tkinter import DISABLED, NORMAL, E, W
import time
money = 0
marble_angle = 0
numberd = 0
strave = "normal"
root = tk.Tk()
root.geometry("1000x350")
windll.shcore.SetProcessDpiAwareness(1)
root.title("Rulet")
root.configure(background='Green')
entry_variable = tk.StringVar()
picked_option = tk.StringVar()
root.attributes('-topmost', 1)
root.resizable(False, False)


def create_wheel(canvas):
    canvas.create_oval(50, 50, 450, 450, fill="dark green", outline="white", width=2)
    red_numbers = {3, 9, 12, 18, 21, 27, 30, 36, 5, 14, 23, 32, 1, 7, 10, 16, 19, 25, 28, 34}
    for i in range(1, 37):
        angle = 360 - i * (360 / 37)
        angle_radians = math.radians(angle)
        x = 250 + 180 * math.cos(angle_radians)
        y = 250 - 180 * math.sin(angle_radians)
        color = "red" if i in red_numbers else "black"
        canvas.create_text(x, y, text=str(i), fill=color, font=("Arial", 10, "bold"))

def spin(canvas, spin_button, buttonState, animate_wheel):
    spin_button.config(state="disabled")
    buttonState(tk.DISABLED)
    animate_wheel(canvas, spin_button)

def animate_wheel(canvas, spin_button):
    speed = 20
    spins = random.randint(6, 10)
    angle_per_frame = speed
    total_angle = spins * 360
    animate_wheel_recursive(canvas, angle_per_frame, total_angle, 0, spin_button)

def animate_wheel_recursive(canvas, angle_per_frame, total_angle, current_angle, spin_button):
    if total_angle > 0:
        canvas.delete("marble")
        canvas.delete("arrow")
        global marble_angle 
        marble_angle += angle_per_frame
        marble_angle %= 360
        move_marble(canvas, marble_angle)
        canvas.create_arc(50, 50, 450, 450, start=current_angle, extent=total_angle, fill="", outline="dark green")
        canvas.create_text(250, 250, text="SPINNING", font=("Arial", 20, "bold"), tags="arrow")
        canvas.after(10, animate_wheel_recursive, canvas, angle_per_frame, total_angle - angle_per_frame, current_angle + angle_per_frame, spin_button)  # Pass spin_button
    else:
        result = random.randint(0, 36)
        land_on_number(canvas, result)
        spin_button.config(state="normal") 
        buttonState(tk.NORMAL)

def move_marble(canvas, marble_angle):
    angle_radians = math.radians(marble_angle)
    x = 250 + 180 * math.cos(angle_radians)
    y = 250 - 180 * math.sin(angle_radians)
    canvas.delete("marble")
    marble = canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="white", tags="marble")

def buttonState(state):
    for button in [button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12,
                buttonq, buttonw, buttone, buttonr, buttont, buttony, buttonu, buttoni, buttono, buttonp, buttona, buttonsd,
                buttond, buttonf, buttong, buttonh, buttonj, buttonk, buttonl, buttonz, buttonx, buttonc, buttonv, buttonb, bun1, bun2, bun3, bun4, bun5, bun6,buttonbq,buttoncq,buttonvq]:
        button.config(state=state)



def land_on_number(canvas, number):
    global numberd
    angle = 360 - number * (360 / 37)
    angle_radians = math.radians(angle)
    x = 250 + 180 * math.cos(angle_radians)
    y = 250 - 180 * math.sin(angle_radians)
    canvas.delete("marble")
    picked_option_value = picked_option.get()
    if picked_option_value.isdigit() and 1 <= int(picked_option_value) <= 36:
        numberd = int(picked_option_value)

    marble = canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red", tags="marble")
    if picked_option.get() == "Black" and number in [6,15,24,33, 2, 8, 11, 17, 20, 26, 29, 35, 4, 13, 22, 31]:
        messagebox.showinfo("Result", "Well done, you guessed the right number! Your money has been doubled.")
        current_money = int(entry_variable.get())
        new_money = current_money * 2
        entry_variable.set(new_money)
        buttonState(tk.NORMAL)
    elif picked_option.get() == "Red" and number in [3, 9, 12, 18, 21, 27, 30, 36, 5, 14, 23, 32, 1, 7, 10, 16, 19, 25, 28, 34]:
        messagebox.showinfo("Result", "Well done, you guessed the right number! Your money has been doubled.")
        current_money = int(entry_variable.get())
        new_money = current_money * 2
        entry_variable.set(new_money)
        buttonState(tk.NORMAL)
    elif picked_option.get() == "1st12" and number in [1,2,3,4,5,6,7,8,9,10,11,12]:
        messagebox.showinfo("Result", "Well done, you guessed the right number! Your money has been tripled.")
        current_money = int(entry_variable.get())
        new_money = current_money * 3
        entry_variable.set(new_money)
        buttonState(tk.NORMAL)
    elif picked_option.get() == "2nd12" and number in [13,14,15,16,17,18,19,20,21,22,23,24]:
        messagebox.showinfo("Result", "Well done, you guessed the right number! Your money has been tripled.")
        current_money = int(entry_variable.get())
        new_money = current_money * 3
        entry_variable.set(new_money)
        buttonState(tk.NORMAL)
    elif picked_option.get() == "3rd12" and number in [25,26,27,28,29,30,31,32,33,34,35,36]:
        messagebox.showinfo("Result", "Well done, you guessed the right number! Your money has been tripled.")
        current_money = int(entry_variable.get())
        new_money = current_money * 3
        entry_variable.set(new_money)
        buttonState(tk.NORMAL)
    elif picked_option.get() == "1-18" and number in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]:
        messagebox.showinfo("Result", "Well done, you guessed the right number! Your money has been quadrupled.")
        current_money = int(entry_variable.get())
        new_money = current_money * 2
        entry_variable.set(new_money)
        buttonState(tk.NORMAL)
    elif picked_option.get() == "19-36" and number in [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]:
        messagebox.showinfo("Result", "Well done, you guessed the right number! Your money has been quadrupled.")
        current_money = int(entry_variable.get())
        new_money = current_money * 2
        entry_variable.set(new_money)
        buttonState(tk.NORMAL)
    elif picked_option.get() == "Even" and number % 2 == 0:
        messagebox.showinfo("Result", "Well done, you guessed the right number! Your money has been doubled.")
        current_money = int(entry_variable.get())
        new_money = current_money * 2
        entry_variable.set(new_money)
        buttonState(tk.NORMAL)
    elif picked_option.get() == "Odd" and number % 2 != 0:
        messagebox.showinfo("Result", "Well done, you guessed the right number! Your money has been doubled.")
        current_money = int(entry_variable.get())
        new_money = current_money * 2
        entry_variable.set(new_money)
        buttonState(tk.NORMAL)
    elif numberd == int(number):
        messagebox.showinfo("Result", f"Congratulations! You won! The winning number is: {number} and you picked: {numberd}! Your money has been multiplied by 36!")
        current_money = int(entry_variable.get())
        new_money = current_money * 36
        entry_variable.set(new_money)
        buttonState(tk.NORMAL)

    else:
        messagebox.showinfo("Result", f"Sorry! You lost! The winning number is: {number}! Better luck next time!")
        entry_variable.set(0)
        buttonState(tk.NORMAL)

window = tk.Tk()
window.title("Roulette")
window.geometry("550x610")
window.attributes('-topmost', 1)
canvas = tk.Canvas(window, width=500, height=500, bg="dark green")
canvas.grid(row=10, column=0, columnspan=3, padx=20, pady=20)

create_wheel(canvas) 
canvas.update()

spin_button = tk.Button(window, text="Spin", command=lambda: spin(canvas, spin_button, buttonState, animate_wheel), font=("Arial", 12, "bold"), bg="orange", fg="white")
spin_button.grid(row=11, column=1, pady=10)


r = 2
t = 3
u = 4
y = 1
x = 1
w = 10
h = 3
title = tk.Label(text = "Choose an option", font = 'arial',bg = "Green", fg = "White").grid(row = 1, column = 2, columnspan = 10)
def func(args):
    global picked_option  # Update the global picked_option variable
    picked_option.set(args)
    numbers = random.randint(0, 36)
    
    for button in [button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12,
                   buttonq, buttonw, buttone, buttonr, buttont, buttony, buttonu, buttoni, buttono, buttonp, buttona, buttonsd,
                   buttond, buttonf, buttong, buttonh, buttonj, buttonk, buttonl, buttonz, buttonx, buttonc, buttonv, buttonb, bun1,bun2,bun3,bun4,bun5,bun6,buttonbq,buttoncq,buttonvq]:
        button.config(state=tk.DISABLED)
        option = picked_option.get()
def set_variable():
    if entryq.get() == "":
        messagebox.showerror("Error", "Please enter a valid number")
        return
    if entryq.get() == "wrong":
        for button in [button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12,
                   buttonq, buttonw, buttone, buttonr, buttont, buttony, buttonu, buttoni, buttono, buttonp, buttona, buttonsd,
                   buttond, buttonf, buttong, buttonh, buttonj, buttonk, buttonl, buttonz, buttonx, buttonc, buttonv, buttonb, bun1,bun2,bun3,bun4,bun5,bun6,buttonbq,buttoncq,buttonvq]:
            button.config(state=tk.NORMAL)
        spin_button.config(state="normal") 
        buttonState(tk.NORMAL)
        
    moneyInput_str = entryq.get() 
    moneyInput = 0 
    if moneyInput_str:  
        moneyInput = int(moneyInput_str)  
    moneyon_str = entry_variable.get()  
    if moneyon_str:  
        moneyon = int(moneyon_str)  
    else:
        moneyon = 0  
    entry_variable.set(moneyon + moneyInput)
    print("Entry variable set to:", entry_variable.get()) 
    money = entry_variable.get()
def add_number():
    buttonState(NORMAL)
    

    

root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(1, weight=1)
button1 = tk.Button(root, text="3", bg="Red", foreground="White", width=w, height=h, command=lambda: func(3))
button1.grid(row=r, column=1, padx=x, pady=y,sticky=E+W)

button2 = tk.Button(root, text="6", bg="Black", foreground="White", width=w, height=h, command=lambda: func(6))
button2.grid(row=r, column=2, padx=x, pady=y,sticky=E+W)

button3 = tk.Button(root, text="9", bg="Red", foreground="White", width=w, height=h, command=lambda: func(9))
button3.grid(row=r, column=3, padx=x, pady=y,sticky=E+W)

button4 = tk.Button(root, text="12", bg="Red", foreground="White", width=w, height=h, command=lambda: func(12))
button4.grid(row=r, column=4, padx=x, pady=y,sticky=E+W)

button5 = tk.Button(root, text="15", bg="Black", foreground="White", width=w, height=h, command=lambda: func(15))
button5.grid(row=r, column=5, padx=x, pady=y,sticky=E+W)

button6 = tk.Button(root, text="18", bg="Red", foreground="White", width=w, height=h, command=lambda: func(18))
button6.grid(row=r, column=6, padx=x, pady=y,sticky=E+W)

button7 = tk.Button(root, text="21", bg="Red", foreground="White", width=w, height=h, command=lambda: func(21))
button7.grid(row=r, column=7, padx=x, pady=y,sticky=E+W)

button8 = tk.Button(root, text="24", bg="Black", foreground="White", width=w, height=h, command=lambda: func(24))
button8.grid(row=r, column=8, padx=x, pady=y,sticky=E+W)

button9 = tk.Button(root, text="27", bg="Red", foreground="White", width=w, height=h, command=lambda: func(27))
button9.grid(row=r, column=9, padx=x, pady=y,sticky=E+W)

button10 = tk.Button(root, text="30", bg="Red", foreground="White", width=w, height=h, command=lambda: func(30))
button10.grid(row=r, column=10, padx=x, pady=y,sticky=E+W)

button11 = tk.Button(root, text="33", bg="Black", foreground="White", width=w, height=h, command=lambda: func(33))
button11.grid(row=r, column=11, padx=x, pady=y,sticky=E+W)

button12 = tk.Button(root, text="36", bg="Red", foreground="White", width=w, height=h, command=lambda: func(36))
button12.grid(row=r, column=12, padx=x, pady=y,sticky=E+W)


buttonq = tk.Button(root, text="2", bg="Black", foreground="White", width=w, height=h, command=lambda: func(2))
buttonq.grid(row=t, column=1, padx=x, pady=y,sticky=E+W)

buttonw = tk.Button(root, text="5", bg="Red", foreground="White", width=w, height=h, command=lambda: func(5))
buttonw.grid(row=t, column=2, padx=x, pady=y,sticky=E+W)

buttone = tk.Button(root, text="8", bg="Black", foreground="White", width=w, height=h, command=lambda: func(8))
buttone.grid(row=t, column=3, padx=x, pady=y,sticky=E+W)

buttonr = tk.Button(root, text="11", bg="Black", foreground="White", width=w, height=h, command=lambda: func(11))
buttonr.grid(row=t, column=4, padx=x, pady=y,sticky=E+W)

buttont = tk.Button(root, text="14", bg="Red", foreground="White", width=w, height=h, command=lambda: func(14))
buttont.grid(row=t, column=5, padx=x, pady=y,sticky=E+W)

buttony = tk.Button(root, text="17", bg="Black", foreground="White", width=w, height=h, command=lambda: func(17))
buttony.grid(row=t, column=6, padx=x, pady=y,sticky=E+W)

buttonu = tk.Button(root, text="20", bg="Black", foreground="White", width=w, height=h, command=lambda: func(20))
buttonu.grid(row=t, column=7, padx=x, pady=y,sticky=E+W)

buttoni = tk.Button(root, text="23", bg="Red", foreground="White", width=w, height=h, command=lambda: func(23))
buttoni.grid(row=t, column=8, padx=x, pady=y,sticky=E+W)

buttono = tk.Button(root, text="26", bg="Black", foreground="White", width=w, height=h, command=lambda: func(26))
buttono.grid(row=t, column=9, padx=x, pady=y,sticky=E+W)

buttonp = tk.Button(root, text="29", bg="Black", foreground="White", width=w, height=h, command=lambda: func(29))
buttonp.grid(row=t, column=10, padx=x, pady=y,sticky=E+W)

buttona = tk.Button(root, text="32", bg="Red", foreground="White", width=w, height=h, command=lambda: func(32))
buttona.grid(row=t, column=11, padx=x, pady=y,sticky=E+W)

buttonsd = tk.Button(root, text="35", bg="Black", foreground="White", width=w, height=h, command=lambda: func(35))
buttonsd.grid(row=t, column=12, padx=x, pady=y,sticky=E+W)

buttond = tk.Button(root, text="1", bg="Red", foreground="White", width=w, height=h, command=lambda: func(1))
buttond.grid(row=u, column=1, padx=x, pady=y,sticky=E+W)

buttonf = tk.Button(root, text="4", bg="Black", foreground="White", width=w, height=h, command=lambda: func(4))
buttonf.grid(row=u, column=2, padx=x, pady=y,sticky=E+W)

buttong = tk.Button(root, text="7", bg="Red", foreground="White", width=w, height=h, command=lambda: func(7))
buttong.grid(row=u, column=3, padx=x, pady=y,sticky=E+W)

buttonh = tk.Button(root, text="10", bg="Red", foreground="White", width=w, height=h, command=lambda: func(10))
buttonh.grid(row=u, column=4, padx=x, pady=y,sticky=E+W)

buttonj = tk.Button(root, text="13", bg="Black", foreground="White", width=w, height=h, command=lambda: func(13))
buttonj.grid(row=u, column=5, padx=x, pady=y,sticky=E+W)

buttonk = tk.Button(root, text="16", bg="Red", foreground="White", width=w, height=h, command=lambda: func(16))
buttonk.grid(row=u, column=6, padx=x, pady=y,sticky=E+W)

buttonl = tk.Button(root, text="19", bg="Red", foreground="White", width=w, height=h, command=lambda: func(19))
buttonl.grid(row=u, column=7, padx=x, pady=y,sticky=E+W)

buttonz = tk.Button(root, text="22", bg="Black", foreground="White", width=w, height=h, command=lambda: func(22))
buttonz.grid(row=u, column=8, padx=x, pady=y,sticky=E+W)

buttonx = tk.Button(root, text="25", bg="Red", foreground="White", width=w, height=h, command=lambda: func(25))
buttonx.grid(row=u, column=9, padx=x, pady=y,sticky=E+W)

buttonc = tk.Button(root, text="28", bg="Red", foreground="White", width=w, height=h, command=lambda: func(28))
buttonc.grid(row=u, column=10, padx=x, pady=y,sticky=E+W)

buttonv = tk.Button(root, text="31", bg="Black", foreground="White", width=w, height=h, command=lambda: func(31))
buttonv.grid(row=u, column=11, padx=x, pady=y,sticky=E+W)

buttonb = tk.Button(root, text="34", bg="Red", foreground="White", width=w, height=h, command=lambda: func(34))
buttonb.grid(row=u, column=12, padx=x, pady=y,sticky=E+W)

buttoncq = tk.Button(root, text="1st 12", foreground="White", bg="Green", width=44, command=lambda: func("1st12"))
buttoncq.grid(row=5, column=1, columnspan=4, rowspan=1)

buttonvq = tk.Button(root, text="2nd 12", foreground="White", bg="Green", width=45, command=lambda: func("2nd12"))
buttonvq.grid(row=5, column=5, columnspan=4)

buttonbq = tk.Button(root, text="3rd 12", foreground="White", bg="Green", width=45, command=lambda: func("3rd12"))
buttonbq.grid(row=5, column=9, columnspan=4)

bun1 = tk.Button(root, text="1-18", fg="White", bg="Green", width = 22, height=h, command=lambda: func("1-18"))
bun1.grid(row=6, column=1, padx=x, pady=y,sticky=E+W, columnspan=2)

bun2 = tk.Button(root, text="Even", fg="White", bg="Green", width=22, height=h, command=lambda: func("Even"))
bun2.grid(row=6, column=3, padx=x, pady=y,sticky=E+W, columnspan=2)

bun3 = tk.Button(root, text="Red", fg="White", bg="Green", width=22, height=h, command=lambda: func("Red"))
bun3.grid(row=6, column=5, padx=x, pady=y,sticky=E+W, columnspan=2)

bun4 = tk.Button(root, text="Black", fg="White", bg="Green", width=22, height=h,command=lambda: func("Black"))
bun4.grid(row=6, column=7, padx=x, pady=y,sticky=E+W, columnspan=2)

bun5 = tk.Button(root, text="Odd", fg="White", bg="Green", width=22, height=h,command=lambda: func("Odd"))
bun5.grid(row=6, column=9, padx=x, pady=y,sticky=E+W, columnspan=2)

bun6 = tk.Button(root, text="19 - 36", fg="White", bg="Green", width=22, height=h, command=lambda: func("19-36"))
bun6.grid(row=6, column=11, padx=x, pady=y,sticky=E+W, columnspan=2)

labelq = tk.Label(root, text = "How much money are you betting:", fg = "White", bg = "Green").grid(row = 9, column = 1, columnspan = 5)
entryq = tk.Entry(root, width = 16, fg = "White", bg = "Green")
entryq.grid(row=9, column=4, columnspan=4)
buttun12 = tk.Button(root, width = 8, text = "Enter", bg = "Green", fg = "White", command=set_variable).grid(row = 9, column = 7, columnspan = 2)
button14 = tk.Button(root, text="Add another number", bg = "Green", fg = "White", command=add_number).grid(row = 9, column = 10, columnspan = 2)
Labelmon = tk.Label(root, text = "Your money is: £", fg = "White", bg = "Green").grid(row = 10, column = 1, columnspan = 5)
labelw = tk.Label(root, textvariable=entry_variable, fg="White", bg="Green")
labelw.grid(row=10, column=4, columnspan=4)
labelpick = tk.Label(root, text = "You picked option: ", fg = "White", bg = "Green").grid(row = 11, column = 1, columnspan = 5)
labelpickac = tk.Label(root, textvariable = picked_option, fg = "White", bg = "Green").grid(row = 11, column =4, columnspan = 4)



root.mainloop()
window.mainloop()










# -*- coding: utf-8 -*-
import tkinter as tk

#--- Button Actions -----
def clicked_1():
    lbl2.configure(text = "You clicked button 1")
def clicked_2():
    lbl2.configure(text = "You clicked button 2")
def clicked_3():
    lbl2.configure(text = "You clicked button 3")


# === Create a canvas with Tkinter ===
# --- Basic Properties of the window ----------------------
window = tk.Tk()
window.title("A button selection")
window.geometry('500x280')

# --- Define top, middle and bottom frames -----------------
top_frame = tk.Frame(window)
top_frame.pack()

middle_frame = tk.Frame(window)
middle_frame.pack()

bottom_frame = tk.Frame(window)
bottom_frame.pack(side = tk.BOTTOM)

# --- Define elements in top frame -----------------
lbl1 = tk.Label(top_frame, text="Click on one of the three buttons", font=('Helvetica', '20'), pady = 30)
lbl1.pack(side=tk.LEFT)

# --- Define elements in middle frame -------------------
# Note that the buttons contain references to functions that are to be run when they are clicked
btn1 = tk.Button(middle_frame, text="Button 1\nChoose me", font=('Helvetica', '20'), command=clicked_1)
btn1.pack(side=tk.LEFT)
btn2 = tk.Button(middle_frame, text="Button 2\nChoose me", font=('Helvetica', '20'),  command=clicked_2)
btn2.pack(side=tk.LEFT)
btn3 = tk.Button(middle_frame, text="Button 3\nChoose me", font=('Helvetica', '20'),  command=clicked_3)
btn3.pack(side=tk.LEFT)

# --- Define elements in bottom frame -----------------
# Note that this label starts off with an empty string that is modified by the button functions at the top
lbl2 = tk.Label(bottom_frame, text="", font=('Helvetica', '20'))
lbl2.pack(side=tk.BOTTOM, pady = 30)
# === End of Canvas creation ===========

window.mainloop()


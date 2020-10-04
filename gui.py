from tkinter import *
from calc import calc


def calculate():
    msg = calc(p.get(), s.get())
    output.delete(1.0, END)
    output.insert(1.0, msg + "\n\n")


def calculate_bound(e):
    # bind() sends an event
    calculate()


def reset():
    s.delete(0, END)
    p.delete(0, END)
    output.delete(1.0, END)


window = Tk()

window.title("ThermoVapor")
window.geometry("400x500+150+150")
window.bind("<Return>", calculate_bound)
window.bind("<KP_Enter>", calculate_bound)

frame = Frame(window, pady=12)
frame.pack()

heading = Label(frame, text="ThermoVapor", pady=16, font=("application", 36, "bold"))
heading.grid(row=0, columnspan=2)

monospace = ("Courier", 16)

p = Label(frame, text="P:", font=monospace)
p.grid(row=1, sticky=E)
p = Entry(frame, width=16, font=monospace)
p.grid(row=1, column=1, sticky=W)

s = Label(frame, text="s:", font=monospace)
s.grid(row=2, sticky=E)
s = Entry(frame, width=16, font=monospace)
s.grid(row=2, column=1, sticky=W)

submit = Button(frame, text="Interpolate", command=calculate, pady=12)
submit.grid(row=3, columnspan=2)

reset = Button(frame, text="Reset", command=reset)
reset.grid(row=4, columnspan=2)

output = Text(background="#ffffe5", font=monospace, padx=8, pady=8)
output.pack()

window.mainloop()

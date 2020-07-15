from tkinter import *
import parser

root = Tk()
root.title("CALCULATOR")

#entering number into display field

i = 0
def display_num (num):
    global i
    display.insert(i, num)
    i += 1

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length

def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"error")

def clear_all():
    display.delete(0, END)

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "Error")
#adding entry field

display=Entry(root, bg = "yellow")
display.grid(row=0, columnspan=6, sticky=W+E)

#Adding buttons

Button(root, text="1", bg="pink", command=lambda: display_num(1)).grid(row=1, column=0)
Button(root, text="2", bg="pink", command=lambda: display_num(2)).grid(row=1, column=1)
Button(root, text="3", bg="pink", command=lambda: display_num(3)).grid(row=1, column=2)

Button(root, text="4", bg="pink", command=lambda: display_num(4)).grid(row=2, column=0)
Button(root, text="5", bg="pink", command=lambda: display_num(5)).grid(row=2, column=1)
Button(root, text="6", bg="pink", command=lambda: display_num(6)).grid(row=2, column=2)

Button(root, text="7", bg="pink", command=lambda: display_num(7)).grid(row=3, column=0)
Button(root, text="8", bg="pink", command=lambda: display_num(8)).grid(row=3, column=1)
Button(root, text="9", bg="pink", command=lambda: display_num(9)).grid(row=3, column=2)

#ADDING OTHER BUTTONS

Button(root, text="Ac", bg="pink", command=lambda: clear_all()).grid(row=4, column=0)
Button(root, text="0", bg="pink", command=lambda: display_num(0)).grid(row=4, column=1)
Button(root, text="=", bg="pink", command=lambda : calculate()).grid(row=4, column=2)

#OPERATING

Button(root, text="+", bg="cyan", command=lambda : get_operation("+")).grid(row=1, column=3)
Button(root, text="-", bg="cyan", command=lambda : get_operation("-")).grid(row=2, column=3)
Button(root, text="*", bg="cyan", command=lambda : get_operation("*")).grid(row=3, column=3)
Button(root, text="/", bg="cyan", command=lambda : get_operation("/")).grid(row=4, column=3)

#FEW MORE OPERATIONS
Button(root, text="pi", bg="cyan", command=lambda : get_operation("*3.14")).grid(row=1, column=4)
Button(root, text="%", bg="cyan", command=lambda : get_operation("%")).grid(row=2, column=4)
Button(root, text="x!", bg="cyan").grid(row=3, column=4)
Button(root, text="(", bg="cyan", command=lambda : get_operation("(")).grid(row=4, column=4)

#MORE FUNCTIONALITIES

Button(root, text="C", bg="cyan", command=lambda: undo()).grid(row=1, column=5)
Button(root, text="^2", bg="cyan", command=lambda : get_operation("**2")).grid(row=2, column=5)
Button(root, text="exp", bg="cyan", command=lambda : get_operation("**")).grid(row=3, column=5)
Button(root, text=")", bg="cyan", command=lambda : get_operation(")")).grid(row=4, column=5)
root.mainloop()
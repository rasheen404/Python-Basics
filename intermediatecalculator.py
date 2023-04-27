# python intermediate calculator

# importing the necessary modules
from logging import root
from tkinter import *
 import parser
from math import factorial

# making a window for our calculator

root = Tk()
root.title('intermrdiatepython - Calculator')
root.mainloop()

# Designing the buttons
# adding the input field
display = Entry(root)
display.grid(row=1,columnspan=6,sticky=N+E+W+S)

#Code to add buttons to the calculator

Button(root.text="1",command = lambda :get_variable(1)).grid(row=2,column=0,sticky=N+S+E+W)
Button(root.text="2",command = lambda :get_variable(2)).grid(row=2,column=1,sticky=N+S+E+W)
Button(root.text="3",command = lambda :get_variable(3)).grid(row=2,column=2,sticky=N+S+E+W)

Button(root.text="4",command = lambda :get_variable(4)).grid(row=3,column=0,sticky=N+S+E+W)
Button(root.text="5",command = lambda :get_variable(5)).grid(row=3,column=1,sticky=N+S+E+W)
Button(root.text="6",command = lambda :get_variable(6)).grid(row=3,column=2,sticky=N+S+E+W)

Button(root.text="1",command = lambda :get_variable(7)).grid(row=4,column=0,sticky=N+S+E+W)
Button(root.text="2",command = lambda :get_variable(8)).grid(row=4,column=1,sticky=N+S+E+W)
Button(root.text="3",command = lambda :get_variable(9)).grid(row=4,column=2,sticky=N+S+E+W)

#adding other special buttons to the calculator

Button(root.text="AC",command = lambda :clear_all()).grid(row=2,column=0,sticky=N+S+E+W)
Button(root.text="0",command = lambda :get_variable(0)).grid(row=2,column=1,sticky=N+S+E+W)
Button(root.text=".",command = lambda :get_variable(".")).grid(row=2,column=2,sticky=N+S+E+W)

# adding operation buttons to the calculator

Button(root.text="+",command = lambda :get_operation("+")).grid(row=2,column=0,sticky=N+S+E+W)
Button(root.text="-",command = lambda :get_operation("-")).grid(row=3,column=1,sticky=N+S+E+W)
Button(root.text="*",command = lambda :get_operation("*")).grid(row=4,column=2,sticky=N+S+E+W)
Button(root.text="/",command = lambda :get_operation("/")).grid(row=5,column=2,sticky=N+S+E+W)
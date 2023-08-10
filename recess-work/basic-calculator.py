import tkinter as tk

# globally declare the calculation variable
calculation = ""
# function to update calculation in the text entry box
def add_to_calculation(symbol):
    # point out the global calculation variable
    global calculation
    # concatenation of string
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
    # Function to evaluate the final expression


# noinspection PyBroadException
def evaluate_calculation():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
    # Put that code inside the try block
    # which may generate the error
    global calculation
    try:
        # eval function evaluate the calculation
        # and str function convert the result
        # into string
        result = str(eval(calculation))
        # initialize the calculation variable
        # by empty string
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
        # if the error is generated then handle
        # by the except block
    except:
        clear_field()
        text_result.insert(1.0, "Syntax Error")
        # Function to clear the contents
        # of text entry box
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")
# Create GUI window
root = tk.Tk()


# Set configuration for the GUI window
root.geometry("1000x1000")
# Set title for the GUI window
root.title("Amanda_Ann_Kirabo_Calculator")
# Set background color
root.configure(background="white")

text_result = tk.Text(root, height=2, width=55, font=("Arial", 25))
text_result.grid(columnspan=90)

# create Buttons and place them at a particular location inside the root window .
# when user press the button, the function affiliated to that button is executed .
btn1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1),
                 width=20, font=("Arial", 14), fg='white', bg='teal')
btn1.grid(row=2, column=1)
btn2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2),
                 width=20, font=("Arial", 14), fg='white', bg='teal')
btn2.grid(row=2, column=2)
btn3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3),
                 width=20, font=("Arial", 14), fg='white', bg='teal')
btn3.grid(row=2, column=3)
btn4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4),
                 width=20, font=("Arial", 14), fg='white', bg='teal')
btn4.grid(row=3, column=1)
btn5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5),
                 width=20, font=("Arial", 14), fg='white', bg='teal')
btn5.grid(row=3, column=2)
btn6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6),
                 width=20, font=("Arial", 14), fg='white', bg='teal')
btn6.grid(row=3, column=3)
btn7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7),
                 width=20, font=("Arial", 14), fg='white', bg='teal')
btn7.grid(row=4, column=1)
btn8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8),
                 width=20, font=("Arial", 14), fg='white', bg='teal')
btn8.grid(row=4, column=2)
btn9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9),
                 width=20, font=("Arial", 14), fg='white',
                 bg='teal')
btn9.grid(row=4, column=3)
btn0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0),
                 width=20, font=("Arial", 14), fg='white', bg='teal')
btn0.grid(row=5, column=2)
btn_ob = tk.Button(root, text="(", command=lambda: add_to_calculation("("),
                   width=20, font=("Arial", 14), fg='white', bg='teal')
btn_ob.grid(row=5, column=1)
btn_oc = tk.Button(root, text=")", command=lambda: add_to_calculation(")"),
                   width=20, font=("Arial", 14), fg='white', bg='teal')
btn_oc.grid(row=5, column=3)
btn_times = tk.Button(root, text="*", command=lambda: add_to_calculation("*"),
                      width=20, font=("Arial", 14), fg='white', bg='orange')
btn_times.grid(row=3, column=4)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"),
                     width=20, font=("Arial", 14), fg='white', bg='orange')
btn_plus.grid(row=4, column=4)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"),
                      width=20, font=("Arial", 14), fg='white', bg='orange')
btn_minus.grid(row=5, column=4)
btn_divide = tk.Button(root, text="/", command=lambda: add_to_calculation("/"),
                       width=20, font=("Arial", 14), fg='white', bg='orange')
btn_divide.grid(row=6, column=4)
btn_ac = tk.Button(root, text="AC", command=clear_field,
                   width=20, font=("Arial", 14), fg='white', bg='red')
btn_ac.grid(row=2, column=4)
btn_equals = tk.Button(root, text="=", command=evaluate_calculation,
                       width=20, font=("Arial", 14), fg='white', bg='teal')
btn_equals.grid(row=6, column=3)
btn_dec = tk.Button(root, text=".", command=lambda: add_to_calculation("."),
                    width=20, font=("Arial", 14), fg='white', bg='teal')
btn_dec.grid(row=6, column=1)
btn_zero = tk.Button(root, text="00", command=lambda: add_to_calculation("00"),
                     width=20, font=("Arial", 14), fg='white', bg='teal')
btn_zero.grid(row=6, column=2)
# Start the GUI
root.mainloop()


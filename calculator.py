import tkinter as tk

# Create the root window
root = tk.Tk()
root.title("Calculator")

# Global variables
expression = ""

# Function to update the display when buttons are pressed
def button_click(value):
    global expression
    expression += str(value)
    display_var.set(expression)

# Function to evaluate the expression
def calculate():
    global expression
    try:
        result = str(eval(expression))  # Evaluate the expression
        display_var.set(result)
        expression = result  # Store result for future calculations
    except Exception as e:
        display_var.set("Error")
        expression = ""

# Function to clear the display
def clear_display():
    global expression
    expression = ""
    display_var.set("")

# Create the display entry with variable
display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
display.grid(row=0, column=0, columnspan=4)

# Create buttons for numbers and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == "=":
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18), command=calculate).grid(row=row, column=col)
    elif button == "C":
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18), command=clear_display).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18), 
                  command=lambda b=button: button_click(b)).grid(row=row, column=col)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the GUI main loop
root.mainloop()

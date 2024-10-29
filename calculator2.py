import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Global variables
current_expression = ""
input_text = tk.StringVar()

# Function to update expression in the text entry box
def update_expression(value):
    global current_expression
    current_expression += value
    input_text.set(current_expression)

# Function to clear the input field
def clear_input():
    global current_expression
    current_expression = ""
    input_text.set(current_expression)

# Function to evaluate the expression
def evaluate_expression():
    global current_expression
    try:
        result = str(eval(current_expression))
        input_text.set(result)
        current_expression = result
    except Exception as e:
        input_text.set("Error")
        current_expression = ""

# Create the input field
input_field = tk.Entry(root, textvariable=input_text, font=('Arial', 18), bd=10, insertwidth=2, width=14, borderwidth=4)
input_field.grid(row=0, column=0, columnspan=4)

# Calculator buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18),
                           command=evaluate_expression)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18),
                           command=lambda t=text: update_expression(t))
    button.grid(row=row, column=col)

# Clear button
clear_button = tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18),
                         command=clear_input)
clear_button.grid(row=4, column=3)

# Run the main event loop
root.mainloop()

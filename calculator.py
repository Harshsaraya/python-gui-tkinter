from tkinter import *

first_number = None
operator = None
waiting_for_new_number = False
decimal_used = False  # Track if decimal point is used

def update_status(msg):
    status_label.config(text=msg)

def get_digit(digit):
    global waiting_for_new_number
    current = result_label['text']

    if waiting_for_new_number or current == "0":
        result_label.config(text=str(digit))
        waiting_for_new_number = False
    else:
        result_label.config(text=current + str(digit))

    update_status('')

def get_decimal():
    global waiting_for_new_number, decimal_used
    current = result_label['text']

    if waiting_for_new_number:
        result_label.config(text="0.")
        decimal_used = True
        waiting_for_new_number = False
    elif not decimal_used:
        result_label.config(text=current + '.')
        decimal_used = True

def clear():
    global first_number, operator, waiting_for_new_number, decimal_used
    result_label.config(text='0')
    first_number = None
    operator = None
    waiting_for_new_number = False
    decimal_used = False
    update_status('Cleared')

def backspace():
    global decimal_used
    current = result_label['text']
    if len(current) > 1:
        if current[-1] == '.':
            decimal_used = False
        result_label.config(text=current[:-1])
    else:
        result_label.config(text='0')
    update_status('')

def calculate(n1, op, n2):
    try:
        if op == '+':
            return n1 + n2
        elif op == '-':
            return n1 - n2
        elif op == '*':
            return n1 * n2
        elif op == '/':
            if n2 == 0:
                return 'Cannot divide by zero'
            return round(n1 / n2, 8)  # show up to 8 decimals
        else:
            return 'Unknown operator'
    except Exception:
        return 'Calculation error'

def get_operator(op):
    global first_number, operator, waiting_for_new_number, decimal_used
    try:
        current_text = result_label['text']
        if current_text == '':
            update_status('Please enter a number first')
            return

        current_number = float(current_text)

        if first_number is None:
            first_number = current_number
        else:
            result = calculate(first_number, operator, current_number)
            if isinstance(result, str):
                update_status(result)
                result_label.config(text='Error')
                first_number = None
                operator = None
                waiting_for_new_number = False
                decimal_used = False
                return
            first_number = result
            # Format to remove trailing zeros after decimal point
            str_result = str(result)
            if '.' in str_result:
                str_result = str_result.rstrip('0').rstrip('.')
            result_label.config(text=str_result)

        operator = op
        waiting_for_new_number = True
        decimal_used = False
        update_status(f'Operator "{op}" set')
    except ValueError:
        update_status('Invalid number input')
        result_label.config(text='Error')
        first_number = None
        operator = None
        waiting_for_new_number = False
        decimal_used = False

def get_result():
    global first_number, operator, waiting_for_new_number, decimal_used
    try:
        if operator is None or first_number is None:
            update_status('Nothing to calculate')
            return

        current_text = result_label['text']
        if current_text == '':
            update_status('Enter a number before pressing "="')
            return

        second_number = float(current_text)
        result = calculate(first_number, operator, second_number)
        if isinstance(result, str):
            update_status(result)
            result_label.config(text='Error')
        else:
            str_result = str(result)
            if '.' in str_result:
                str_result = str_result.rstrip('0').rstrip('.')
            result_label.config(text=str_result)
            update_status('Calculation complete')

        first_number = None
        operator = None
        waiting_for_new_number = True
        decimal_used = False
    except ValueError:
        update_status('Invalid input')
        result_label.config(text='Error')
        first_number = None
        operator = None
        waiting_for_new_number = False
        decimal_used = False

def on_keypress(event):
    if event.char.isdigit():
        get_digit(event.char)
    elif event.char in '+-*/':
        get_operator(event.char)
    elif event.char == '.':
        get_decimal()
    elif event.keysym == 'Return':
        get_result()
    elif event.keysym == 'BackSpace':
        backspace()
    elif event.keysym == 'Escape':
        clear()

root = Tk()
root.title('Friendly Calculator')
root.geometry('340x500')
root.resizable(0, 0)
root.configure(background='#222')

# Display label
result_label = Label(root, text='0', bg='#222', fg='white', font=('Verdana', 32, 'bold'), anchor='e')
result_label.grid(row=0, column=0, columnspan=4, sticky='we', padx=10, pady=(20, 10))

# Status label for hints/errors
status_label = Label(root, text='Welcome! Enter your calculation.', bg='#222', fg='#aaa', font=('Verdana', 10), anchor='w')
status_label.grid(row=1, column=0, columnspan=4, sticky='we', padx=10)

# Button specs for better UX colors
btn_params = {'bg': '#333', 'fg': 'white', 'font': ('Verdana', 16), 'width': 5, 'height': 2, 'activebackground': '#555', 'activeforeground': 'white'}

buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 4, 3),
    ('C', 5, 0), ('0', 5, 1), ('.', 5, 2), ('/', 5, 3),
    ('⌫', 6, 0), ('=', 6, 1, 3),
]

for btn in buttons:
    text = btn[0]
    row = btn[1]
    col = btn[2]
    colspan = btn[3] if len(btn) > 3 else 1

    if text.isdigit():
        action = lambda t=text: get_digit(t)
    elif text == 'C':
        action = clear
    elif text == '=':
        action = get_result
    elif text == '.':
        action = get_decimal
    elif text == '⌫':
        action = backspace
    else:
        # Fix late binding issue in lambda
        action = lambda t=text: get_operator(t)

    b = Button(root, text=text, command=action, **btn_params)
    b.grid(row=row, column=col, columnspan=colspan, sticky='we', padx=5, pady=5)

root.bind('<Key>', on_keypress)

root.mainloop()

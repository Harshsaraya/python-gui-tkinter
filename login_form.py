from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os

def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email == 'harsh@gmail.com' and password == '1234':
        messagebox.showinfo('Yayyy', 'Login Successful')
    else:
        messagebox.showerror('Error', 'Login Failed')

root = Tk()
root.title('Login Form')

try:
    root.iconbitmap('favicon.ico')
except Exception:
    pass

root.geometry('350x500')
root.configure(background='#0096DC')

# Image loading with safety check
image_path = r'C:\Users\harsh\OneDrive\Desktop\Parul\Projects\python-gui-tkinter\flipkart-logo.png'

if os.path.exists(image_path):
    img = Image.open(image_path)
    resized_img = img.resize((70, 70))
    img = ImageTk.PhotoImage(resized_img)

    img_label = Label(root, image=img)
    img_label.pack(pady=(10, 10))
else:
    img_label = Label(root, text='[Logo Missing]', bg='#0096DC', fg='white', font=('verdana', 12))
    img_label.pack(pady=(10, 10))

text_label = Label(root, text='Flipkart', fg='white', bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana', 24))

email_label = Label(root, text='Enter Email', fg='white', bg='#0096DC')
email_label.pack(pady=(20, 5))
email_label.config(font=('verdana', 12))

email_input = Entry(root, width=50)
email_input.pack(ipady=6, pady=(1, 15))

password_label = Label(root, text='Enter Password', fg='white', bg='#0096DC')
password_label.pack(pady=(20, 5))
password_label.config(font=('verdana', 12))

password_input = Entry(root, width=50, show='*')  # masked password
password_input.pack(ipady=6, pady=(1, 15))

login_btn = Button(root, text='Login Here', bg='white', fg='black', width=20, height=2, command=handle_login)
login_btn.pack(pady=(10, 20))
login_btn.config(font=('verdana', 10))

root.mainloop()

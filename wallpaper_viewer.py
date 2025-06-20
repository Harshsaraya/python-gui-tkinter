from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os

def rotate_image():
    global counter
    if img_array:
        counter = (counter + 1) % len(img_array)
        img_label.config(image=img_array[counter])

counter = 0
img_array = []

root = Tk()
root.title('Wallpaper Viewer')
root.geometry('250x400')
root.configure(background='black')

# Use absolute path for wallpapers directory
wallpaper_dir = r'C:\Users\harsh\OneDrive\Desktop\Parul\Projects\python-gui-tkinter\wallpapers'

if not os.path.exists(wallpaper_dir):
    messagebox.showerror("Error", f"Directory '{wallpaper_dir}' not found.")
    root.destroy()
else:
    files = [f for f in os.listdir(wallpaper_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    for file in files:
        try:
            img_path = os.path.join(wallpaper_dir, file)
            img = Image.open(img_path)
            resized_img = img.resize((200, 300))
            img_array.append(ImageTk.PhotoImage(resized_img))
        except Exception as e:
            continue

    if not img_array:
        messagebox.showinfo("No Images", "No valid images found in the 'wallpapers' folder.")
        root.destroy()
    else:
        img_label = Label(root, image=img_array[0])
        img_label.pack(pady=(15, 10))

        next_btn = Button(root, text='Next', bg='white', fg='black', width=28, height=2, command=rotate_image)
        next_btn.pack()
        root.mainloop()

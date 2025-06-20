Tkinter GUI Projects Collection
This repository contains three separate Python GUI applications built using Tkinter and other libraries such as PIL (Pillow). Each project demonstrates different GUI features and functionalities.

1. Friendly Calculator (calculator.py)
Description
A simple yet user-friendly calculator app with basic arithmetic operations (+, -, *, /). It supports decimal numbers, backspace, clear, and keyboard input. Results are displayed with clean formatting, and errors such as division by zero are handled gracefully.

Features
Addition, subtraction, multiplication, and division

Decimal input support

Backspace functionality to delete last digit

Keyboard shortcuts: numbers, operators, Enter for equals, Backspace, Escape to clear

Status bar for hints and error messages

Responsive buttons with hover effects and styling

How to Run
bash
Copy
Edit
python calculator.py
Dependencies
Python 3.x

Tkinter (usually included with Python)

2. Login Form (login_form.py)
Description
A simple login form GUI simulating user authentication. Includes email and password fields, with masked password input. Upon submission, checks hardcoded credentials and shows success or failure messageboxes.

Features
Input fields for email and password (password masked)

Login button

Logo image display (adjust the image path as needed)

Uses Tkinter message boxes for feedback

Custom window styling with colors and fonts

How to Run
bash
Copy
Edit
python login_form.py
Dependencies
Python 3.x

Tkinter (usually included with Python)

Pillow (pip install pillow) for image handling

Notes
Update the image_path variable to point to your local logo image.

The valid credentials are hardcoded as:

Email: harsh@gmail.com

Password: 1234

3. Wallpaper Viewer (wallpaper_viewer.py)
Description
A basic wallpaper viewer that cycles through images from a specified directory. Users can click the "Next" button to rotate through available wallpapers displayed in the window.

Features
Loads all valid image files (png, jpg, jpeg, gif, bmp) from a given folder

Resizes images to fit the viewer window

Cycles through images on button click

Error handling for missing directory or no valid images

How to Run
bash
Copy
Edit
python wallpaper_viewer.py
Dependencies
Python 3.x

Tkinter (usually included with Python)

Pillow (pip install pillow) for image processing

Notes
Change the wallpaper_dir variable to your local wallpapers folder path.

Make sure the folder contains valid image files.

General Notes
All projects use Tkinter and rely on the Pillow library for image-related functionality.

To install Pillow:

bash
Copy
Edit
pip install pillow
Tested on Windows, but should work on Linux/macOS with minor path adjustments.

Ensure you have the appropriate images and directories as per the code comments.

If you have any questions or need help running these projects, feel free to ask!


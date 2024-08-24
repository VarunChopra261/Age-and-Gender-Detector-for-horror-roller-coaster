# import tkinter as tk
# from tkinter import Label, filedialog
# from tkinter import *
# from PIL import Image, ImageTk
# import numpy as np
# from keras.models import load_model
# import pandas as pd
# from datetime import datetime
# import cv2

# # Loading the model
# model = load_model("Age_Gender_Detection.keras")

# # Initializing the GUI
# top = tk.Tk()
# top.geometry('800x600')
# top.title("Age and Gender Detector")
# top.configure(background="#CDCDCD")

# # Initializing the Labels (1 for age and 1 for gender)
# label1 = Label(top, background="#CDCDCD", font=("arial", 15, "bold"))
# label2 = Label(top, background="#CDCDCD", font=("arial", 15, "bold"))
# sign_image = Label(top)

# # Designing Detect function which detects the age and gender of the person in image using the model
# def Detect(file_path):
#     global label_packed
#     image = Image.open(file_path)
#     image = image.resize((48, 48))
#     image = np.expand_dims(image, axis=0)
#     image = np.array(image)
#     image = np.delete(image, 0, 1)
#     image = np.resize(image, (48, 48, 3))
#     print(image.shape)
#     sex_f = ["Male", "Female"]
#     image = np.array(image) / 255
#     pred = model.predict(np.array([image]))
#     age = int(np.round(pred[1][0]))
#     sex = int(np.round(pred[0][0]))
#     print("Predicted Age is " + str(age))
#     print("Predicted Gender is " + sex_f[sex])
#     label1.configure(foreground="#011638", text=f"Predicted Age: {age}")
#     label2.configure(foreground="#011638", text=f"Predicted Gender: {sex_f[sex]}")
#     label1.pack(side="bottom", expand=True)
#     label2.pack(side="bottom", expand=True)
    
#     # Load image with OpenCV
#     img = cv2.imread(file_path)
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
#     # Draw rectangle and message if age is less than 13 or greater than 60
#     if age < 13 or age > 60:
#         cv2.rectangle(img, (10, 10), (img.shape[1]-10, img.shape[0]-10), (255, 0, 0), 2)
#         cv2.putText(img, "Not allowed", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    
#     # Convert image to display in tkinter
#     img = Image.fromarray(img)
#     img = img.resize((250, 250), Image.ANTIALIAS)
#     img = ImageTk.PhotoImage(img)
#     sign_image.configure(image=img)
#     sign_image.image = img
    
#     # Store data in CSV
#     entry_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     data = {'Age': [age], 'Gender': [sex_f[sex]], 'Entry Time': [entry_time]}
#     df = pd.DataFrame(data)
#     df.to_csv('entry_data.csv', mode='a', header=False, index=False)

# # Defining Show_detect button function 
# def show_Detect_button(file_path):
#     global Detect_b
#     if 'Detect_b' in globals():
#         Detect_b.pack_forget()  # Remove the previous button if it exists
#     Detect_b = Button(button_frame, text="Detect Image", command=lambda: Detect(file_path), padx=10, pady=5)
#     Detect_b.configure(background="#364156", foreground="white", font=("arial", 10, "bold"))
#     Detect_b.pack(side="bottom", pady=20)

# # Defining Upload Image function
# def upload_image():
#     try:
#         file_path = filedialog.askopenfilename()
#         uploaded = Image.open(file_path)
#         uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
#         im = ImageTk.PhotoImage(uploaded)
#         sign_image.configure(image=im)
#         sign_image.image = im
#         label1.configure(text='')
#         label2.configure(text='')
#         show_Detect_button(file_path)
#     except Exception as e:
#         print(f"Error: {e}")

# # Creating a frame to hold the buttons and labels
# button_frame = Frame(top, background="#CDCDCD")
# button_frame.pack(side="bottom", fill="x", pady=20)

# upload = Button(button_frame, text="Upload an image", command=upload_image, padx=10, pady=5)
# upload.configure(background="#364156", foreground="white", font=("arial", 10, "bold"))
# upload.pack(side="bottom", pady=20)
# sign_image.pack(side="bottom", expand=True)
# label1.pack(side="bottom", expand=True)
# label2.pack(side="bottom", pady=20, expand=True)
# heading = Label(top, text="Age and Gender Detector", pady=15, font=("arial", 15, "bold"))
# heading.configure(background="#CDCDCD", foreground="#364156")
# heading.pack()
# top.mainloop()

import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
from keras.models import load_model
import pandas as pd
from datetime import datetime
import cv2
import os

# Loading the model
model = load_model("Age_Gender_Detection.keras")

# Initializing the GUI
top = tk.Tk()
top.geometry('800x600')
top.title("Age and Gender Detector")
top.configure(background="#CDCDCD")

# Initializing the Labels (1 for age and 1 for gender)
label1 = Label(top, background="#CDCDCD", font=("arial", 15, "bold"))
label2 = Label(top, background="#CDCDCD", font=("arial", 15, "bold"))
sign_image = Label(top)

# Designing Detect function which detects the age and gender of the person in image using the model
def Detect(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((48, 48))
    image = np.expand_dims(image, axis=0)
    image = np.array(image)
    image = np.delete(image, 0, 1)
    image = np.resize(image, (48, 48, 3))
    print(image.shape)
    sex_f = ["Male", "Female"]
    image = np.array(image) / 255
    pred = model.predict(np.array([image]))
    age = int(np.round(pred[1][0]))
    sex = int(np.round(pred[0][0]))
    print("Predicted Age is " + str(age))
    print("Predicted Gender is " + sex_f[sex])
    label1.configure(foreground="#011638", text=f"Predicted Age: {age}")
    label2.configure(foreground="#011638", text=f"Predicted Gender: {sex_f[sex]}")
    label1.pack(side="bottom", expand=True)
    label2.pack(side="bottom", expand=True)
    
    # Load image with OpenCV
    img = cv2.imread(file_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Draw rectangle and message if age is less than 13 or greater than 60
    if age < 13 or age > 60:
        cv2.rectangle(img, (10, 10), (img.shape[1]-10, img.shape[0]-10), (255, 0, 0), 2)
        cv2.putText(img, "Not allowed", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    
    # Convert image to display in tkinter
    img = Image.fromarray(img)
    img = img.resize((250, 250), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    sign_image.configure(image=img)
    sign_image.image = img
    
    # Store data in CSV
    entry_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {'Age': [age], 'Gender': [sex_f[sex]], 'Entry Time': [entry_time]}
    df = pd.DataFrame(data)
    if not os.path.isfile('entry_data.csv'):
        df.to_csv('entry_data.csv', mode='a', header=True, index=False)
    else:
        df.to_csv('entry_data.csv', mode='a', header=False, index=False)

# Defining Show_detect button function 
def show_Detect_button(file_path):
    global Detect_b
    if 'Detect_b' in globals():
        Detect_b.pack_forget()  # Remove the previous button if it exists
    Detect_b = Button(button_frame, text="Detect Image", command=lambda: Detect(file_path), padx=10, pady=5)
    Detect_b.configure(background="#364156", foreground="white", font=("arial", 10, "bold"))
    Detect_b.pack(side="bottom", pady=20)

# Defining Upload Image function
def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label1.configure(text='')
        label2.configure(text='')
        show_Detect_button(file_path)
    except Exception as e:
        print(f"Error: {e}")

# Function to display the CSV file contents
def display_csv():
    try:
        if not os.path.isfile('entry_data.csv'):
            raise FileNotFoundError("CSV file not found.")
        df = pd.read_csv('entry_data.csv', header=None, names=['Age', 'Gender', 'Entry Time'])
        csv_window = Toplevel(top)
        csv_window.title("CSV Data")
        csv_window.geometry("400x400")
        text = Text(csv_window)
        text.pack(expand=True, fill='both')
        text.insert(END, df.to_string(index=False))
    except Exception as e:
        print(f"Error: {e}")

# Creating a frame to hold the buttons and labels
button_frame = Frame(top, background="#CDCDCD")
button_frame.pack(side="bottom", fill="x", pady=20)

upload = Button(button_frame, text="Upload an image", command=upload_image, padx=10, pady=5)
upload.configure(background="#364156", foreground="white", font=("arial", 10, "bold"))
upload.pack(side="bottom", pady=20)

display_csv_button = Button(button_frame, text="Display CSV Data", command=display_csv, padx=10, pady=5)
display_csv_button.configure(background="#364156", foreground="white", font=("arial", 10, "bold"))
display_csv_button.pack(side="bottom", pady=20)

sign_image.pack(side="bottom", expand=True)
label1.pack(side="bottom", expand=True)
label2.pack(side="bottom", pady=20, expand=True)
heading = Label(top, text="Age and Gender Detector", pady=15, font=("arial", 15, "bold"))
heading.configure(background="#CDCDCD", foreground="#364156")
heading.pack()
top.mainloop()
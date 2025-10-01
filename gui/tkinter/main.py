# basic graphical user interface using python

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

app = tk.Tk()
app.configure(background="white")
app.geometry("800x600")
app.resizable(False, False)
app.title("Twenty-Four-Seven")

USER_NAME = tk.StringVar()
USER_AGE = tk.StringVar()


def submit_function():
    showinfo(title="Info", message=f"{USER_NAME.get()} is {USER_AGE.get()} years old.")


# create frame
input_frame = ttk.Frame(app)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# create componenents
label_name = ttk.Label(input_frame, text="Name")
label_name.pack(padx=10, fill="x", expand=True)

input_name = ttk.Entry(input_frame, textvariable=USER_NAME)
input_name.pack(padx=10, pady=10, fill="x", expand=True)

label_age = ttk.Label(input_frame, text="Age")
label_age.pack(padx=10, fill="x", expand=True)

input_age = ttk.Entry(input_frame, textvariable=USER_AGE)
input_age.pack(padx=10, pady=10, fill="x", expand=True)

submit_button = ttk.Button(input_frame, text="Submit", command=submit_function)
submit_button.pack(padx=10, pady=10, fill="x", expand=True)

app.mainloop()

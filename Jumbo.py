import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.font import *

root = tk.Tk()
root.title("Jumbo - Text Editor")
root.geometry("884x568")

# Declaring Action Button Spot / Frame
action_buttons = tk.Frame()
action_buttons.grid(column=1, row=1)

# Action Buttons & Functions

root_font = Font(
    family="Helvetica",
    size="14",
    weight="bold",
    slant="roman",
    overstrike="0",
    underline="0",
)

# Save File
def savefile():
    file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[
        ("Text File", ".txt"),
        ("Batch File", ".batch"),
        ("Executable File", ".exe"),
        ("C++ File", ".cpp"),
        ("C File", ".c"),
        ("Sass css File", ".scss"),
        ("Json File", ".json"),
        ("Javascript File", ".js"),
        ("HTML File", ".html"),
        ("CSS File", ".css"),
        ("Python File", ".py"),
        ("All Files", ".*"),
    ])

    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()


save_btn = tk.Button(action_buttons, text="Save", fg="white", bg="green", font=root_font, command=savefile)
save_btn.grid(column=1, row=1)
save_btn.bind("<Shift-s>", savefile)

# Open File
def openfile():
    filepath = filedialog.askopenfilename(title="Open a File In Jumbo Text Editor")
    filee = open(filepath, 'r')
    textoftheopenedfile = filee.read()
    text.delete(1.0, END)
    text.insert(1.0, textoftheopenedfile)
    filee.close()


open_btn = tk.Button(action_buttons, text="Open", fg="white", bg="blue", font=root_font, command=openfile)
open_btn.grid(column=2, row=1)

# Text Area

text = tk.Text(fg="white", bg="#09001c", font=root_font)
text.config(insertbackground="yellow")
text.grid(column=1, row=2)

# Mainloop
root.mainloop()
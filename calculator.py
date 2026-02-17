import tkinter as tk
import math

# Create main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x550")
root.resizable(False, False)
root.configure(bg="#309e69")   # Dark background

# Entry box
entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, 
                 justify="right", bg="#475850", fg="white")
entry.grid(row=0, column=0, columnspan=5, pady=10)

# Function to insert value
def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Scientific functions
def sin():
    try:
        value = float(entry.get())
        result = math.sin(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.insert(tk.END, "Error")

def cos():
    try:
        value = float(entry.get())
        result = math.cos(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.insert(tk.END, "Error")

def tan():
    try:
        value = float(entry.get())
        result = math.tan(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.insert(tk.END, "Error")

def sqrt():
    try:
        value = float(entry.get())
        result = math.sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.insert(tk.END, "Error")

def log():
    try:
        value = float(entry.get())
        result = math.log10(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.insert(tk.END, "Error")

# Button layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3), ('C',1,4),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3), ('√',2,4),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3), ('log',3,4),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3), ('sin',4,4),
    ('cos',5,0), ('tan',5,1)
]

for (text, row, col) in buttons:
    
    # Default style
    bg_color = "#776F6F"
    fg_color = "white"

    # Special button colors
    if text in ['+', '-', '*', '/']:
        bg_color = "#ff9500"   # Orange operators
    elif text == "=":
        bg_color = "#1a8232"   # Green equal
    elif text == "C":
        bg_color = "#dc3545"   # Red clear
    elif text in ["sin", "cos", "tan", "log", "√"]:
        bg_color = "#007acc"   # Blue scientific

    # Button command mapping
    if text == "=":
        cmd = calculate
    elif text == "C":
        cmd = clear
    elif text == "sin":
        cmd = sin
    elif text == "cos":
        cmd = cos
    elif text == "tan":
        cmd = tan
    elif text == "√":
        cmd = sqrt
    elif text == "log":
        cmd = log
    else:
        cmd = lambda t=text: click(t)

    tk.Button(root, text=text, width=6, height=2,
              bg=bg_color, fg=fg_color,
              font=("Arial", 12, "bold"),
              command=cmd).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()

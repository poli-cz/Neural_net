import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()
# the input dialog
number = simpledialog.askstring(title="Test", prompt="What's your number?:")
number1 = int(number)
# check it out
for i in range(number1):
    print(i)

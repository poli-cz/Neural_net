import tkinter as tk
# Let's create the Tkinter window.
window = tk.Tk()
window.title("Neural net gui")


def some_fce():
    input()

def some_other_fce():
    print("hell")

top_frame = tk.Frame(window, width=1000, height=1000).pack()
bottom_frame = tk.Frame(window).pack(side = "bottom")

btn1 = tk.Button(top_frame, text = "Run calculations", fg = "green", height=3, width=12, command=some_fce).place(x=5, y=5)
btn2 = tk.Button(top_frame, text = "Stop calculations", fg = "red", height=3, width=12, command=some_other_fce).place(x=5, y=65)

window.mainloop()

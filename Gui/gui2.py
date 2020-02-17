import tkinter
# Let's create the Tkinter window.
window = tkinter.Tk()
window.title("Neural net gui")

# You will first create a division with the help of Frame class and align them on TOP and BOTTOM with pack() method.
top_frame = tkinter.Frame(window, width=500, height=500).pack()
bottom_frame = tkinter.Frame(window).pack(side = "bottom")

# Once the frames are created then you are all set to add widgets in both the frames.
btn1 = tkinter.Button(top_frame, text = "Run calculations", fg = "green", height=3, width=12).place(x=5, y=5)

btn2 = tkinter.Button(top_frame, text = "Stop calculations", fg = "red", height=3, width=12).place(x=5, y=65)




window.mainloop()

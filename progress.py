from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import simpledialog

root = Tk()
root1 = tk.Tk()

root1.withdraw()
USER_INP = simpledialog.askstring(title="Iter",
                                  prompt="Number of iter?")
USER_INP = int(USER_INP)
progress = Progressbar(root, orient = HORIZONTAL,
			length = 100, mode = 'determinate')

def bar():
	import time

	for i in range(0, USER_INP):
		if i == USER_INP:
			pass
		else:
			progress['value'] = int(i)
			root.update_idletasks()
			time.sleep(0.1)

def stop():
	root.withdraw()

progress.pack(pady = 10)

Button(root, text = 'Start', command = bar).pack(pady = 100)
Button(root, text = 'Close', command = stop).pack(pady = 100)

mainloop()

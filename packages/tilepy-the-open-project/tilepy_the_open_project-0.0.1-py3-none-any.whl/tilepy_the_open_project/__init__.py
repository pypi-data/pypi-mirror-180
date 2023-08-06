import tkinter as gui

window = None

def create_window(window_title):
	window = gui.Tk()
	window.title(window_title)
	window["bg"] = "#111133"
	window.mainloop()

def text(text):
	e = gui.Label(window)
	e.configure(text=text)
	e.pack()
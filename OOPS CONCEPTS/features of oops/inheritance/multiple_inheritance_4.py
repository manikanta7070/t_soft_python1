import tkinter as tk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()

class MyFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

app = MyApp()
frame = MyFrame(app)
app.mainloop()

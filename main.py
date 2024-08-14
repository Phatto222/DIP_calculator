import tkinter as tk

class MyCalculator:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x400")
        self.root.title("My Calculator")

        self.label = tk.Label(self.root, text="Calculator", font=('Arial', 18))
        self.label.pack()
        
        self.button = tk.Button(self.root, text="1", width=6, height=3)
        self.button.place(x=20, y=140)
        
        self.button = tk.Button(self.root, text="2", width=6, height=3)
        self.button.place(x=80, y=140)

        self.button = tk.Button(self.root, text="3", width=6, height=3)
        self.button.place(x=140, y=140)

        self.button = tk.Button(self.root, text="4", width=6, height=3)
        self.button.place(x=20, y=200)

        self.button = tk.Button(self.root, text="5", width=6, height=3)
        self.button.place(x=80, y=200)

        self.button = tk.Button(self.root, text="6", width=6, height=3)
        self.button.place(x=140, y=200)

        self.button = tk.Button(self.root, text="7", width=6, height=3)
        self.button.place(x=20, y=260)

        self.button = tk.Button(self.root, text="8", width=6, height=3)
        self.button.place(x=80, y=260)

        self.button = tk.Button(self.root, text="9", width=6, height=3)
        self.button.place(x=140, y=260)

        self.button = tk.Button(self.root, text="0", width=6, height=3)
        self.button.place(x=80, y=320)

        self.button = tk.Button(self.root, text="/", width=6, height=3)
        self.button.place(x=200, y=80)

        self.button = tk.Button(self.root, text="x", width=6, height=3)
        self.button.place(x=200, y=140)

        self.button = tk.Button(self.root, text="-", width=6, height=3)
        self.button.place(x=200, y=200)

        self.button = tk.Button(self.root, text="+", width=6, height=3)
        self.button.place(x=200, y=260)

        self.button = tk.Button(self.root, text="=", width=6, height=3)
        self.button.place(x=200, y=320)

        self.root.mainloop()

MyCalculator() 
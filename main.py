import tkinter as tk

class MyCalculator:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x400")
        self.root.title("My Calculator")

        self.label = tk.Label(self.root, text="Calculator", font=('Arial', 18))
        self.label.pack()
        
        self.button = tk.Button(self.root, text="1", width=8, height=4)
        self.button.place(x=20, y=80)
        
        self.button = tk.Button(self.root, text="2", width=8, height=4)
        self.button.place(x=90, y=80)

        self.button = tk.Button(self.root, text="3", width=8, height=4)
        self.button.place(x=160, y=80)

        self.button = tk.Button(self.root, text="4", width=8, height=4)
        self.button.place(x=20, y=160)

        self.button = tk.Button(self.root, text="5", width=8, height=4)
        self.button.place(x=90, y=160)

        self.button = tk.Button(self.root, text="6", width=8, height=4)
        self.button.place(x=160, y=160)

        self.button = tk.Button(self.root, text="7", width=8, height=4)
        self.button.place(x=20, y=240)

        self.button = tk.Button(self.root, text="8", width=8, height=4)
        self.button.place(x=90, y=240)

        self.button = tk.Button(self.root, text="9", width=8, height=4)
        self.button.place(x=160, y=240)

        self.root.mainloop()

MyCalculator() 
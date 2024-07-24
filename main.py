import tkinter as tk

class MyCalculator:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x400")
        self.root.title("My Calculator")

        self.label = tk.Label(self.root, text="Calculator", font=('Arial', 18))
        self.label.pack()
        
        self.button = tk.Button(self.root, text="1", width=6, height=6)
        self.button.place(x=20, y=80)
        
        self.button = tk.Button(self.root, text="Don't click", height=4)
        self.button.place(x=100, y=80)

        self.button = tk.Entry()
        self.button.place(x=80, y=40)

        self.root.mainloop()

MyCalculator() 
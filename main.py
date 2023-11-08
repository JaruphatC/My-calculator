import tkinter as tk

class mycalculator:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x300")
        self.root.title("My Calculator")
        self.label = tk.Label(self.root, text="HWD1", font=('Arel',50))
        self.label.pack()
        self.button = tk.Button(self.root, text="00000")
        self.button.place(x=0,y=0)
        self.root.mainloop()
        
mycalculator()
from tkinter import *
from tkinter import ttk
from file_organizer import Organizer
from ttkthemes import ThemedTk


class Application(Organizer):
    def __init__(self):
        super().__init__()
        self.instruction_label = "Enter path of folder you would like organized: \nEx: Mac OS -> /Users/Guest/Downloads"
        self.window = ThemedTk(theme="itft1", themebg=True, fonts=True)
        self.window.title("File Organizer")
        self.window.config(padx=10, pady=10)
        self.frame = ttk.Frame(padding="5")
        self.entry = ttk.Entry(width=30)
        self.entry.grid(column=1, row=0)
        self.instruction = ttk.Label(text=self.instruction_label, padding=10)
        self.instruction.grid(column=0, row=0)
        self.enter_btn = ttk.Button(text="Enter", padding=10, command=self.call_organizer)
        self.enter_btn.grid(column=0, row=1)
        self.quit_btn = ttk.Button(text="Quit", padding=10, command=self.frame.quit)
        self.quit_btn.grid(column=1, row=1)
        self.window.mainloop()

    def get_txt(self):
        source = self.entry.get()
        print(f"Function Successful {source} Retrieved.")
        return source

    def call_organizer(self):
        Organizer.organizer(self, self.get_txt())
        print(f"Organization of {self.get_txt()} Complete.")

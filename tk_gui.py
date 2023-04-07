"""
tk_gui.py
Creates a user input textbox and uses it to interact with gpt.
"""

import tkinter as tk
from gpt_interaction import GptCom
from compile_run import execute

class TkGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x50")
        self.gc = GptCom()
        self.textbox = tk.Entry(self.root)
        self.textbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.textbox.bind('<Return>', self.process_text)

        self.root.mainloop()

    def process_text(self, event):
        text = self.textbox.get()
        print(text)
        self.textbox.delete(0, tk.END)
        output = self.gc.get_interaction(text)
        execute(output)

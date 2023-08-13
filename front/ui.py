from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

class DSAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Search DSA")

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f4f4f4')
        self.style.configure('TLabel', font=('Arial', 16), foreground='#333333')
        self.style.configure('TButton', font=('Arial', 14), foreground='black', background='#FA8072')
        self.style.configure('TButton:hover', background='#0056b3')

        self.container = ttk.Frame(root, padding=30)
        self.container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.container.columnconfigure(0, weight=1)

        self.title_label = ttk.Label(self.container, text="Enter Question")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        self.text_input = tk.Text(self.container, wrap=tk.WORD, width=40, height=10)
        self.text_input.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.submit_button = ttk.Button(self.container, text="Submit", command=self.submit)
        self.submit_button.grid(row=2, column=0, columnspan=2, pady=20)
        self.output_text = ""

    def submit(self):
        question_text = self.text_input.get("1.0", "end-1c")
        messagebox.showinfo('Question',f"{question_text} \n question_text")

if __name__ == "__main__":
    root = tk.Tk()
    app = DSAApp(root)
    root.mainloop()

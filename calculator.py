import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        self.expression = ""
        
        # Display
        self.display_var = tk.StringVar()
        self.display = tk.Entry(
            root, 
            textvariable=self.display_var, 
            font=("Arial", 24), 
            bd=10, 
            relief=tk.SUNKEN, 
            justify=tk.RIGHT
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
        
        # Button layout
        buttons = [
            ('C', 1, 0), ('±', 1, 1), ('%', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0, 2), ('.', 5, 2), ('=', 5, 3),
        ]
        
        # Configure grid weights
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        
        # Create buttons
        for btn in buttons:
            text = btn[0]
            row = btn[1]
            col = btn[2]
            colspan = btn[3] if len(btn) > 3 else 1
            
            if text in ['/', '*', '-', '+', '=']:
                bg_color = '#ff9500'
                fg_color = 'white'
            elif text in ['C', '±', '%']:
                bg_color = '#a5a5a5'
                fg_color = 'black'
            else:
                bg_color = '#333333'
                fg_color = 'white'
            
            button = tk.Button(
                root,
                text=text,
                font=("Arial", 18),
                bg=bg_color,
                fg=fg_color,
                activebackground=bg_color,
                command=lambda t=text: self.on_button_click(t)
            )
            button.grid(
                row=row, 
                column=col, 
                columnspan=colspan, 
                sticky="nsew", 
                padx=2, 
                pady=2
            )
    
    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display_var.set("")
        elif char == '=':
            self.calculate()
        elif char == '±':
            self.toggle_sign()
        elif char == '%':
            self.percentage()
        else:
            self.expression += char
            self.display_var.set(self.expression)
    
    def calculate(self):
        try:
            result = eval(self.expression)
            # Format result to avoid long decimals
            if isinstance(result, float):
                result = round(result, 10)
                if result == int(result):
                    result = int(result)
            self.display_var.set(str(result))
            self.expression = str(result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
            self.expression = ""
            self.display_var.set("")
        except Exception:
            messagebox.showerror("Error", "Invalid expression")
            self.expression = ""
            self.display_var.set("")
    
    def toggle_sign(self):
        if self.expression:
            try:
                value = eval(self.expression)
                value = -value
                self.expression = str(value)
                self.display_var.set(self.expression)
            except Exception:
                pass
    
    def percentage(self):
        if self.expression:
            try:
                value = eval(self.expression)
                value = value / 100
                self.expression = str(value)
                self.display_var.set(self.expression)
            except Exception:
                pass


def main():
    root = tk.Tk()
    Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()

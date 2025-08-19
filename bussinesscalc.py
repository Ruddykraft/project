import tkinter as tk
from tkinter import messagebox

def calc():
    try:
        fc = float(e1.get())   # Fixed cost
        vc = float(e2.get())   # Variable cost per unit
        sp = float(e3.get())   # Selling price per unit
        target_profit = float(e4.get())  # Desired profit

        if sp <= vc:
            messagebox.showerror("Error", "Selling price must be greater than variable cost to calculate break-even.")
            return
        
        # Break-even units
        be_units = fc / (sp - vc)
        
        # Units needed for target profit
        units_for_profit = (fc + target_profit) / (sp - vc)

        result_text = (
            f"Break-even Units: {be_units:.2f}\n"
            f"Units for Target Profit: {units_for_profit:.2f}"
        )
        result_label.config(text=result_text, fg="#2E8B57")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

root = tk.Tk()
root.title("Units Calculator")
root.geometry("1920x1080")
root.configure(bg="#f4f4f4")

title_label = tk.Label(root, text="📊 Break-even & Target Profit Calculator", font=("Helvetica", 20, "bold"), bg="#f4f4f4", fg="#333")
title_label.pack(pady=15)

tk.Label(root, text="Fixed Cost", font=("Arial", 16), bg="#f4f4f4").pack()
e1 = tk.Entry(root, font=("Arial", 24), width=20, bd=2, relief="solid", justify="center"); e1.pack(pady=5)

tk.Label(root, text="Variable Cost/Unit", font=("Arial", 16), bg="#f4f4f4").pack()
e2 = tk.Entry(root, font=("Arial", 24), width=20, bd=2, relief="solid", justify="center"); e2.pack(pady=5)

tk.Label(root, text="Selling Price/Unit", font=("Arial", 16), bg="#f4f4f4").pack()
e3 = tk.Entry(root, font=("Arial", 24), width=20, bd=2, relief="solid", justify="center"); e3.pack(pady=5)

tk.Label(root, text="Target Profit", font=("Arial", 16), bg="#f4f4f4").pack()
e4 = tk.Entry(root, font=("Arial", 24), width=20, bd=2, relief="solid", justify="center"); e4.pack(pady=5)

def on_enter(e):
    calc_btn.config(bg="#2E8B57", fg="white")

def on_leave(e):
    calc_btn.config(bg="#4CAF50", fg="white")

calc_btn = tk.Button(root, text="Calculate", font=("Arial", 20, "bold"), bg="#4CAF50", fg="white", padx=20, pady=10, command=calc, relief="flat")
calc_btn.pack(pady=15)
calc_btn.bind("<Enter>", on_enter)
calc_btn.bind("<Leave>", on_leave)

root.bind("<Return>", lambda event: calc())

result_label = tk.Label(root, text="", justify="left", font=("Arial", 22, "bold"), bg="#f4f4f4")
result_label.pack(pady=10)

root.mainloop()

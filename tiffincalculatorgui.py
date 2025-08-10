import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        fixed_cost = float(entry_fixed_cost.get())
        variable_cost = float(entry_variable_cost.get())
        selling_price = float(entry_selling_price.get())

        # Avoid division by zero
        if selling_price == variable_cost:
            messagebox.showerror("Error", "Selling price and variable cost cannot be equal.")
            return

        # Step 1: calculate n
        n = fixed_cost / (selling_price - variable_cost)

        # Step 2: calculate profit
        # profit = n * selling_price - (fixed_cost + n * variable_cost)

        # Display results
        label_result.config(
            text=(
                f"Number of tiffins (n): {n:.2f}\n"
                # f"Profit: ₹{profit:.2f}"
            )
        )
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create main window
root = tk.Tk()
root.title("Tiffin Cost & Profit Calculator")
root.geometry("900x600")  # Bigger window

# Title
tk.Label(root, text="Tiffin Cost & Profit Calculator", font=("Arial", 18, "bold")).pack(pady=15)

# Labels and Entry fields
tk.Label(root, text="Fixed Cost:", font=("Arial", 14)).pack(pady=5)
entry_fixed_cost = tk.Entry(root, font=("Arial", 14), width=20)
entry_fixed_cost.pack(pady=5)

tk.Label(root, text="Variable Cost per Tiffin:", font=("Arial", 14)).pack(pady=5)
entry_variable_cost = tk.Entry(root, font=("Arial", 14), width=20)
entry_variable_cost.pack(pady=5)

tk.Label(root, text="Selling Price per Tiffin:", font=("Arial", 14)).pack(pady=5)
entry_selling_price = tk.Entry(root, font=("Arial", 14), width=20)
entry_selling_price.pack(pady=5)

# Calculate button
tk.Button(root, text="Calculate", command=calculate, font=("Arial", 14), bg="lightblue", width=15).pack(pady=15)

# Result label
label_result = tk.Label(root, text="", font=("Arial", 20), fg="green")
label_result.pack(pady=15)

# Run application
root.mainloop()

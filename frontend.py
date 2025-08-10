import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def calculate():
    try:
        # Get inputs
        n1 = int(entry_students.get())
        w1 = int(entry_students_water.get())
        n2 = int(entry_sweepers.get())
        w2 = int(entry_sweepers_water.get())
        n3 = int(entry_gardeners.get())
        w3 = int(entry_gardeners_water.get())
        cost_per_litre = float(entry_cost.get())

        # Daily usage
        daily_students = n1 * w1
        daily_sweepers = n2 * w2
        daily_gardeners = n3 * w3
        total_daily = daily_students + daily_sweepers + daily_gardeners

        # Monthly calculations
        monthly_usage = total_daily * 30
        monthly_cost = monthly_usage * cost_per_litre
        required_budget = monthly_cost + (0.20 * monthly_cost)

        # Output
        result_usage.config(text=f"Total monthly usage: {monthly_usage} litres")
        result_cost.config(text=f"Total monthly cost: ₹{monthly_cost:.2f}")
        result_budget.config(text=f"Required budget: ₹{required_budget:.2f}")

        # Clear old chart
        for widget in chart_frame.winfo_children():
            widget.destroy()

        # Create pie chart
        fig = Figure(figsize=(4, 4), dpi=100)
        ax = fig.add_subplot(111)
        values = [daily_students, daily_sweepers, daily_gardeners]
        labels = ["Students", "Sweepers", "Gardeners"]
        colors = ["#4CAF50", "#2196F3", "#FFC107"]
        ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90, colors=colors)
        ax.set_title("Daily Water Usage Distribution")

        # Embed in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers in all fields.")

# Main window
root = tk.Tk()
root.title("School Water Budget Calculator")
root.geometry("500x800")
root.config(bg="#eaf4f4")

# Title
tk.Label(root, text="School Water Budget Calculator", font=("Arial", 16, "bold"), bg="#eaf4f4").pack(pady=10)

# Input fields
def make_label_entry(text):
    tk.Label(root, text=text, bg="#eaf4f4").pack()
    entry = tk.Entry(root)
    entry.pack()
    return entry

entry_students = make_label_entry("Number of students:")
entry_students_water = make_label_entry("Water used per student (litres/day):")
entry_sweepers = make_label_entry("Number of sweepers:")
entry_sweepers_water = make_label_entry("Water used per sweeper (litres/day):")
entry_gardeners = make_label_entry("Number of gardeners:")
entry_gardeners_water = make_label_entry("Water used per gardener (litres/day):")
entry_cost = make_label_entry("Cost of water per litre (₹):")

# Calculate button
tk.Button(root, text="Calculate", command=calculate, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=15)

# Results
result_usage = tk.Label(root, text="", font=("Arial", 12), bg="#eaf4f4")
result_usage.pack()

result_cost = tk.Label(root, text="", font=("Arial", 12), bg="#eaf4f4")
result_cost.pack()

result_budget = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#eaf4f4")
result_budget.pack()

# Frame for chart
chart_frame = tk.Frame(root, bg="#eaf4f4")
chart_frame.pack(pady=20)

root.mainloop()

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        weight_unit=weight_unit_value.get()
        height_unit=height_unit_value.get()
        if weight_unit=="lbs":
            weight=weight*0.453592
        if height_unit=="cm":
            height=height/100
        elif height_unit=="ft":
            height=height*0.3048
        if height>0:
    
            bmi = weight / (height ** 2)
            if bmi<18.5:
                message="You are underweight"
            elif bmi > 18.5 and bmi < 24.9:
                message="You are normal weight, congrats."
            elif bmi > 25.5 and bmi < 29.9:
                message="You are overweight"
            else:
                message="You are obese, be careful. Work out more."
            entry_BMI.delete(0, tk.END)  # Clear the BMI entry box
            entry_BMI.insert(0, f"{bmi:.2f} {message}")  # Display BMI with two decimal places
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for weight and height.")


window = tk.Tk()
window.geometry("300x400")
window.config(bg="cyan")
window.title("BMI Calculator")
weight_unit_value=tk.StringVar(value="kg")
height_unit_value=tk.StringVar(value="cm")
label_weight = tk.Label(window, text="Weight in KG")
label_weight.pack(pady=5)
entry_weight = tk.Entry(window)
entry_weight.pack(pady=5)
weight_menu=ttk.OptionMenu(window, weight_unit_value, "kg", "kg", "lbs")
weight_menu.pack(pady=5)
label_height = tk.Label(window, text="Height in CM")
label_height.pack(pady=5)
entry_height = tk.Entry(window)
entry_height.pack(pady=5)
height_menu=ttk.OptionMenu(window, height_unit_value, "cm", "cm", "ft")
button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
button.pack(pady=5)
height_menu.pack(pady=5)

label_BMI = tk.Label(window, text="Your BMI")
label_BMI.pack(pady=5)
entry_BMI = tk.Entry(window, width=40)
entry_BMI.pack(pady=5)

window.mainloop()
import tkinter as tk
from tkinter import messagebox

def total_amount():
    try:
        apples = int(apple_entry.get())
        oranges = int(orange_entry.get())

        cost_apple = 20  
        cost_orange = 25  

        total_apple_cost = apples * cost_apple
        total_orange_cost = oranges * cost_orange
        total_cost = total_apple_cost + total_orange_cost

        messagebox.showinfo("Summary", 
            f"The {apples} apple you ordered will cost {total_apple_cost} pesos while the {oranges} orange you ordered will cost {total_orange_cost} pesos\n"
            f"\n"
            f"In total, you owe {total_cost} pesos")

    except ValueError:
        messagebox.showerror("Reminder!", "Please enter your desired amount of apples and oranges.")

root = tk.Tk()
root.title("Program 2")
root.geometry("300x200")
root.configure(bg="light blue")
root.resizable(False, False)

font_style = ("Times New Roman", 12)

apple_label = tk.Label(root, text="Desired amount of Apples:", font=font_style, bg="light blue")
apple_label.pack(pady=5)
apple_entry = tk.Entry(root, font=font_style)
apple_entry.pack(pady=5)

orange_label = tk.Label(root, text="Desired amount of Oranges:", font=font_style, bg="light blue")
orange_label.pack(pady=5)
orange_entry = tk.Entry(root, font=font_style)
orange_entry.pack(pady=5)

enter_button = tk.Button(root, text="Enter", command=total_amount, font=font_style)
enter_button.pack(pady=10)

root.mainloop()
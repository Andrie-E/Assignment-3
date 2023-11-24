import tkinter as tk
from tkinter import messagebox

def cash_and_apple_price():
    try:
        cash = float(cash_entry.get())
        apple_cost = float(price_entry.get())

        max_apples = int(cash // apple_cost)
        remaining_cash = cash - (max_apples * apple_cost)

        messagebox.showinfo("Summary",
            f"If you have {cash} pesos and try to buy the apples at {apple_cost} then the merchant will give you {max_apples} apples.\n" 
            f"\n"
            f"If you decide to buy the apples, you will have {remaining_cash:.2f} pesos as your change.")

    except ValueError:
        messagebox.showerror("Reminder!", "Please state the amount of cash you have and how much would you like to purchase the apples.")

root = tk.Tk()
root.title("Program 3")
root.geometry("300x200")
root.configure(bg="black")

font_style = ("Times New Roman", 12)
font_color = "white"

cash_label = tk.Label(root, text="How much cash do you have?", font=font_style, fg=font_color, bg="black")
cash_label.pack(pady=5)
cash_entry = tk.Entry(root, font=font_style)
cash_entry.pack(pady=5)

price_label = tk.Label(root, text="How much would you like to buy the apples?:", font=font_style, fg=font_color, bg="black")
price_label.pack(pady=5)
price_entry = tk.Entry(root, font=font_style)
price_entry.pack(pady=5)

enter_button = tk.Button(root, text="Enter", command=cash_and_apple_price, font=font_style)
enter_button.pack(pady=10)

root.mainloop()
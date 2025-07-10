import tkinter as tk
from tkinter import ttk, messagebox, filedialog

stock_prices = {
    "Apple (AAPL)": 180,
    "Tesla (TSLA)": 250,
    "Google (GOOGL)": 2800,
    "Microsoft (MSFT)": 330,
    "Amazon (AMZN)": 140
}

portfolio = {}

def add_stock():
    selected = stock_menu.get()
    quantity = quantity_entry.get()

    if not selected or selected not in stock_prices:
        messagebox.showerror("Error", "Please select a valid stock.")
        return

    if not quantity.isdigit():
        messagebox.showerror("Error", "Please enter a valid quantity.")
        return

    quantity = int(quantity)
    portfolio[selected] = portfolio.get(selected, 0) + quantity
    update_display()

def update_display():
    result_text.delete(1.0, tk.END)
    total = 0
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total += value
        result_text.insert(tk.END, f"{stock}: {qty} x ${price} = ${value}\n")
    result_text.insert(tk.END, f"\nTotal Investment: ${total}")

def save_to_file():
    total = sum(stock_prices[stock] * qty for stock, qty in portfolio.items())
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if filename:
        with open(filename, "w") as file:
            for stock, qty in portfolio.items():
                value = stock_prices[stock] * qty
                file.write(f"{stock}: {qty} x ${stock_prices[stock]} = ${value}\n")
            file.write(f"\nTotal Investment: ${total}")
        messagebox.showinfo("Saved", "Summary saved successfully!")

root = tk.Tk()
root.title("Stock Portfolio Tracker")

tk.Label(root, text="Select Stock:").grid(row=0, column=0, padx=5, pady=5)
stock_menu = ttk.Combobox(root, values=list(stock_prices.keys()), state="readonly")
stock_menu.grid(row=0, column=1)

tk.Label(root, text="Quantity:").grid(row=1, column=0, padx=5, pady=5)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=1, column=1)

tk.Button(root, text="Add Stock", command=add_stock).grid(row=2, column=0, columnspan=2, pady=10)
tk.Button(root, text="Save Summary", command=save_to_file).grid(row=3, column=0, columnspan=2)

result_text = tk.Text(root, height=15, width=45)
result_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

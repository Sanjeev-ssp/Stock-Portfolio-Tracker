# 📊 Stock Portfolio Tracker (GUI Version)

A GUI-based stock portfolio tracker built with Python's `tkinter` library. It allows users to calculate and save their stock investments using dropdowns and entry fields.

## ✅ Features

- 📈 Predefined list of popular stock symbols (AAPL, TSLA, GOOGL, MSFT, AMZN)
- 🔽 Dropdown menu to select stock (no typing required)
- 🔢 Input field to enter quantity of shares
- 💰 Calculates total investment value
- 💾 Option to save result to a `.txt` file
- 🖱️ Simple, interactive interface with clear layout

## 📷 How It Looks

Select stock: [ AAPL ▼ ]  
Enter quantity: [   5   ]  
[ Calculate ] [ Save to File ]

Result: You have invested ₹12345 in AAPL.


## ▶️ How to Run

Make sure you have **Python 3** installed.

Open terminal or VS Code and run:

```bash
python stock_tracker_gui.py

🧠 Concepts Used
1. tkinter for GUI design
2. ttk.Combobox for dropdown selection
3. Dictionaries for stock-price mapping
4. Input validation and error handling
5. File dialog for saving results

🧾 Requirements
Python 3.x

No external libraries needed (only standard library)

📂 File Structure
Copy
Edit
stock_tracker_gui/
├── stock_tracker_gui.py
└── README.md

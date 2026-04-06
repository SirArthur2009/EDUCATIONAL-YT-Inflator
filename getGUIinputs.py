import tkinter as tk
from tkinter import ttk, messagebox
from urllib.parse import urlparse

def is_valid_url(url):
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])

def submit_gui(default_url=""):
    result = {"data": None}

    def on_submit():
        url = entry_url.get()
        number = entry_number.get()
        choice = yes_no_var.get()

        if not is_valid_url(url):
            messagebox.showerror("Error", "Invalid URL")
            return

        try:
            number_val = float(number)
            if number_val <= 0:
                raise ValueError
        except:
            messagebox.showerror("Error", "Enter a positive number")
            return

        result["data"] = [url, number_val, choice] # type: ignore
        root.destroy()

    root = tk.Tk()
    root.title("Input Form")
    root.geometry("780x300")  # 👈 bigger window

    # Style
    style = ttk.Style()
    style.configure("TLabel", font=("Segoe UI", 11))
    style.configure("TButton", font=("Segoe UI", 11))
    style.configure("TEntry", font=("Segoe UI", 11))

    frame = ttk.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)

    # URL
    ttk.Label(frame, text="URL:").grid(row=0, column=0, sticky="w", pady=5)
    entry_url = ttk.Entry(frame, width=40)
    entry_url.grid(row=0, column=1, pady=5)
    entry_url.insert(0, default_url or "https://example.com")

    # Number
    ttk.Label(frame, text="Views:").grid(row=1, column=0, sticky="w", pady=5)
    entry_number = ttk.Entry(frame, width=20)
    entry_number.grid(row=1, column=1, pady=5, sticky="w")
    entry_number.insert(0, "1")

    # Yes/No (checkbox)
    yes_no_var = tk.BooleanVar(value=True)
    ttk.Checkbutton(frame, text="Does it start Paused?", variable=yes_no_var)\
        .grid(row=2, column=1, sticky="w", pady=10)

    # Button
    ttk.Button(frame, text="Submit", command=on_submit)\
        .grid(row=3, column=0, columnspan=2, pady=15)

    root.mainloop()
    return result["data"]
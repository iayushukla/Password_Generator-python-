import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    password += random.choices(characters, k=length-4)
    random.shuffle(password)
    return ''.join(password)

def generate():
    try:
        length = int(length_entry.get())
        number = int(number_entry.get())
        
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return
        
        passwords = [generate_password(length) for _ in range(number)]
        result_text.delete(1.0, tk.END)
        for password in passwords:
            result_text.insert(tk.END, password + "\n")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for length and quantity.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg='black')

# Apply a style
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", font=("Helvetica", 10), background='black', foreground='white')
style.configure("TButton", font=("Helvetica", 10), background='black', foreground='white')
style.configure("TEntry", font=("Helvetica", 10), fieldbackground='black', foreground='white')
style.configure("TFrame", background='black')
style.configure("TText", background='black', foreground='white')

# Create and place the widgets
header_label = ttk.Label(root, text="Password Generator", font=("Helvetica", 16), style="TLabel")
header_label.pack(pady=10)

frame = ttk.Frame(root, padding="10 10 10 10", style="TFrame")
frame.pack(fill=tk.BOTH, expand=True)

number_label = ttk.Label(frame, text="Number of Passwords:", style="TLabel")
number_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
number_entry = ttk.Entry(frame, style="TEntry")
number_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)

length_label = ttk.Label(frame, text="Length of Passwords:", style="TLabel")
length_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
length_entry = ttk.Entry(frame, style="TEntry")
length_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)

generate_button = ttk.Button(frame, text="Generate", command=generate, style="TButton")
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_text = tk.Text(frame, height=10, wrap=tk.WORD, bg='black', fg='white', insertbackground='white')
result_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky=tk.EW)

frame.columnconfigure(1, weight=1)

# Run the application
root.mainloop()

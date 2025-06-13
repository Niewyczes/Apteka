import tkinter as tk
from tkinter import ttk
import pandas as pd
import os
from datetime import datetime
import requests
from PIL import Image, ImageTk

# Główne okno
root = tk.Tk()
root.title("Apteka")
root.geometry("1100x700")
root.configure(bg="white")

style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 10))
style.configure("TButton", font=("Segoe UI", 10))
style.configure("TEntry", font=("Segoe UI", 10))

# Tło
url = 'https://www.sentimed.pl/wp-content/uploads/2018/05/Fotolia_45326423_XL.jpg'
img_path = "tabletki.jpg"
if not os.path.exists(img_path):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(img_path, 'wb') as f:
            f.write(r.content)

bg_img = Image.open(img_path).resize((1100, 700))
bg_photo = ImageTk.PhotoImage(bg_img)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.lower()

# ====================== SEKJA: DODAJ LEK ======================
frame_dodaj = ttk.LabelFrame(root, text="Dodanie leku", padding=15)
frame_dodaj.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

ttk.Label(frame_dodaj, text="Nazwa:").grid(row=0, column=0)
entry_nazwa = ttk.Entry(frame_dodaj)
entry_nazwa.grid(row=0, column=1, padx=5)

ttk.Label(frame_dodaj, text="Recepta:").grid(row=0, column=2)
entry_recepta = ttk.Entry(frame_dodaj)
entry_recepta.grid(row=0, column=3, padx=5)

ttk.Label(frame_dodaj, text="Ilość:").grid(row=0, column=4)
entry_ilosc = ttk.Entry(frame_dodaj)
entry_ilosc.grid(row=0, column=5, padx=5)

def dodaj_lek():
    nazwa = entry_nazwa.get()
    recepta = entry_recepta.get()
    ilosc = entry_ilosc.get()
    filepath = "drugs.xlsx"

    if os.path.exists(filepath):
        df = pd.read_excel(filepath)
    else:
        df = pd.DataFrame(columns=["ID", "DRUG", "ON_RECEPT", "NO_PACKAGES_AVAILABLE", "DATE"])

    new_id = 1 if df.empty else df["ID"].max() + 1
    current_date = datetime.now().strftime("%Y-%m-%d")

    nowy_lek = {
        "ID": new_id,
        "DRUG": nazwa,
        "ON_RECEPT": recepta,
        "NO_PACKAGES_AVAILABLE": ilosc,
        "DATE": current_date
    }

    filepath = "drugs.xlsx"
    df = pd.read_excel(filepath) if os.path.exists(filepath) else pd.DataFrame(
        columns=["ID", "DRUG", "ON_RECEPT", "NO_PACKAGES_AVAILABLE", "DATE"]
    )

    new_id = 1 if df.empty else df["ID"].max() + 1
    new_row = {
        "ID": new_id,
        "DRUG": nazwa,
        "ON_RECEPT": recepta,
        "NO_PACKAGES_AVAILABLE": ilosc,
        "DATE": datetime.now().strftime("%Y-%m-%d")
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_excel(filepath, index=False)

    entry_nazwa.delete(0, tk.END)
    entry_recepta.delete(0, tk.END)
    entry_ilosc.delete(0, tk.END)

ttk.Button(frame_dodaj, text="Dodaj", command=dodaj_lek).grid(row=0, column=6, padx=10)

# ====================== SEKJA: USUŃ LEK ======================
frame_usun = ttk.LabelFrame(root, text="Usunięcie leku", padding=15)
frame_usun.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

usun_var = tk.IntVar(value=1)

ttk.Radiobutton(frame_usun, text="Po ID", variable=usun_var, value=1).grid(row=0, column=0)
entry_id = ttk.Entry(frame_usun)
entry_id.grid(row=0, column=1, padx=5)

ttk.Radiobutton(frame_usun, text="Po nazwie", variable=usun_var, value=2).grid(row=0, column=2)
entry_nazwa_usun = ttk.Entry(frame_usun)
entry_nazwa_usun.grid(row=0, column=3, padx=5)

def usun_lek():
    filepath = "drugs.xlsx"
    if not os.path.exists(filepath): return

    df = pd.read_excel(filepath)

    if usun_var.get() == 1:
        try:
            id_val = int(entry_id.get())
            df = df[df["ID"] != id_val]
        except ValueError:
            return
    elif usun_var.get() == 2:
        nazwa = entry_nazwa_usun.get().strip().lower()
        df = df[df["DRUG"].str.lower() != nazwa]

    df.to_excel(filepath, index=False)
    entry_id.delete(0, tk.END)
    entry_nazwa_usun.delete(0, tk.END)

ttk.Button(frame_usun, text="Usuń", command=usun_lek).grid(row=0, column=4, padx=10)

# ====================== SEKJA: REJESTRACJA ======================
frame_rejestracja = ttk.LabelFrame(root, text="Rejestracja użytkownika", padding=15)
frame_rejestracja.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

labels = ["Imię i Nazwisko", "Email", "Telefon", "Ulica", "Miasto", "Państwo"]
entries = {}

for i, label in enumerate(labels):
    ttk.Label(frame_rejestracja, text=f"{label}:").grid(row=0, column=i)
    entry = ttk.Entry(frame_rejestracja, width=15)
    entry.grid(row=1, column=i, padx=3)
    entries[label] = entry

ttk.Button(frame_rejestracja, text="Rejestruj").grid(row=1, column=len(labels), padx=10)

# ====================== START GUI ======================
root.mainloop()
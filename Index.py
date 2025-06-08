import tkinter as tk
from tkinter import *
import requests
import pandas as pd
from PIL import Image, ImageTk
import os
from datetime import datetime,timedelta
from tkinter import messagebox, simpledialog
import random,string
HASLO_ADMIN="BigPharma123!"
okno = Tk() # tworzenie głównego okna
okno.title("Apteka") # tytuł okna
okno.geometry("1200x600") # rozmiar okna

#TŁO
url1 = 'https://www.sentimed.pl/wp-content/uploads/2018/05/Fotolia_45326423_XL.jpg'
response = requests.get(url1, stream=True)
if response.status_code == 200:
    with open("tabletki.jpg", 'wb') as f:
        f.write(response.content)

bg_image = Image.open("tabletki.jpg")
bg_image = bg_image.resize((700, 500))  # dopasuj do okna
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = Label(okno, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.image = bg_photo  # zapobiega usunięciu z pamięci

# Funkcja dodająca lek do pliku Excel

def dodaj_lek():
    nazwa = NazwaEntry.get()
    recepta = ReceptaEntry.get()
    ilosc = IloscEntry.get()

    # Ścieżka do pliku
    filepath = "drugs.xlsx"

    # Wczytaj dane
    if os.path.exists(filepath):
        df = pd.read_excel(filepath)
    else:
        df = pd.DataFrame(columns=["ID", "DRUG", "ON_RECEPT", "NO_PACKAGES_AVAILABLE", "DATE"])

    # Ustal nowe ID
    if df.empty:
        new_id = 1
    else:
        new_id = df["ID"].max() + 1

    # Bieżąca data
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Nowy wiersz
    nowy_lek = {
        "ID": new_id,
        "DRUG": nazwa,
        "ON_RECEPT": recepta,
        "NO_PACKAGES_AVAILABLE": ilosc,
        "DATE": current_date
    }

    # Dodaj i zapisz
    df = pd.concat([df, pd.DataFrame([nowy_lek])], ignore_index=True)
    df.to_excel(filepath, index=False)

    # Czyść pola
    NazwaEntry.delete(0, END)
    ReceptaEntry.delete(0, END)
    IloscEntry.delete(0, END)

def usun_lek():
    filepath = "drugs.xlsx"

    if not os.path.exists(filepath):
        return  # nie ma pliku – nic do usuwania

    df = pd.read_excel(filepath)

    if var.get() == 1:  # Usuwanie po ID
        try:
            id_do_usuniecia = int(ID.get())
            df = df[df["ID"] != id_do_usuniecia]
        except ValueError:
            return  # nieprawidłowy ID (np. puste lub litery)

    elif var.get() == 2:  # Usuwanie po nazwie
        nazwa = NazwaDoUsuniecia.get().strip().lower()
        df = df[df["DRUG"].str.lower() != nazwa]

    df.to_excel(filepath, index=False)

    # Wyczyść pola
    ID.delete(0, END)
    NazwaDoUsuniecia.delete(0, END)

###Tworzenie pliku z historią leków pacjenta
def utworz_txt_DATABASE(identyfikator,ImieINazwisko):
    os.makedirs("DATABASE",exist_ok=True)
    plik_txt=f"DATABASE/{identyfikator}.txt"
    text=(f"Historia zamówień dla {identyfikator} , {ImieINazwisko}\n")
    with open(plik_txt, "w", encoding="utf-8") as f:
        f.write(text)

def rejestruj_uzytkownika():
    try:
        imie_nazwisko = ImieINazwisko.get().strip()
        email = Email.get().strip()
        telefon = Telefon.get().strip()
        ulica = Ulica.get().strip()
        miasto = Miasto.get().strip()
        panstwo = Panstwo.get().strip()
        ## Sprawdzenie czy są tylko litery z uwzględnioną spacją pomiędzy imieniem i nazwiskiem
        if not imie_nazwisko.replace(" "," ").isalpha():
            messagebox.showerror("Błąd", "Imię i Nazwisko muszą zawierać tylko litery!")
            return
        ## Sprawdzenie telefonu czy zawiera same cyfry i ma długość 9
        if not telefon.isdigit():
            messagebox.showerror("Błąd","Telefon musi zawierać tylko liczby")
            return
        if len(telefon) !=9:
            messagebox.showerror("Błąd","Numer musi zawierać 9 cyfr!")
            return
        # Sprawdzenie czy pola są wypełnione
        if not all([imie_nazwisko, email, telefon, ulica, miasto, panstwo]):
            messagebox.showerror("Uwaga", "Uzupełnij wszystkie pola.")
            return
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd: {e}")
        return
    try:
        # Ścieżki do plików
        customer_file = "customer.csv"
        address_file = "address.csv"

        # Wczytanie lub utworzenie DataFrame
        if os.path.exists(customer_file):
            df_customer = pd.read_csv(customer_file)
        else:
            df_customer = pd.DataFrame(columns=["ID", "NAME", "E-MAIL", "PHONE", "CREATED", "UPDATED"])

        if os.path.exists(address_file):
            df_address = pd.read_csv(address_file)
        else:
            df_address = pd.DataFrame(columns=["ID", "STREET", "CITY", "COUNTRY"])

        # Nadanie nowego ID
        if df_customer.empty and df_address.empty:
            new_id = 1
        else:
            new_id = max(
                df_customer["ID"].max() if not df_customer.empty else 0,
                df_address["ID"].max() if not df_address.empty else 0
            ) + 1

        # Data rejestracji
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Dodanie do DataFrame'ów
        new_customer = {
            "ID": new_id,
            "NAME": imie_nazwisko,
            "E-MAIL": email,
            "PHONE": telefon,
            "CREATED": now,
            "UPDATED": now
        }

        new_address = {
            "ID": new_id,
            "STREET": ulica,
            "CITY": miasto,
            "COUNTRY": panstwo
        }

        df_customer = pd.concat([df_customer, pd.DataFrame([new_customer])], ignore_index=True)
        df_address = pd.concat([df_address, pd.DataFrame([new_address])], ignore_index=True)

        # Zapis do plików CSV
        df_customer.to_csv(customer_file, index=False)
        df_address.to_csv(address_file, index=False)

        ##Wywołanie fukcji tworzącej plik z historią leków
        utworz_txt_DATABASE(new_id,imie_nazwisko)

        # Wyczyść pola
        ImieINazwisko.delete(0, END)
        Email.delete(0, END)
        Telefon.delete(0, END)
        Ulica.delete(0, END)
        Miasto.delete(0, END)
        Panstwo.delete(0, END)
        messagebox.showinfo("Sukces","Zarejestrowano użytkownika!")
    except Exception as e:
        messagebox.showerror("Błąd","Nie zapisano danych")

def usun_uzytkownika():
    customer_file = "customer.csv"
    address_file = "address.csv"

    if not os.path.exists(customer_file) or not os.path.exists(address_file):
        return  # pliki nie istnieją

    df_customer = pd.read_csv(customer_file)
    df_address = pd.read_csv(address_file)

    if var1.get() == 1:  # Usuwanie po ID
        try:
            id_do_usuniecia = int(IDUzytkownika.get())
            df_customer = df_customer[df_customer["ID"] != id_do_usuniecia]
            df_address = df_address[df_address["ID"] != id_do_usuniecia]
        except ValueError:
            return  # nieprawidłowe ID

    elif var1.get() == 2:  # Usuwanie po nazwie
        nazwa = NazwaDoUsunieciaUzytkownika.get().strip().lower()
        # Znajdź wszystkie ID użytkowników o tej nazwie
        ids_do_usuniecia = df_customer[df_customer["NAME"].str.lower() == nazwa]["ID"].tolist()
        df_customer = df_customer[~df_customer["ID"].isin(ids_do_usuniecia)]
        df_address = df_address[~df_address["ID"].isin(ids_do_usuniecia)]

    # Zapisz zmodyfikowane dane
    df_customer.to_csv(customer_file, index=False)
    df_address.to_csv(address_file, index=False)

    # Wyczyść pola
    IDUzytkownika.delete(0, END)
    NazwaDoUsunieciaUzytkownika.delete(0, END)

def edytuj_uzytkownika():
    customer_file = "customer.csv"
    address_file = "address.csv"

    if not os.path.exists(customer_file) or not os.path.exists(address_file):
        print("Brak plików customer.csv lub address.csv")
        return

    df_customer = pd.read_csv(customer_file)
    df_address = pd.read_csv(address_file)

    if var2.get() == 1:
        try:
            identyfikator = int(IDUzytkownikaZmiana.get())
        except ValueError:
            print("Nieprawidłowe ID.")
            return
    elif var2.get() == 2:
        nazwa = NazwaDoUsunieciaUzytkownikaZmiana.get().strip().lower()
        pasujace = df_customer[df_customer["NAME"].str.lower() == nazwa]
        if pasujace.empty:
            print("Nie znaleziono użytkownika o tej nazwie.")
            return
        identyfikator = pasujace.iloc[0]["ID"]
    else:
        print("Nie wybrano sposobu identyfikacji.")
        return

    # Dane nowe
    nowe_imie = ImieINazwiskoZmiana.get().strip()
    nowy_email = EmailZmiana.get().strip()
    nowy_telefon = TelefonZmiana.get().strip()
    nowa_ulica = UlicaZmiana.get().strip()
    nowe_miasto = MiastoZmiana.get().strip()
    nowe_panstwo = PanstwoZmiana.get().strip()

    teraz = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Aktualizacja danych
    df_customer.loc[df_customer["ID"] == identyfikator, ["NAME", "E-MAIL", "PHONE", "UPDATED"]] = [
        nowe_imie, nowy_email, nowy_telefon, teraz
    ]
    df_address.loc[df_address["ID"] == identyfikator, ["STREET", "CITY", "COUNTRY"]] = [
        nowa_ulica, nowe_miasto, nowe_panstwo
    ]

    # Zapis
    df_customer.to_csv(customer_file, index=False)
    df_address.to_csv(address_file, index=False)

    # Czyszczenie pól
    for entry in [IDUzytkownikaZmiana, NazwaDoUsunieciaUzytkownikaZmiana,
                  ImieINazwiskoZmiana, EmailZmiana, TelefonZmiana,
                  UlicaZmiana, MiastoZmiana, PanstwoZmiana]:
        entry.delete(0, END)
###funkcja która otwiera nowe okno i prosi o dane do recepty
def wystaw_receptę():
    ####Wymagane hasło żeby móc wystawiać recepty
    haslo=simpledialog.askstring("Uwaga","Podaj hasło:")
    if haslo !=HASLO_ADMIN:
        messagebox.showerror("Błąd","Złe hasło")
        return
    ###utworzenie nowego okna
    okno_recepta=Toplevel(okno)
    okno_recepta.title("Dodaj receptę")
    okno_recepta.geometry("300x200")
    Label(okno_recepta,text="Podaj ID pacjenta:").grid(row=0,column=0)
    IDEntry=Entry(okno_recepta)
    IDEntry.grid(row=0,column=1)
    Label(okno_recepta,text="Podaj leki, oddziel przecinkiem:").grid(row=1,column=0)
    LekiEntry=Entry(okno_recepta)
    LekiEntry.grid(row=2,column=0)
    ###dodanie fukcji która dodaje recepte
    def dodaj_receptę():
        ID_uzytkownika=IDEntry.get().strip()
        leki=LekiEntry.get().strip()
        ###Sprawdzenie czy są uzupełnione pola
        if not ID_uzytkownika or not leki:
            messagebox.showerror("Błąd","Proszę uzupłnić dane")
            return
        ##Generowanie 8 znakowego kodu recepty z  dużych liter i liczb
        kod_recepty=""
        for _ in range(8):
            kod_recepty +=random.choice(string.ascii_uppercase+string.digits)
        plik_recepty='recepty.xlsx'
        ###Dodanie dat wystawienia i ważności
        data_wystawienia=datetime.now()
        data_waznosci=data_wystawienia+timedelta(days=30)
        ##Dodanie wpisu do pliku recepty excel
        dodaj_wpis={
            "ID": ID_uzytkownika,
            "leki": leki,
            "kod_recepty": kod_recepty,
            "Data wystawienia":data_wystawienia.strftime("%Y-%m-%d %H:%M:%S"),
            "Ważna do":data_waznosci.strftime("%Y-%m-%d %H:%M:%S")
        }
        try:
            try:
                df=pd.read_excel(plik_recepty)
            except FileNotFoundError:
                ###jeśli nie istnieje plik tworzy nowy
                df=pd.DataFrame(columns=["ID", "leki", "kod_recepty","Data wystawienia","Ważna do"])
            df=pd.concat([df,pd.DataFrame([dodaj_wpis])],ignore_index=True)
            df.to_excel(plik_recepty,index=False)
            messagebox.showinfo("Udało się",f"Recepta dodana: {kod_recepty}")
            IDEntry.delete(0, END)
            LekiEntry.delete(0, END)
        except Exception as e:
            messagebox.showerror("Błąd","Nie udało się wystawić recepty!")
    Button(okno_recepta,text="Dodaj receptę",command=dodaj_receptę).grid(row=3,column=1)
def dodanie_historii_leków(nazwa,ilosc,recepta,data_zakupu,data_waznosci,id):
    plik_txt=f"DATABASE/{id}.txt"
    text = (f"Zakupiono lek {nazwa} w ilości {ilosc} na receptę: {recepta} zakupiony:{data_zakupu} ważny do: {data_waznosci}\n")
    with open(plik_txt, "a", encoding="utf-8") as f:
        f.write(text)

def zakup_lek():
    nazwa_leku = NazwaLeku.get().strip()
    ID_uzytkownika = IDZmnienna.get().strip()
    ilosc_zamowienie=Ilosc.get().strip()
    ##dodanie obsługi błędów
    if not all([nazwa_leku, ID_uzytkownika,ilosc_zamowienie]):
        messagebox.showerror("Błąd","Muszą być uzupełnione wszystkie pola")
    try:
        # zamiana stringa na int
        ilosc_zamowienie = int(ilosc_zamowienie)
    except ValueError:
        messagebox.showerror("Błąd","Musi być podana liczba całkowita")
        return
    df=pd.read_excel("drugs.xlsx")
    ##szukanie czy lek istnieje na liście
    lek=df[df["DRUG"]==nazwa_leku]
    if lek.empty:
        print("Nie ma takiego leku w bazie")
        return
    znaleziony_lek=lek.iloc[0].to_dict()
    modyfikowana_ilosc=lek.index[0]
    ilosc_na_stanie=int(znaleziony_lek["NO_PACKAGES_AVAILABLE"])

    ##sprawdzenie czy jest lek na stanie
    if ilosc_zamowienie>ilosc_na_stanie:
        print("Za mało na stanie!")
        return
    ##aktulizacja ilości w execelu
    df.loc[modyfikowana_ilosc,"NO_PACKAGES_AVAILABLE"]=ilosc_na_stanie-ilosc_zamowienie
    df.to_excel("drugs.xlsx",index=False)

    ####Dane znalezionego leku z "drugs.xlsx"
    nazwa=znaleziony_lek["DRUG"]
    recepta=znaleziony_lek["ON_RECEPT"]
    data_waznosci=znaleziony_lek["DATE"]
    data_zakupu=datetime.now().strftime("%Y-%m-%d")
    plik_txt = f"DATABASE/{ID_uzytkownika}.txt"
    ## wywołanie funkcji do zapisu zamówienia do txt
    dodanie_historii_leków(nazwa,ilosc_zamowienie,recepta,data_zakupu,data_waznosci,ID_uzytkownika)
    ###czyszczenie danych
    NazwaLeku.delete(0, END)
    IDZmnienna.delete(0, END)
    Ilosc.delete(0, END)

#Dodanie leku
Label(okno, text="Dodanie leku: ").grid(row=1, column=1)

Label(okno, text="Nazwa:").grid(row=2, column=1)
NazwaEntry = Entry(okno)
NazwaEntry.grid(row=2, column=2)

Label(okno, text="Recepta:").grid(row=2, column=3)
ReceptaEntry = Entry(okno)
ReceptaEntry.grid(row=2, column=4)

Label(okno, text="Ilość:").grid(row=2, column=5)
IloscEntry = Entry(okno)
IloscEntry.grid(row=2, column=6)

Button(okno , text = "Dodaj", command=dodaj_lek).grid(row = 2,column = 7)

# Usunięcie leku
LabelLeki = Label(okno, text="Usunięcie leku: ").grid(row=4, column=1)

var = IntVar()
Radiobutton(okno, text="ID:", variable=var, value=1).grid(row=5, column=1)
ID = Entry(okno)
ID.grid(row=5, column=2)

Radiobutton(okno, text="Nazwa:", variable=var, value=2).grid(row=5, column=3)
NazwaDoUsuniecia = Entry(okno)
NazwaDoUsuniecia.grid(row=5, column=4)

Button(okno, text="Usuń", command=usun_lek).grid(row=5, column=5)

#Rejestracja
Label(okno, text="Rejestracja: ").grid(row=6, column=1)

Label(okno, text="Imię i Nazwisko:").grid(row=7, column=1)
ImieINazwisko = Entry(okno,)
ImieINazwisko.grid(row=7, column=2)

Label(okno, text="Email:").grid(row=7, column=3)
Email = Entry(okno,)
Email.grid(row=7, column=4)

Label(okno, text="Telefon:").grid(row=7, column=5)
Telefon = Entry(okno,)
Telefon.grid(row=7, column=6)

Label(okno, text="Ulica:").grid(row=7, column=7)
Ulica = Entry(okno,)
Ulica.grid(row=7, column=8)

Label(okno, text="Miasto:").grid(row=7, column=9)
Miasto = Entry(okno,)
Miasto.grid(row=7, column=10)

Label(okno, text="Państwo:").grid(row=7, column=11)
Panstwo = Entry(okno,)
Panstwo.grid(row=7, column=12)

Button(okno , text = "Rejestruj", command=rejestruj_uzytkownika).grid(row = 7,column = 13)

# Usunięcie użytkownika
Label(okno, text="Usunięcie użytkownika: ").grid(row=8, column=1)
var1 = IntVar()

Radiobutton(okno, text="ID:", variable=var1, value=1).grid(row=9, column=1)
IDUzytkownika = Entry(okno)
IDUzytkownika.grid(row=9, column=2)

Radiobutton(okno, text="Nazwa:", variable=var1, value=2).grid(row=9, column=3)
NazwaDoUsunieciaUzytkownika = Entry(okno)
NazwaDoUsunieciaUzytkownika.grid(row=9, column=4)

Button(okno, text="Usuń", command=usun_uzytkownika).grid(row=9, column=5)

#Edycja użytkownika

Label(okno, text="Edycja użytkownika: ").grid(row=10, column=1)
var2 = IntVar()

Radiobutton(okno, text="ID:", variable=var2, value=1).grid(row=11, column=1)
IDUzytkownikaZmiana = Entry(okno)
IDUzytkownikaZmiana.grid(row=11, column=2)

Radiobutton(okno, text="Nazwa:", variable=var2, value=2).grid(row=11, column=3)
NazwaDoUsunieciaUzytkownikaZmiana = Entry(okno)
NazwaDoUsunieciaUzytkownikaZmiana.grid(row=11, column=4)

Label(okno, text="Imię i Nazwisko:").grid(row=12, column=1)
ImieINazwiskoZmiana = Entry(okno)
ImieINazwiskoZmiana.grid(row=12, column=2)

Label(okno, text="Email:").grid(row=12, column=3)
EmailZmiana = Entry(okno)
EmailZmiana.grid(row=12, column=4)

Label(okno, text="Telefon:").grid(row=12, column=5)
TelefonZmiana = Entry(okno)
TelefonZmiana.grid(row=12, column=6)

Label(okno, text="Ulica:").grid(row=12, column=7)
UlicaZmiana = Entry(okno)
UlicaZmiana.grid(row=12, column=8)

Label(okno, text="Miasto:").grid(row=12, column=9)
MiastoZmiana = Entry(okno)
MiastoZmiana.grid(row=12, column=10)

Label(okno, text="Państwo:").grid(row=12, column=11)
PanstwoZmiana = Entry(okno)
PanstwoZmiana.grid(row=12, column=12)

Button(okno, text="Zmień", command=edytuj_uzytkownika).grid(row=12, column=13)

###Zakup leku
Label(okno,text="Zamów lek: ").grid(row=13,column=1)
Label(okno, text="Nazwa leku: ").grid(row=14,column=1)
NazwaLeku=Entry(okno)
NazwaLeku.grid(row=14, column=2)
Label(okno,text="ID: ").grid(row=14, column=3)
IDZmnienna=Entry(okno)
IDZmnienna.grid(row=14, column=4)
Label(okno,text="Ilość: ").grid(row=14, column=5)
Ilosc=Entry(okno)
Ilosc.grid(row=14, column=6)
Button(okno, text="potwierdź",command=zakup_lek).grid(row=14,column=7)

###Wystawianie recepty
Label(okno,text="Funkcje administratora").grid(row=15,column=1)
Button(okno,text="Dodaj receptę",command=wystaw_receptę).grid(row=15,column=2)
#koniec okna
okno.mainloop() # generowanie obiektów okna
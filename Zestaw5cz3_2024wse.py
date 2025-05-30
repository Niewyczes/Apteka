from tkinter import *  # biblioteka do tworzenia interfejsu graficznego użytkownika
import requests
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

## Window

# okno = Tk() # tworzenie głównego okna
# okno.title("Moj interfejs uzytkownika 1") # tytuł okna
# okno.geometry("500x300") # rozmiar okna
# okno.mainloop() # generowanie obiektów okna

# url1 = 'https://www.druk-flag.pl/drukarnia-flag/wp-content/uploads/2019/05/4.jpeg'
# response = requests.get(url1, stream=True)
# if response.status_code == 200:
#     with open("sample.jpg", 'wb') as f:
#         f.write(response.content)

#### Window - tło

# okno = Tk()
# canvas = Canvas(okno, width=100, height=50)
# canvas.grid(columnspan=3)  # columnnspan - liczba kolumn którą obejmuje kontrolka
# image = Image.open('sample.jpg')
# logo = ImageTk.PhotoImage(image)
# logo_label = Label(image=logo)
# logo_label.image = logo
# logo_label.grid(row=0, column=0, rowspan = 10, columnspan= 10)

# text = Label(okno,
#             text="Ustaw parametr A = ",
#             fg="black",
#             font='Raleway')
# text.grid(row=0, column=0)
# okno.mainloop()

###### Kontrola pozycji kontrolek, inne warianty niż row/column
# okno = Tk()
# Label(okno, text="pack BOTTOM", bg="red", fg="white").pack(side=BOTTOM)
# Label(okno, text="pack TOp", bg="blue", fg="white").pack(side=TOP)
# okno.mainloop()

# okno = Tk()
# t = Label(okno, text="Position : padx=0, pady=20", bg="red", fg="white")
# t.pack(padx=0, pady=20, side=LEFT)
# okno.mainloop()

# okno = Tk()
# t = Label(okno, text="Position : x=10, y=0", bg="red", fg="white")
# t.place(x=10, y=0)
# mainloop()


################# Przykład - text edit, radiobutton
# def wynik():  # funkcja uruchamiana po wciśnieciu kontrolki radioButton
#   if var.get() == 1:
#     wynikDzialania = int(text1.get()) + int(text2.get())
#   if var.get() == 2:
#     wynikDzialania = int(text1.get()) - int(text2.get())
#   mojtekst = "Wynik działania to: " + str(wynikDzialania)
#   etykieta_text.config(
#     text=mojtekst)  # ustawienie tekstu w kontrolce o nazwie etykieta_text3


#
# okno = Tk()
# okno.title("Kalkulator")
# okno.geometry("400x200")

# var = IntVar()  # typ pobieranej zmiennej
# Label(okno, text="Wpisz pierwszą liczbę: ").grid(row=1, column=1)
# Label(okno, text="Wpisz drugą liczbę: ").grid(row=2, column=1)
# text1 = Entry(okno, fg='red')
# text1.grid(row=1, column=2)
# text2 = Entry(okno, fg='blue')
# text2.grid(row=2, column=2)
# Radiobutton(okno, text=" + ", variable=var, value=1).grid(row=1, column=3)
# Radiobutton(okno, text=" - ", variable=var, value=2).grid(row=2, column=3)
# etykieta_text = Label(okno, text="Wynik działania to: 0")
# etykieta_text.grid(row=3, column=1)
# Button(okno, text="Enter", command=wynik, fg="red").grid(row=4, column=1)
# okno.mainloop()

################# Przykład - slider
# def wyswietlWynik():
#    suma = var1.get() + var2.get()
#    wyswietlany_tekst = "A + B = " + str(suma)
#    text3.config(text = wyswietlany_tekst)

# okno = Tk()
# var1 = IntVar()
# var2 = IntVar()
# okno.geometry("400x200")
# text1 = Label(okno, text="Ustaw parametr A", bg="green", fg="white")
# text1.grid(row = 1,column = 1)
# suwak1 = Scale(okno, from_=0, to=100, orient=HORIZONTAL, variable = var1 )
# suwak1.grid(row = 2,column = 1)
# text2 = Label(okno, text="Ustaw parametr B", bg="red", fg="white")
# text2.grid(row = 3,column = 1)
# suwak2 = Scale(okno, from_=0, to=100, orient=HORIZONTAL, variable = var2)
# suwak2.grid(row = 4,column = 1)
# przycisk = Button(okno , text = "Suma", command = wyswietlWynik, fg="red")
# przycisk.grid(row = 5,column = 1)
# text3 = Label(okno, text=" ")
# text3.grid(row = 6,column = 1)
# okno.mainloop()

#####Przykład - Checkbox
# def call():   # funkcja uruchamiana po wciśnieciu kontrolki radioButton
#    if var1.get() == 1 and var2.get() == 0:
#     text.config(text = "lubie dawać prezenty") 
  
#    if var2.get() == 0 and var2.get() == 1:
#     text.config(text = "lubie dostawać prezenty")
  
#    if var2.get() == 1 and var2.get() == 1:
#     text.config(text = "lubie dawać i dostawać prezenty")


# okno = Tk()
# var1 = IntVar()   # możliwe typy np:StringVar(), IntVar(), BooleanVar()
# Checkbutton(okno, 
#             text="lubie dawać prezenty",
#             variable=var1,
#             command = call).grid(row=0, sticky=W, pady=4) # sticky = W - wyrównaj do lewej
# var2 = IntVar()
# Checkbutton(okno, 
#             text="lubie dostawać prezenty", 
#             variable=var2,
#             command = call).grid(row=1, sticky=W,pady=4) # pady=4 - odstęp równy 4 row nad/pod kontrolką

# text = Label(okno, text ="Wynik") 
# text.grid(row = 4,column = 1) #położenie kontrolki z tekstem statycznym


# okno.mainloop()

# Zapoznaj się z przykładami tworzenia okienek informacyjnych
# from tkinter.messagebox import showinfo, showerror, showwarning
# # przykład1
# def info():
#     showinfo("ShowInfo", "Hello World!")
# #
# okno = Tk()
# p = Button(okno, text = 'ok', command = info)
# p.grid(row = 1, column = 1)
# okno.mainloop()

# Przykład 2 - krótszy analog powyższego kodu 
# okno = Tk()
# Button(okno, text = 'ok', command = lambda :showinfo("Box:", 'info')).grid(row = 1, column = 1)
# okno.mainloop()

# # przykład 3 inne typy kontrolek
#  okno = Tk()
#  Button(okno, text = 'ok', command = lambda :showinfo("Box:", 'info')).grid(row = 1, column = 1)
# # Button(okno, text = 'ok', command = lambda :showerror("Box:", 'error')).grid(row = 2, column = 1)
# # Button(okno, text = 'ok', command = lambda :showwarning("Box:", 'warning')).grid(row = 3, column = 1)
#  okno.mainloop()

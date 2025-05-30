import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Wczytanie pliku CSV
df = pd.read_csv('drugs.csv')

# Ustawienie ziarna losowości dla powtarzalności wyników
np.random.seed(42)

# Generowanie losowych wartości dla kolumny NO_PACKAGES_AVAILABLE (od 10 do 500)
df['NO_PACKAGES_AVAILABLE'] = np.random.randint(10, 501, size=len(df))

# Definiowanie zakresu dat
start_date = datetime(2015, 1, 1)
end_date = datetime(2029, 5, 22)

# Obliczanie liczby dni między datami
delta_days = (end_date - start_date).days

# Generowanie losowych dat w formacie 'YYYY-MM-DD'
df['DATE'] = [
    (start_date + timedelta(days=np.random.randint(0, delta_days))).strftime('%Y-%m-%d')
    for _ in range(len(df))
]

# Zapisanie zmodyfikowanego pliku CSV
df.to_csv('drugs_filled.csv', index=False)

print("Plik 'drugs_filled.csv' został pomyślnie zapisany.")

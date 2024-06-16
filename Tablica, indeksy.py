import numpy as np

# Utworzenie tablicy a o wymiarach (3, 4, 8)
a = np.random.randint(0, 10, size=(3, 4, 8))

# Wyświetlenie tablicy a
print("Oryginalna tablica:")
print(a)
print("\nKształt:", a.shape)

# Wczytanie tablicy tidx od użytkownika
tidx = input("\nPodaj indeksy (tidx) oddzielone spacjami: ")
tidx = list(map(int, tidx.split()))

# Sprawdzenie długości tidx
if len(tidx) != a.shape[1]:
    raise ValueError("Tablica tidx musi mieć długość równą wymiarowi J (czyli 4).")

# Wybranie danych z pierwszego wymiaru (K) po indeksach tidx
result = np.array([a[tidx[j], j, :] for j in range(a.shape[1])])

# Wyświetlenie wynikowej tablicy
print("\nWynikowa tablica:")
print(result)
print("\nKształt:", result.shape)
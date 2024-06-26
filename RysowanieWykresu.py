import matplotlib.pyplot as plt

# Wczytanie nazwy pliku od użytkownika
filename = input("Podaj nazwę pliku tekstowego: ")

# Inicjalizacja list do przechowywania wartości x i y
x_values = []
y_values = []

# Wczytanie danych z pliku
try:
    with open(filename, 'r') as file:
        for line in file:
            # Rozdzielenie linii na wartości x i y
            x, y = map(float, line.split())
            x_values.append(x)
            y_values.append(y)
except FileNotFoundError:
    print("Plik nie został znaleziony.")
    exit()
except ValueError:
    print("Błąd w przetwarzaniu danych. Upewnij się, że plik zawiera liczby.")
    exit()

# Rysowanie wykresu liniowego
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')

# Dodanie tytułu i etykiet osi
plt.title("Wykres liniowy")
plt.xlabel("x")
plt.ylabel("y")

# Wyświetlenie wykresu
plt.show()
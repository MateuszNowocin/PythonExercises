import sys
import random
import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def load_and_preprocess_image(image_path):
    # Wczytanie obrazka
    img = Image.open(image_path)
    img = img.convert("L")  # Konwersja do skali szarości

    # Sprawdzenie rozmiaru obrazka
    if img.width < 5 or img.height < 5:
        raise ValueError("Obrazek musi mieć wymiary co najmniej 5x5 pikseli.")

    # Przycięcie do lewego górnego rogu 5x5 pikseli
    img_cropped = img.crop((0, 0, 5, 5))

    # Konwersja na czarno-biały (0 i 255)
    img_bw = img_cropped.point(lambda p: p > 128 and 255)

    # Konwersja wartości pikseli do zakresu 1 i -1
    img_array = np.array(img_bw)
    img_array = np.where(img_array == 255, -1, 1)

    return img_array.flatten()

# Wczytanie obrazka i przetworzenie
image_path = input("Podaj ścieżkę do pliku .png: ")
x = load_and_preprocess_image(image_path)
L = 5  # długość boku obrazka
N = L * L  # liczba neuronów
print(x.reshape(L, L))

# Hopfield Network code
time = 10  # czas symulacji
n = 2  # liczba wzorców do nauczenia
one = np.identity(N, dtype=np.int8)
w = np.zeros((N, N), dtype=np.int8)

pattern = []
pattern.append(np.array([-1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1]))  # A
pattern.append(np.array([1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1]))  # Z

# Etap uczenia
for mu in range(n):
    w += np.outer(pattern[mu], pattern[mu]) - one

# Etap symulacji (rozpoznawania wzorca)
for t in range(time):
    if t % 1 == 0:
        print(t * 100 / time, "%")
        plt.imshow(x.reshape(L, L), cmap=plt.cm.Greys_r, interpolation='none')
        plt.savefig(str('letter%03d' % t) + ".png", format="png")
    x = np.sign(np.dot(w, x))
    for i in range(N):
        if x[i] == 0:
            x[i] = 1
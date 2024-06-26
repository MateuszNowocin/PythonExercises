#!/usr/bin/env python
import sys
import random
import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

time = 10 # czas symulacji
L = 5 # dlugosc boku obrazka
N = L * L # liczba neuronow]]
n = 2 # liczba wzorcow do nauczenia
one = np.identity(N,dtype = np.int8)
w = np.zeros((N,N),dtype = np.int8)


def load_image(filename):
    img = Image.open(filename)
    img = img.convert('L')  # Konwersja na obrazek czarno-biały (grayscale)

    # Sprawdzenie rozmiarów obrazka
    width, height = img.size
    if width < L or height < L:
        raise ValueError("Obrazek jest za mały. Minimalny rozmiar to 5x5 pikseli.")

    # Przycinanie obrazka do rozmiaru 5x5 pikseli z lewego górnego rogu
    img_crop = img.crop((0, 0, L, L))
    img_conv = img_crop.point(lambda p: p > 128 and 255)

    # Konwersja obrazka do formatu zero-jeden
    img_array = np.array(img_conv)
    img_array = np.where(img_array == 255, -1, 1)  # Konwersja wartości pikseli 0-255 na 1 i -1

    return img_array.flatten()

# Wczytywanie obrazka do rozpoznania
if len(sys.argv) != 2:
    print("Usage: python Hopfield.py <image.png>")
    sys.exit(1)

image_filename = sys.argv[1]
x = load_image(image_filename)
print(x.reshape(L,L))

pattern = []
pattern.append(np.array([-1,1,1,1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,1,1,-1,-1,-1,1])) # A
pattern.append(np.array([1,1,1,1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,1,1])) # Z

# etap uczenia
for mu in range(n):
    w += np.outer(pattern[mu],pattern[mu]) - one

# etap symulacji (rozpoznawania wzorca)
for t in range(time):
    if (t % 1 == 0):
        print(t*100/time,"%")
        plt.imshow(x.reshape(L,L), cmap = plt.cm.Greys_r, interpolation = 'none')
        plt.savefig(str('letter%03d' % t)+".png", format="png")
    x = np.sign(np.dot(w,x))
    for i in range(N):
        if(x[i] == 0):
            x[i] = 1
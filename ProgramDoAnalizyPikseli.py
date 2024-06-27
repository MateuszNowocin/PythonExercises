import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

#Wczytuje obraz z pliku i konwertuje go z BGR do RGB
def load_image(file_name):
    try:
        img = cv2.imread(file_name)
        if img is None:
            raise FileNotFoundError
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    except Exception as e:
        print(f"Nie udało się załadować pliku o nazwie {file_name}. Błąd: {str(e)}")
        return None

# Oblicza statystyki kolorów dla podanego obrazu
def calculate_color_statistics(img):
    total_pixels = img.shape[0] * img.shape[1]
    red_pixels = np.sum((img[:, :, 0] > img[:, :, 1]) & (img[:, :, 0] > img[:, :, 2]))
    green_pixels = np.sum((img[:, :, 1] >= img[:, :, 0]) & (img[:, :, 1] >= img[:, :, 2]))
    blue_pixels = np.sum((img[:, :, 2] > img[:, :, 0]) & (img[:, :, 2] > img[:, :, 1]))
    gray_pixels = np.sum((img[:, :, 0] == img[:, :, 1]) & (img[:, :, 1] == img[:, :, 2]))

    return red_pixels, green_pixels, blue_pixels, gray_pixels, total_pixels

#Wypisuje statystyki kolorów dla obrazu
def print_statistics(file_name, red, green, blue, gray, total):
    print(f"Nazwa pliku obrazka: {file_name}")
    print(f"Liczba czerwonych pikseli: {red}")
    print(f"Liczba zielonych pikseli: {green}")
    print(f"Liczba niebieskich pikseli: {blue}")
    print(f"Liczba szarych pikseli: {gray}")
    print(f"Łączna liczba pikseli: {total}")

#Tworzy i wyświetla wykres kołowy, przedstawiający udział kolorów w obraziku
def plot_pie_chart(red, green, blue, gray):
    labels = ['Czerwone', 'Zielone', 'Niebieskie', 'Szare']
    sizes = [red, green, blue, gray]
    colors = ['red', 'green', 'blue', 'gray']

    plt.figure()  # Utworzenie nowego wykresu
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Udział kolorów w obrazku')
    plt.show(block=False)

#Program w pętli, tak długo jak nie wpiszemy exit, nie zakończy się

if __name__ == "__main__":
    while True:
        file_name = input("Podaj nazwę pliku obrazka (lub 'exit' aby zakończyć): ")

        if file_name.lower() == 'exit':
            print("Koniec programu.")
            break

        img = load_image(file_name)

        if img is not None:
            red, green, blue, gray, total = calculate_color_statistics(img)
            print_statistics(file_name, red, green, blue, gray, total)
            plot_pie_chart(red, green, blue, gray)

        print("\n")  # Dodanie pustej linii dla lepszej czytelności
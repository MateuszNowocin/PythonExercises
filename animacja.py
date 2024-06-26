import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle


def main():
    fig, ax = plt.subplots()
    # Generowanie wartości x od 0 do 2π z krokiem 0.01
    x = np.arange(0, 2 * np.pi, 0.01)

    # Inicjalizacja wykresu z funkcją sinus
    line, = ax.plot(x, np.sin(x))

    # Dodanie kropki o promieniu 0.05 na wykres
    dot = Circle((0, 0), radius=0.2, color='green')
    ax.add_patch(dot)

    # Funkcja animacji, która jest wywoływana dla każdej klatki animacji
    def animowanie(i):
        # Obliczenie przesunięcia fazowego
        phase_shift = i / 10.0
        line.set_ydata(np.sin(x + phase_shift))

        # Obliczenie nowej pozycji kółka (dot) na wykresie
        dot_center_x = x[i % len(x)]
        dot_center_y = np.sin(dot_center_x + phase_shift)
        dot.set_center((dot_center_x, dot_center_y))

        return line, dot

    # Tworzenie animacji z wywołaniem funkcji animate dla każdej klatki
    ani = animation.FuncAnimation(fig, animowanie, frames=len(x), interval=20, blit=False)

    plt.show()

if __name__ == "__main__":
    main()
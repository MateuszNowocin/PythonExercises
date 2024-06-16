import numpy as np

class Floor:
    def __init__(self, distance):
        self.distance = distance

class Needle:
    def __init__(self, x, theta, length):
        self.x = x
        self.theta = theta
        self.length = length

def toss_needle(L, floor):
    x = np.random.rand() * floor.distance
    theta = np.random.rand() * np.pi
    return Needle(x, theta, L)

def cross_line(needle, floor):
    x_right_tip = needle.x + (needle.length / 2) * np.sin(needle.theta)
    x_left_tip  = needle.x - (needle.length / 2) * np.sin(needle.theta)
    return x_right_tip > floor.distance or x_left_tip < 0

def estimate_prob_needle_crosses_line(nb_tosses, floor, L):
    nb_crosses = 0
    for _ in range(nb_tosses):
        needle = toss_needle(L, floor)
        if cross_line(needle, floor):
            nb_crosses += 1
    return nb_crosses / nb_tosses

# Parametry symulacji
floor_distance = 1.0  # Odległość między równoległymi liniami
needle_length = 0.75   # Długość igły
num_tosses = 10000    # Liczba rzutów igłą

floor = Floor(floor_distance)
estimated_probability = estimate_prob_needle_crosses_line(num_tosses, floor, needle_length)

# Obliczenie teoretycznego prawdopodobieństwa
theoretical_probability = (2 * needle_length) / (np.pi * floor_distance)

print(f"Szacowane prawdopodobieństwo: {estimated_probability}")
print(f"Teoretyczne prawdopodobieństwo: {theoretical_probability}")
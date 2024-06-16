import argparse
import os
import glob


def parse_arguments():
    parser = argparse.ArgumentParser(description='Znajdź i wypisz pliki z danym rozszerzeniem')
    parser.add_argument('extension', type=str, help='Szukane rozszerzenie')
    parser.add_argument('directory', type=str, nargs='?', default=os.getcwd(),
                        help='Przeszukiwany katalog: (domyślnie: obecnie używany katalog)')
    return parser.parse_args()


def find_files(directory, extension):
    # przeszukujemy cały katalog w poszukiwaniu podanego rozszerzenia
    search_pattern = os.path.join(directory, f"*.{extension}")
    files = glob.glob(search_pattern)
    return files


def file_size_generator(directory, extension):
    seen_files = set()
    while True:
        # przeszukujemy przy każdej iteracji, żeby zobaczyć czy nie ma nowych plików
        files = find_files(directory, extension)

        remaining_files = [f for f in files if f not in seen_files]
        if not remaining_files:
            break
        smallest_file = min(remaining_files, key=os.path.getsize)
        seen_files.add(smallest_file)
        yield smallest_file


def main():
    args = parse_arguments()
    files = find_files(args.directory, args.extension)

    if not files:
        print(f"Nie znaleziono plików z rozszerzeniem '{args.extension}' w katalogu '{args.directory}'.")
        return

    file_gen = file_size_generator(args.directory, args.extension)

    for file in file_gen:
        try:
            file_size = os.path.getsize(file)
            print(f"Plik: {file}, Rozmiar: {file_size} bitów")
        except FileNotFoundError:
            print(f"Plik nie odnaleziony: {file}")

        input("Wciśnij Enter by kontynuować...")


if __name__ == "__main__":
    main()
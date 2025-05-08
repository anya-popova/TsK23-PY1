import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as csv_file:
        reader = [i for i in csv.DictReader(csv_file, delimiter=',', quotechar='\n')]
    with open(OUTPUT_FILENAME, 'w') as json_file:
        json.dump(reader, json_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

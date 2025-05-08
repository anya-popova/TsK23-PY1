import json

FILE = 'input.json'


def task() -> float:
    with open(FILE) as f:
        data = json.load(f)

    multiplied = [i['score']*i['weight'] for i in data]
    answer = sum(multiplied)

    return round(answer, 3)


print(task())

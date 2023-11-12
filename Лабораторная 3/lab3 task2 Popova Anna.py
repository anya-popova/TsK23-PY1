def find_common_participants(first_group, second_group, razdelit=","):
    first_list = first_group.split(razdelit)
    second_list = second_group.split(razdelit)
    obschie = []

    for first in first_list:
        for second in second_list:
            if first == second and first not in obschie:
                obschie.append(first)
                continue
    obschie.sort()

    return obschie


participants_first_group = "Иванов|Петров|Сидоров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, "|")

print(result)

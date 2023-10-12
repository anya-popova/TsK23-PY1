list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

total = len(list_players)
team = int(total/2)

team1 = list_players[:team]
team2 = list_players[team:]

print(team1)
print(team2)

users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
users_kolichestvo = len(users)
unique = set(users)
unique_kolichestvo = len(unique)

visits = {
    "Общее количество": users_kolichestvo,
    "Уникальные посещения": unique_kolichestvo
}

print(visits)

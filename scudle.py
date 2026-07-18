import random

people = ["sakshi", "Sarah", "Rohan", "chinmaya",
          "bhor", "Sonali", "sama", "sumit"]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", ]

# Shuffle the people list once, so the order is random
random.shuffle(people)

start_index = 0

for day in days:
    group = []
    i = start_index

    while len(group) < 3:
        person = people[i % len(people)]
        group.append(person)
        i = i + 1

    print(day + ": " + ", ".join(group))

    start_index = start_index + 3

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Luna", "house": "Ravenclaw", "patronus": "Hare"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
    {"name": "Cedric", "house": "Hufflepuff", "patronus": "Badger"}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

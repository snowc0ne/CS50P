students = ["Hermione", "Harry", "Ron"]

students2 = { # This is a dictionary. A dictionary is a collection of key-value pairs. The key is on the left side of the colon and the value is on the right side of the colon. The key-value pairs are separated by commas. The key-value pairs are enclosed in curly braces.
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
    "Luna": "Ravenclaw"
}

print(students2["Hermione"])

for name in students2:
    print(name, students2[name], sep=", ")



print(students[0])
print(students[1])
print(students[2])

for student in students:
    print(student)


for i in range(len(students)): # len(students) is the length of the list students. The length of the list students is 3. So the range function will create a range from 0 to 2. The range function takes an integer as an argument. The integer is the number of elements in the range. So if the integer is 3, the range function will create a range from 0 to 2.
    print(i + 1, students[i])
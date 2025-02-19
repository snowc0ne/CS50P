i = 3
while i != 0:
    print("moo")
    i = i - 1


i = 0
while i < 3:
    print("mooer")
    i += 1

for i in range(3):
    print("mooest")

while True:
    n = int(input("Gimme number: "))
    if n > 0:
        break # Breaks out of the loop if the condition is met

for _ in range(n):
    print("mootist")
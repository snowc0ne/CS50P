def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("Gimme number "))
        if n > 0:
            break
    return n
    

def meow(n):
    for i in range(n):
        print("meow")

main()
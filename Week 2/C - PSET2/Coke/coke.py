# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents. In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

def main():
    total_inserted = 0
    amount_due = 50
    denominations = [25, 10, 5]

    print(f"Amount Due: {amount_due}")

    while total_inserted < amount_due:
        try:
            coin = int(input("Insert a coin: "))
            if coin in denominations:
                total_inserted += coin
                if total_inserted < amount_due:
                    print(f"Change due: {amount_due - total_inserted}")
            else:
                pass
        except ValueError:
            pass

    if total_inserted >= amount_due:
        change = total_inserted - amount_due
        print(f"Change owed: {change}")

main()


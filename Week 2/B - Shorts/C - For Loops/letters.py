def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]

    print(f"The current guest list is {names} ")
    response = input("Do you want to add more guests? (y/n) ")


    if response == "y":
        new_guests = input("Enter the names of the guests separated by commas: ")
        names.extend(new_guests.split(",")) # Add the new guests to the list. Extend is used to add multiple items to the list.
        print(f"The new guest list is {names}")


        response2 = input("Send the invitations? (y/n) ")
        if response2 == "y":
            send_letter(names)
        else:
            print("Invitations not sent.")                
    else:
        send_letter(names)
    

def send_letter(names):
    for name in names:
        print(write_letter(name, "Princess Peach"))



def write_letter(receiver, sender):
    return f"""
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
Dear {receiver},

You are cordially invited to a ball at Peach's Castle this evening, 7:00 PM.

Sincerely,
{sender}
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
"""


main()
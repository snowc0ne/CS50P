distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} meters")


def convert(au):
    return au * 149597870700



# def main():
#     for name in distances.keys():
#         print(f"{name} is {distances[name]} AU from Earth") 
# {distances[name]} is the value of the key name in the dictionary distances.
# This code spits out: Voyager 1 is 163 AU from Earth


main()
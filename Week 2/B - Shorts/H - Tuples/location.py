import sys

def main():
    coordinate_tuple = (42.376, -71.115)
    coordinate_list = [42.376, -71.115]
    print(f"{sys.getsizeof(coordinate_tuple)} bytes")
    print(f"{sys.getsizeof(coordinate_list)} bytes")



    # latitude, longitude = coordinates # Unpacking the tuple
    # print(f"Latitude: {coordinates[0]}")
    # print(f"Longitude: {coordinates[1]}")

    # print(f"Latitude: {latitude}")
    # print(f"Longitude: {longitude}")

main()
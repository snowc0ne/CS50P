# Dictionary is {} and list is []

def main():
    spacecraft = {"name": "Voyager 1", "distance": 163}
    spacecraft["distance"] = 167
    spacecraft.update({"orbit": "Heliosheath", "swag": "out of this world"})
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
========== REPORT ==========

Name: {spacecraft["name"]}
Distance: {spacecraft.get("distance", "No Data")} AU
Orbit: {spacecraft.get("orbit", "No Orbit")}
Swag: {spacecraft.get("swag", "No drip")}

============================
"""

if __name__ == "__main__":
    main()
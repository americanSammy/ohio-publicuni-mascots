import time

# This program shows you about dictionaries?
mascots = {
    "akron": "zips",
    "kent state": "golden flashes",
    "bowling green": "falcons",
    "ohio state": "buckeyes",
    "cincinnati": "bearcats",
    "miami": "redhawks",
    "cleveland state": "vikings",
    "toledo": "rockets",
    "central state": "maurauder",
    "ohio": "bobcats",
    "wright state": "raiders",
    "shawnee state": "bears",
    "youngstown state": "penguins"
    }
print("Welcome to the Ohio Public University Mascot Finder")
print("There are "  + str(len(mascots)) + " public universities in the Great State.")
while True:
    school = input("Type in the name of your school: ").lower()
    if school in mascots:
        print(mascots[school])
    elif school not in mascots:
        print("Wrong....")
    else:
        print("Try again...")
        break
    


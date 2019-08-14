import ast
import time


def mascot_finder():
    with open('mascots.txt', 'r') as f:
        s = f.read()
        mascots = ast.literal_eval(s)
    print("Welcome to the Public University Mascot Finder")
    print("There are "  + str(len(mascots)) + " universities in the list.")
    go = 'yes'
    while go in {'yes','y'}:
        school = input("Type in the name of your school: ").lower()
        if school in mascots:
            print(mascots[school].capitalize())
            go = input('Would you like continue (yes/no): ').lower()
            if go not in {'yes', 'y', 'n', 'no'}:
                while go not in {'yes', 'y', 'n', 'no'}:
                    print('I did not understand what you entered. Please try again.')
                    go = input('Would you like continue (yes/no): ').lower()
        elif school not in mascots:
            print("I couldn't find that. Please try again.")
        else:
            print("Try again...")
            break


try:
    mascot_finder()
except Exception as err:
    print(str(err))
    time.sleep(10)

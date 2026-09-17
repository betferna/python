#!/bin/env python3

import math

def get_player_pos():
    while True:
        try:
            user_input = input("Enter new coordinates as floats in format 'x,y,z': ")
            # coordinates = tuple(float(x) for x in user_input
            comas = 0
            coord = [None, None, None]
            string = ""
            for chars in user_input:
                if chars == ',':
                    coord[comas] = string
                    string = ""
                    comas +=1
                elif chars != ',':
                    string += chars
                elif comas > 2:
                    raise Exception
                coord[comas] = string
            coordinates = tuple(float(val) for val in coord)
            break
        except Exception:
            print("Invalid syntax")
            print("Enter new coordinates as floats in format 'x,y,z': 1.0 , 2.5, 3.0")
    return coordinates

if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    coordinate1 = get_player_pos()
    print(f"Got a first tuple: {coordinate1}")
    print(f"It includes: X={coordinate1[0]}, Y={coordinate1[1]} Z={coordinate1[2]}")
    distance = math.sqrt((0-coordinate1[0])**2 + (0-coordinate1[1])**2 + (0-coordinate1[2])**2)
    print(f"Distance to center: {distance}")
    print("\nGet a second set of coordinates")
    coordinate2 = get_player_pos()
    distance = math.sqrt((coordinate1[0]-coordinate2[0])**2 + (coordinate1[1]-coordinate2[1])**2 + (coordinate1[2]-coordinate2[2])**2)
    print(f"Distance between the 2 sets of coordinates: {distance}")

import math


def pythagoreous_theorem():

    ab: float = float(input("Enter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))

    bc: float = math.sqrt(ab**2 + ac**2)
    print("The length of BC (the hypotenuse) is: " + str(bc))

pythagoreous_theorem()
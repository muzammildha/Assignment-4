def triangle_perimeter():
    side1: str = input("What is the length of side 1?")
    side1: float = float(side1)

    side2: str = input("What is the length of side 2?")
    side2: float = float(side2)
    
    side3: str = input("What is the length of side 3?")
    side3: float = float(side3) 
    
    perimeter: float = side1 + side2 + side3
    
    print(f"The perimeter of the triangle is {perimeter}")

triangle_perimeter()


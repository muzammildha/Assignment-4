


inches_in_one_foot: int = 12 

def feet_to_inches():
    feet: float = float(input("Enter number of feet: "))  
    inches: float = feet * inches_in_one_foot 
    print("That is", inches, "inches!")

feet_to_inches()    

# program to solve this age-related riddle!
# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows
# Anton is 21 years old.
# Beth is 6 years older than Anton.
# Chen is 20 years older than Beth.
# Drew is as old as Chen's age plus Anton's age.
# Ethan is the same age as Chen.

def how_old_are_they():
    anton_uncle_age :int = 21
    beth_aunt_age :int = anton_uncle_age + 6
    chen_aunt_age :int = beth_aunt_age + 20
    drew_uncle_age :int = chen_aunt_age + anton_uncle_age
    ethan_uncle_age :int = chen_aunt_age

    print(f"Anton is {anton_uncle_age} years old.")
    print(f"Beth is {beth_aunt_age} years old.")
    print(f"Chen is {chen_aunt_age} years old.")
    print(f"Drew is {drew_uncle_age} years old.")
    print(f"Ethan is {ethan_uncle_age} years old.")

how_old_are_they()  

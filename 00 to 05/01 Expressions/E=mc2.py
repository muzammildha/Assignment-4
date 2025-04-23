def calculate_energy():

    C = 299792458  # speed of light in m/s
    while True:  # Using while loop
        user_input = input("Enter mass in kilograms (or type 'exit' to quit): ")
        if user_input.lower() == 'exit': # to break the loop
            break
        try:
            mass = float(user_input)
            energy = mass * C**2
            print(f"Equivalent energy: {energy} joules")
        except ValueError:
            print("Please enter a valid number or type 'exit' to quit.")

calculate_energy() 

def farenheit_to_celsius():
    farenheit_temperature :str = input("Enter the temperature in Farenheit")
    farenheit :int = int(farenheit_temperature)
    celsius :int = (farenheit - 32) * 5/9
    print(f"The temperature in Celsius is {celsius}")

farenheit_to_celsius()


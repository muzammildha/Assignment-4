def add_many_numbers(numbers):
    return sum(numbers)

numbers:list[int] = input("Enter a list of numbers separated by spaces: ").split()

numbers = [int(number) for number in numbers]
print(add_many_numbers(numbers))


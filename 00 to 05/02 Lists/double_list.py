def double_list(numbers):
    return [number * 2 for number in numbers]

numbers:list[int] = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(number) for number in numbers]
print(double_list(numbers))



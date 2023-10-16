# function that computes the average of a list of numbers
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0  # To handle the case when the list is empty.
    total = sum(numbers)
    average = total / len(numbers)
    return average

# implement the function in main using a splitted list of numbers from the user
def main():
    # Get a list of numbers from the user
    numbers_str = input("Enter a list of numbers separated by spaces: ")
    numbers_str_list = numbers_str.split()

    # Convert the input values to a list of floats
    numbers = [float(num) for num in numbers_str_list]

    # Call the calculate_average function
    avg = calculate_average(numbers)

    print("Average:", avg)

# call the main function
if __name__ == "__main__":
    main()

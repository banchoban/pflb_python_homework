#! /usr/bin/python

def nums_counter():
    """
    Takes numbers from stdin.
    Prints taken numbers, their count, sum, max, min and avg numbers.

    :return: None
    """

    numbers = list()

    while True:
        number = input("Enter a number: ")

        if not number:
            break

        try:
            numbers.append(int(number))
        except ValueError:
            print("This is not a number")

    print(f"You have entered {len(numbers)} numbers: " + ", ".join([str(num) for num in numbers]))

    numbers_sum = sum(numbers)
    print(f"Numbers sum: {numbers_sum}")
    print(f"Max number: {max(numbers)}")
    print(f"Min number: {min(numbers)}")
    print(f"Avg number: {numbers_sum / len(numbers)}")


if __name__ == "__main__":
    nums_counter()

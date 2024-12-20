def fizzbuzz():
    # Iterate through numbers 1 to 100 (inclusive)
    for num in range(1, 101):
        # Check if number is multiple of both 3 and 5 first
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        # Check if number is multiple of 3
        elif num % 3 == 0:
            print("Fizz")
        # Check if number is multiple of 5
        elif num % 5 == 0:
            print("Buzz")
        # If none of the above conditions are met, print the number
        else:
            print(num)

# Call the function
fizzbuzz()
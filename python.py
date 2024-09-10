# 1. Simple Comparison: Check if a number is even or odd
def is_even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"
print(is_even_or_odd(4))


# 2. Age Check: Categorize age into Minor, Adult, or Senior
def check_age_category(age):
    if age < 18:
        return "Minor"
    elif age <= 64:
        return "Adult"
    else:
        return "Senior"
print(check_age_category(20))



# 3. Temperature Advice: Provide advice based on temperature
def temperature_advice(temperature):
    if temperature > 30:
        return "Hot"
    elif 15 <= temperature <= 30:
        return "Warm"
    else:
        return "Cold"
print(temperature_advice(25))


# 4. Grade Evaluation: Evaluate the grade based on score
def evaluate_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"
print(evaluate_grade(85))


# 5. Sum of List: Return the sum of all numbers in a list
def sum_list(numbers):
    return sum(numbers)
print(sum_list([1, 2, 3, 4, 5]))


# 6. Print Multiples: Print the first 10 multiples of a number
def print_multiples(n):
    for i in range(1, 11):
        print(n * i)
print_multiples(3)


# 7. Reverse String: Print each character of a string in reverse order
def reverse_string(s):
    print(s[::-1])
reverse_string("hello")


# 8. Count Vowels: Count the number of vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
print(count_vowels("hello world"))


# 9. Countdown: Print a countdown from n to 1
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
countdown(5)


# 10. Guess the Number: Simulate a number guessing game
import random
def guess_number_game():
    number_to_guess = random.randint(1, 100)
    guess = None
    while guess != number_to_guess:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
    print("Congratulations! You guessed it!")
guess_number_game()


# 11. Factorial Calculation: Calculate the factorial of a number using a while loop
def calculate_factorial(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial
print(calculate_factorial(5))


# 12. Fibonacci Sequence: Generate and print the first n numbers in the Fibonacci sequence
def fibonacci_sequence(n):
    a, b = 0, 1
    count = 0
    while count < n:
        print(a)
        a, b = b, a + b
        count += 1
fibonacci_sequence(5)


# 13. Convert to Uppercase: Convert a string to uppercase
def to_uppercase(s):
    return s.upper()
print(to_uppercase("hello"))


# 14. Calculate Square: Return the square of a number
def square_number(n):
    return n * n
print(square_number(4))


# 15. Check Palindrome: Check if a string is a palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Making it case insensitive and ignoring spaces
    return s == s[::-1]
print(is_palindrome("madam"))


# 16. Find Maximum: Find the maximum number in a list
def find_maximum(numbers):
    return max(numbers)
print(find_maximum([1, 3, 2, 5, 4]))
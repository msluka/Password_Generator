#Password Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

def  generate_password():
    while True:

        pass_length = input("Choose the password length:\n")

        try:
            pass_length = int(pass_length)
            nr_of_letters = int(pass_length * 0.4) #40% letters
            nr_of_numbers = int(pass_length * 0.4) #40% numbers
            nr_of_symbols = pass_length - (nr_of_letters + nr_of_numbers) # the rest are symbols

            random_letters = random.choices(letters, k=nr_of_letters)
            random_numbers = random.choices(numbers, k=nr_of_numbers)
            random_symbols = random.choices(symbols, k=nr_of_symbols)

            password = random_letters +  list(map(str, random_numbers)) + random_symbols
            random.shuffle(password)
            password = ''.join(password)
            print(password)
            return password

        except ValueError:
            print("Invalid input. Please provide a correct numeric value.")
            continue

generate_password()
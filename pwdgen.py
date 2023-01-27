import random

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+1234567890-="

number = input("Amount of passwords to generate: ")
number = int(number)

length = input("Length of passwords: ")
length = int(length)

for password in range(number):
    passwords=" "
    for x in range(length):
        passwords += random.choice(char)
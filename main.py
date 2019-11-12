import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDFGHIJKLMNOPQRSTUVWXYZ1234567890'

length = input('Introduce the lenght of your password: ')
length = int(length)
password = ''

for c in range(length):
    password += random.choice(chars)
print(password)
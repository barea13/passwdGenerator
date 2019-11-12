import random
import os

chars = 'abcdefghijklmnopqrstuvwxyzABCDFGHIJKLMNOPQRSTUVWXYZ1234567890'

quant = input('Introduce the quantity of passwords (default 4): ')

if quant == '':
    quant = 4
else:
    quant = int(quant)

length = input('Introduce the lenght of your password (default 10): ')

if length == '':
    length = 10
else:
    length = int(length)

for q in range(quant):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
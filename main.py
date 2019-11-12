import random
import os

chars = 'abcdefghijklmnopqrstuvwxyzABCDFGHIJKLMNOPQRSTUVWXYZ1234567890'

def default(v, i):
    if v == '':
        v = i
    else:
        v = int(v)

quant = input('Introduce the quantity of passwords (default 4): ')
default(quant, 4)
length = input('Introduce the lenght of your password (default 10): ')
default(length, 10)

for q in range(quant):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
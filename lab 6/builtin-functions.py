#1
from functools import reduce

lst = [1, 2, 3, 4, 5]
res = reduce((lambda x, y: x * y), lst)

print(res)

#2
word = 'Programming'
lower_letter, upper_letter = [], []

x = [lower_letter.append(1) if _.islower() else upper_letter.append(1) if _.isupper() else None for _ in word]
print(f'lower: {len(lower_letter)}, upper: {len(upper_letter)}')

#3
string = 'pp2'
check = ''.join(reversed(string))
print(string == check)

#4
from time import sleep
from math import sqrt

num = int(input("Enter a number: "))
miliseconds = int(input("Enter delay in milliseconds: "))

sleep(miliseconds / 1000)  # перевод миллисекунд в секунды

result = sqrt(num)

print(f'Square root of {num} after {miliseconds} milliseconds is {result:.2f}')

#5
from random import randint 
print(all((randint(0, 1) for _ in range(5))))

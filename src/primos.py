#!/usr/bin/python3
# Python program to display all the prime numbers within an interval

lower = 1
upper = 100

print("Prime numbers between", lower, "and", upper, "are:")
# Funciona acá

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

# Y funciona acá también


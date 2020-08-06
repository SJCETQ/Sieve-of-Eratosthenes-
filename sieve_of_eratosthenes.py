# Sieve of Eratosthenes - For Prime Number

import math


number = int(input("Enter a random number: "))

all_number = []

for i in range(2, number + 1):
    all_number.append(i)

i = 2

while(i <= int(math.sqrt(number))):

   
    if i in all_number:

        
        for j in range(i*2, number + 1, i):

            if j in all_number:

                all_number.remove(j) 
    i += 1

print(all_number)

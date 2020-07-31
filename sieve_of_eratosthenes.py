# Sieve of Eratosthenes - For Prime Number

import math


number = int(input("Enter a random number: "))

all_number = []

for i in range(2, number + 1):
    all_number.append(i)

i = 2
# from 2 to square root of the number
while(i <= int(math.sqrt(number))):

    # if i is in list then we gotta delete its multiples
    if i in all_number:

        # j will give multiples of i, starting from 2*i
        for j in range(i*2, number + 1, i):

            if j in all_number:

                all_number.remove(j)  # deleting the multiple if found in list
    i = i + 1

print(all_number)

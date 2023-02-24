n = 40000

#input = [0,1,3,5,10,11,22,24,28,4,8]
input = list(range(3,n))


def isPrime(n):
    result = False
    for i in range(2, n):

        if (n % i) == 0:
            break
    else:
        result = True
    return result



# Function to return nearest prime number
from math import floor, sqrt


def primes_from_to_n(n):
    l = []
    for i in range(2, n):
        if isPrime(i):
            l.append(i)
    return l


def closest_prime(n):
    p = n
    while n!=0:

        if isPrime(n) and p!=n:
            return n
        else:
            n -=1

print(closest_prime(5))


def main(input):
    output = []
    largest_number = max(input)
    l = primes_from_to_n(largest_number)

    for n in input:
        close_prime = closest_prime(n)
        if n in [0, 1] or isPrime(n) and not isPrime(n - close_prime):
            output.append(0)
            pass

        else:
            number_to_append =0


            temp = []
            for i in l[:l.index(close_prime)]:

                if n - i in l and i not in temp and n >i:
                    number_to_append += 1
                    temp.append(n - i)
            output.append(number_to_append)

    return output
t = main(input)
print(t)



# Summation of Primes
# Problem 10th
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
def summationOfPrime(num):
    primeNum = 2
    sum = 0
    while primeNum<num:
        if(isPrime(primeNum)):
            sum += primeNum
        primeNum += 1

    return sum

def isPrime(n):
    # if n < 2: return "Neither prime, nor composite"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
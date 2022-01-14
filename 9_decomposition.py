def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(2))
print(is_prime(10))
print(is_prime(11))
print(is_prime(9))
print(is_prime(2017))


def first_n_primes(n):
    primes = []
    num = 2

    while (len(primes)) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

print(first_n_primes(0))
print(first_n_primes(1))
print(first_n_primes(4))


def sum_of_n_primes(n):
    sum = 0
    primes = first_n_primes(n)
    for i in range(len(primes)):
        sum += primes[i]
    return sum

print(sum_of_n_primes(0))
print(sum_of_n_primes(1))
print(sum_of_n_primes(4))
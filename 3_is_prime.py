def is_prime(num):
    for i in range(2, int(num ** 1/2) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(2))
print(is_prime(10))
print(is_prime(11))
print(is_prime(9))
print(is_prime(2017))

def prime_numbers_in_range(n):
    if isinstance(n,int) and n > 2:
        primes_nums = [2]
        for num in range(3,n):
            if num % 2 > 0:
                isprime = True
                for i in range(2,num):
                    if num % i == 0:
                        isprime = False
                if isprime:
                    primes_nums.append(num)
        return primes_nums
    else:
        raise TypeError("Number must be an integer greater than 2")


print(prime_numbers_in_range(10))
print(prime_numbers_in_range(100))
print(prime_numbers_in_range(1000))
print(prime_numbers_in_range(10000))
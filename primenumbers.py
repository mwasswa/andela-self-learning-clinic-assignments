import time
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
        return "argument must be an integer greater than 2"


for num in range(1000, 1000001, 1000):
    start = time.time()
    prime_numbers_in_range(num)
    end = time.time()
    print('size: %d time: %f' % (num, end-start))
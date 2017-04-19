def fizz_buzz(number):
    if isinstance(number,int):
        is_divisible_by_3 = (number %3 == 0)
        is_divisible_by_5 = (number % 5 == 0)
        if is_divisible_by_3 and is_divisible_by_5:
            return "FizzBuzz"

        elif is_divisible_by_5 and not is_divisible_by_3:
            return "Buzz"
        elif is_divisible_by_3 and not is_divisible_by_5:
            return "Fizz"
        else:
            return number

    else:
        return number

print(fizz_buzz(10))
print(fizz_buzz(33))
print(fizz_buzz(105))
print(fizz_buzz(25))
print(fizz_buzz(10))
print(fizz_buzz(15))
print(fizz_buzz(101))
print(fizz_buzz(8))
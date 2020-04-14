import math

'''
Checking for primality by using a deterministic variant of the Miller-Rabin test in O((lg(n))^4)
'''


# class definition defines a controlled exception to continue outer loops form inner loops, which is
# really useful in this context

class Continue(Exception):
    pass


def is_prime(number: int):

    # checking for simple stuff
    if number < 2 or number % 2 == 0:
        return False

    # we then need to write our input n in the form d*2^r + 1 (d is not divisible by 2)
    # d is first assigned to n - 1, then subsequently divided by every factor of 2 it has, which are factored into 2^r

    r, d = 0, number - 1
    while d % 2 == 0:
        r, d = r + 1, d // 2

    # defining our outer continue
    continue_a = Continue()

    for a in range(2, min(number - 2, math.floor(2 * (math.log(number)) ** 2))):
        try:
            # assigning x to a^d modulo n. Pow does this very efficiently by using modulo arithmetic
            x = pow(a, d, number)

            # if its congruent to 1 or -1 mod n, we don't need the subsequent checks
            if x == 1 or x == number - 1:
                continue

            # we square x modulo n up to r - 1 times until its congruent to -1 mod n.
            # If it never achieves this, its definitively not prime
            # If it does, we continue the outer loop
            for _ in range(r - 1):
                x = pow(x, 2, number)
                if x == number - 1:
                    raise continue_a

            return False

        except Continue:
            # catched in the outer loop
            continue

    # if a^d = 1 (mod n) or a^d*(2^k) = -1 (mod n) for every a in the range, then congrats! it is prime!
    return True

# Inspired by stackOverflow answer: Calculating and printing the nth prime number
# For testing: hundred-millionth prime: 29996224275833


if __name__ == '__main__':
    n = int(input("Enter a number to check for primality: "))
    print("Woah! It's a prime! :O" if is_prime(n) else "Sorry, it's not prime :c")

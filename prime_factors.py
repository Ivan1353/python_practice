def prime_factors(n):
    factors = {}
    divisor = 1
    while True:
        divisor += 1
        if n % divisor == 0:
            factors[divisor] = 1
            n /= divisor
            while True:
                if n % divisor == 0:
                    factors[divisor] += 1
                    n /= divisor
                else:
                    break
        if n == 1:
            break
    string = ""
    print(factors)
    for element in factors:
        if factors[element] > 1:
            string += f"({element}**{factors[element]})"
        else:
            string += f"({element})"
    return string
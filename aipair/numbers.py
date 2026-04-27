def isprime(number:int) -> bool:
    """Returns True if the number is prime, False otherwise."""
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def print_all_factors(number:int) -> None:
    """Prints all factors of the given number."""
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    print(f"Factors of {number}: {factors}")

    


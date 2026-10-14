"""Implementation of Sieve of Eratosthenes"""

def sieve(n) -> list[bool]:
    """Get a list of all primes up to `n`"""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for p in range(2, int(n ** 0.5) + 1):
        if not primes[p]:
            continue
        for n in range(p * 2, n + 1, p):
            primes[n] = False
    return primes

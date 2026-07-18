import math

import matplotlib
import matplotlib.pyplot as plt


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.isqrt(n))
    for divisor in range(3, limit + 1, 2):
        if n % divisor == 0:
            return False
    return True


def first_n_primes(count: int) -> list[int]:
    primes: list[int] = []
    candidate = 2
    while len(primes) < count:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes


def main() -> None:
    primes = first_n_primes(1000)
    indices = list(range(1, len(primes) + 1))

    plt.figure(figsize=(12, 6))
    plt.plot(indices, primes, linewidth=1.25)
    plt.title("Prime Numbers: First 1,000 Values")
    plt.xlabel("Prime index")
    plt.ylabel("Prime value")
    plt.grid(True, linestyle="--", linewidth=0.5, alpha=0.7)
    plt.tight_layout()

    plt.savefig("first_1000_primes.png")
    if matplotlib.get_backend().lower() != "agg":
        plt.show()


if __name__ == "__main__":
    main()

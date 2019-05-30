
def calc_pi(n_terms: int) -> float:
    """Calculate pi using Leibniz formula: pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11...."""
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0

    pi: float = 0.0
    for _ in range(n_terms):
        pi += operation * (numerator / denominator)

        denominator += 2.0
        operation *= -1.0
    return pi


print(calc_pi(10_000_000))

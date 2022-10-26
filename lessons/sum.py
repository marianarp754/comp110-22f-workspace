"""Example of writing a test subject."""


def sum(xs: list[float]) -> float:
    """Compute the sum of a list."""
    total: float = 0.0
    i: int = 0
    while i < len(xs):
        total = total + xs[i]
        i = i + 1
    return total
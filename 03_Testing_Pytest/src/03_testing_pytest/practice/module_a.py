"""Practice module A: pure functions for M3-1 (M03.01-M03.02)."""

import sys


def clamp(value: float, low: float, high: float) -> float:
    """Clamp value to [low, high]. Raises ValueError if low > high."""
    if low > high:
        raise ValueError(f"low ({low}) must be <= high ({high})")
    return max(low, min(value, high))


def split_bill(total: float, people: int, tip_pct: float = 0.0) -> float:
    """Return per-person share including tip_pct. Raises ValueError on invalid input."""
    if people <= 0:
        raise ValueError("people must be > 0")
    if total < 0 or tip_pct < 0:
        raise ValueError("total and tip_pct must be >= 0")
    return total * (1.0 + tip_pct / 100.0) / people


def require_positive_int(raw: str) -> int:
    """Parse raw as a positive int, or exit with code 2."""
    try:
        value = int(raw)
    except ValueError:
        sys.exit(2)
    if value <= 0:
        sys.exit(2)
    return value


def is_even(n: int) -> bool:
    """Return True if n is an even integer (rejects bool and non-int)."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n must be an int, not bool or other type")
    return n % 2 == 0

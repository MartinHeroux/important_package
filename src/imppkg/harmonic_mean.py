from typing import Sized, Iterable
import statistics


def harmonic_mean(numbers: Iterable[float]):
    return statistics.mean(numbers)


def too_long(some_object: Sized) -> bool:
    return len(some_object) > 100

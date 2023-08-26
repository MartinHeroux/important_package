import sys

from termcolor import cprint

from imppkg.harmonic_mean import harmonic_mean
from statistics import StatisticsError


def main():
    result = 0.0

    try:
        nums = [float(num) for num in sys.argv[1:]]
    except ValueError:
        nums = []

    try:
        result = harmonic_mean(nums)
        cprint(str(result), "red", "on_cyan", attrs=["bold"])
    except ZeroDivisionError:
        pass
    except StatisticsError:
        error = "ERROR: NO VALUES TO AVERAGE"
        cprint(error, "red", "on_cyan", attrs=["bold"])

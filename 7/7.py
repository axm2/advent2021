import statistics
import math


def determine_fuel(arr):
    median = statistics.median(arr)
    total_fuel_median = 0
    for i in arr:
        total_fuel_median += abs(i - median)
    print(total_fuel_median)


# brute force lol
def determine_fuel_b(arr):
    min_total_fuel_dev = float("inf")
    for k in range(min(arr), max(arr) + 1):
        total_fuel_dev = 0
        for i in arr:
            n = abs(i - k)
            total_fuel_dev += (n * (n + 1)) / 2
        if total_fuel_dev < min_total_fuel_dev:
            min_total_fuel_dev = total_fuel_dev
    print(min_total_fuel_dev)


if __name__ == "__main__":
    with open("input.txt") as f:
        crabs = [int(x) for x in next(f).rstrip("\n").split(",")]
    determine_fuel(crabs)
    determine_fuel_b(crabs)

"""
Module compute_statistics: Computes statistical measures (mean, median, mode, standard deviation,
and variance) from numbers in a text file.
"""

import time

def read_numbers(path):
    """Reads numbers from a file and returns them as a list of floats."""
    with open(path, 'r', encoding='utf-8') as file:
        return [float(line.strip()) for line in file if line.strip().replace('.', '', 1).isdigit()]

def calculate_mean(numbers):
    """Calculates and returns the mean of a list of numbers."""
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    """Calculates and returns the median of a list of numbers."""
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    return (numbers[mid - 1] + numbers[mid]) / 2 if n % 2 == 0 else numbers[mid]

def calculate_mode(numbers):
    """Calculates and returns the mode(s) of a list of numbers."""
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_frequency = max(frequency.values())
    return [num for num, freq in frequency.items() if freq == max_frequency]

def calculate_variance(numbers, mean):
    """Calculates and returns the variance of a list of numbers."""
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_std_dev(variance):
    """Calculates and returns the standard deviation of a list of numbers."""
    return variance ** 0.5

def compute_statistics(path):
    """Main function to compute statistics."""
    start_time = time.time()
    numbers = read_numbers(path)

    if not numbers:
        return "No valid numbers found in the file."

    mean = calculate_mean(numbers)
    median = calculate_median(numbers)
    mode = calculate_mode(numbers)
    variance = calculate_variance(numbers, mean)
    std_dev = calculate_std_dev(variance)
    elapsed_time = time.time() - start_time

    results = (f"Mean: {mean}\nMedian: {median}\nMode: {mode}\n"
               f"Standard Deviation: {std_dev}\nVariance: {variance}\n"
               f"Elapsed Time: {elapsed_time} seconds")

    with open('statistics_results.txt', 'w', encoding='utf-8') as file:
        file.write(results)

    return results

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        print(compute_statistics(file_path))
    else:
        print("Usage: python compute_statistics.py file_with_data.txt")

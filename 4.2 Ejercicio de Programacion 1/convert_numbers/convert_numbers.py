"""
Module convert_numbers: Converts numbers from a file to their binary and hexadecimal
representations. Reads numbers from a file, converts them, and writes the results to
another file.
"""

import time

def read_numbers(file_path):
    """
    Reads numbers from a file and returns them as a list of integers.
    Only considers lines that represent valid integers.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return [int(line.strip()) for line in file if line.strip().isdigit()]

def to_binary(number):
    """Converts an integer to its binary representation (as a string)."""
    return bin(number)[2:]

def to_hexadecimal(number):
    """Converts an integer to its hexadecimal representation (as a string)."""
    return hex(number)[2:]

def convert_numbers(file_path):
    """
    Main function to convert numbers to binary and hexadecimal.
    Reads numbers from a file, converts them, and writes the results to another file.
    """
    start_time = time.time()
    numbers = read_numbers(file_path)

    if not numbers:
        return "No valid numbers found in the file."

    results = ""
    for number in numbers:
        binary = to_binary(number)
        hexadecimal = to_hexadecimal(number)
        results += f"Number: {number}, Binary: {binary}, Hexadecimal: {hexadecimal}\n"

    elapsed_time = time.time() - start_time

    results += f"Elapsed Time: {elapsed_time} seconds"

    with open('conversion_results.txt', 'w', encoding='utf-8') as file:
        file.write(results)

    return results

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python convert_numbers.py file_with_data.txt")
    else:
        print(convert_numbers(sys.argv[1]))

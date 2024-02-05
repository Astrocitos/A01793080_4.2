"""
Module word_count: Counts the occurrences of each distinct word in a given text file.
The results are saved to another file and also printed on the screen.
"""

import time

def read_words(file_path):
    """
    Reads words from a file and returns them as a list of strings.
    The words are converted to lower case.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().lower().split()

def count_words(words):
    """
    Counts the frequency of each word in a list of words.
    Returns a dictionary with words as keys and their counts as values.
    """
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def analyze_word_count(file_path):
    """
    Main function to count word occurrences.
    Reads a file, counts word occurrences, and writes results to another file.
    """
    start_time = time.time()
    words = read_words(file_path)

    if not words:
        return "No words found in the file."

    counts = count_words(words)
    results = "\n".join([f"Word: '{word}', Count: {count}" for word, count in counts.items()])

    elapsed_time = time.time() - start_time

    results += f"\nElapsed Time: {elapsed_time} seconds"

    with open('word_count_results.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(results)

    return results

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python word_count.py file_with_data.txt")
    else:
        result = analyze_word_count(sys.argv[1])
        print(result)

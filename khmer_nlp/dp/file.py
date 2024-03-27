import csv
import os
from file_path import get_path


def load_dictionary(csv_file):
    dictionary = {}
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            word = row[0]
            parts_of_speech = row[1:]
            dictionary[word] = parts_of_speech

    return dictionary


# Get the directory of the current script file

# Construct the file path
current_dir = get_path()
file_path = os.path.join(current_dir, 'dictionaries', 'kh_words.csv')
print('Loading dictionary', file_path)
# Load the dictionary
khmer_dictionary = load_dictionary(file_path)
print('Loading dictionary', khmer_dictionary)

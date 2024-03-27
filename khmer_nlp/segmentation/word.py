# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# word

class KhmerWordSegmentor:
    """
    This is a KhmerWordSegmentor class to generate word base on dictionary
    """
    def __init__(self, dictionary):
        self.dictionary = set(dictionary)

    def segment(self, character):
        words = []
        while character:
            for i in range(len(character), 0, -1):
                prefix = character[:i]
                if prefix in self.dictionary:
                    words.append(prefix)
                    character = character[i:]
                    break
            else:
                # If prefix doesn't exist in dictionary then just return empty
                new_word = character[0]
                self.dictionary.add(new_word)
                words.append(new_word)
                character = character[1:]
        return words


# How to use:
if __name__ == '__main__':
    # load data from Khmer Dictionary
    khmer_dictionary = {"ខ្ញុំ", "មក", "ពី", "ប្រទេស", "កម្ពុជា"}

    # instantiate KhmerWordsSegmentor class
    segmentor = KhmerWordSegmentor(khmer_dictionary)

    # Segment a Khmer text
    input_text = "ខ្ញុំមកពីប្រទេសកម្ពុជា"
    segmented_text = segmentor.segment(input_text)

    # Print segmented words
    print(segmented_text)

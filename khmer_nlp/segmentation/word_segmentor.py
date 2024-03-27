# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License
# You may obtain a copy of the License at
# tokenize/word_segmentation
from khmer_nlp.core import chars
from khmer_nlp.core.khnlp import is_khmer_character, is_started_khmer_character


def khmer_word_segmentation(sentence: str):
    segmentation = []
    curation = ""
    sentence = sentence
    for word in sentence.split(chars.SEPARATOR):
        for i, char in enumerate(word):
            curation += char
            next_char = word[i + 1] if (i + 1 < len(word)) else ""

            # Clustering or filtering not a Khmer character
            if (not is_khmer_character(char)
                    and next_char != " "
                    and next_char != ""
                    and not is_khmer_character(next_char)):
                continue
            # Clustering or filtering number
            if char in chars.KHMER_NUMBER and next_char in chars.KHMER_NUMBER:
                continue

            # Not a Khmer character and not in clustering or filtering
            if not is_khmer_character(char) and next_char == " " or next_char == "":
                segmentation.append(curation)
                curation = ""
            elif is_started_khmer_character(next_char) and not (char in chars.KHMER_SUBSCRIPT):
                segmentation.append(curation)
                curation = ""
    return segmentation



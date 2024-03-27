# Clean up DataSource
import re
from typing import List, Callable

from khmer_nlp.core import chars
from dictionary import unkown_words


def cleanup_khmer_character(sentence: str) -> str:
    """
    Clean up Khmer characters for tokenizing
    :param sentence: Text input to clean
    :return: str: the cleaned text
    """

    # Define patterns to match characters in Khmer like letters and numbers
    khmer_pattern = re.compile(r'[\u1780-\u17FF\d\s,.!?០ឥ៩]')  # Add or remove characters as needed

    # Iterate through each character in the text
    cleaned_text = ''
    for character in sentence:
        # Check if the character is Khmer character
        if khmer_pattern.match(character):
            cleaned_text += character

    return cleaned_text


def correct_word(word: str):
    for token, normalized_token in unkown_words.word_does_not_exist():
        word = word.replace(token, normalized_token)
    return word


def word_cleaner(word: str):
    word = word.strip(chars.SEPARATOR).strip()
    word = word.replace("  ", " ")  # Space optimization
    word = word.replace(" ", "\u200b \u200b")  # Handle whitespace
    # Clean up messy characters
    word = word.replace("\u200b\u200b", "\u200b")  # Clean dup whitespace
    word = word.replace("\u200b\u200b", "\u200b")  # Various cases
    word = correct_word(word)

    # Remove special characters
    word = word.replace("\u2028", "")  # Line separator
    word = word.replace("\u200a", "")  # Hair spacing between word
    word = word.strip().replace("\n", "").replace("  ", " ")
    return word


def postprocessor(word, separator):
    word = word.replace(separator)
    return re.sub(f"(?:{separator}| )+", separator, word)


def is_khmer_character(character: str):
    """Check if a Khmer character"""
    if (character >= "\u1780") and (character <= "\u17ff"):
        return True
    if character in chars.KHMER_SYMBOLS:
        return True
    if character in chars.KHMER_LUNAR:
        return True
    return False


def is_started_khmer_character(character: str):
    if is_khmer_character(character):
        if character in chars.KHMER_NUMBER:
            return True
        if character in chars.KHMER_CONSONANTS:
            return True
        if character in chars.KHMER_SYMBOLS:
            return True
        if character in chars.KHMER_LUNAR:
            return True
        return False
    return True


# Regular expression to match a string well-known formatted numerals
_DIGITS_WITH_SEPARATOR = re.compile(r'\d+(?:[:.,]\d+)+')


def apply_postprocessors(tokens: List[str], processors: List[Callable[[List[str]], List[str]]]) -> List[str]:
    """
    Apply a list of callable postprocessors to a list of segments
    :param tokens:
    :param processors:
    :return:
    """
    for processor in processors:
        tokens = processor(tokens)
    return tokens


def rejoin_formatted_numbers(tokens: List[str]) -> List[str]:
    """
    Rejoin a list of well-known formatted numbers from a list of segments
    :param tokens:
    :return:
    """

    original_segment = "".join(tokens)
    matching_format = _DIGITS_WITH_SEPARATOR.finditer(original_segment)
    token_joined = []
    part_of_speech = 0

    for match in matching_format:
        if part_of_speech < match.start():
            token_joined.append(original_segment[part_of_speech:match.start()])
        token_joined.append(match.group())
        part_of_speech = match.end()
    return token_joined


def strip_whitespace(tokens: List[str]) -> List[str]:
    """
    Strip whitespace of each token and remove whitespace from tokens

    :param tokens:
    :return:
    """
    return [token.strip() for token in tokens if token.strip()]


if __name__ == "__main__":
    segments = ["123", ":", "45", ",", "678", ".", "90"]
    postprocessors = [rejoin_formatted_numbers, strip_whitespace]
    result = apply_postprocessors(segments, postprocessors)
    print(result)

    text = "សំណួរ: ពិសេស ១២៣៤ !?"
    cleaned_sentence = cleanup_khmer_character(text)
    print("Raw Text: ", text)
    print("Cleaned Text: ", cleaned_sentence)

from abc import ABC

from nltk.tokenize.api import StringTokenizer, TokenizerI


class CharacterTokenizer(StringTokenizer, ABC):
    """
    Tokenizes a string and returns a token string with the specified characters as tokens.
    How to use:
    Instantiate the CharTokenizer
    if __name__ == '__main__':
        tokenizer = CharacterTokenizer()
        input_text = "សួស្តីបងប្អូន ជុំវិញពិភពលោក!"
        tokens = tokenizer.tokenize(input_text)
        print(tokens)
    """

    def tokenize(self, s):
        return list(s)

    def span_tokenize(self, s):
        yield from enumerate(range(1, len(s) + 1))

    def _string(self, s):
        return s


class KhmerCharacterTokenizer(TokenizerI, ABC):
    """"
    Tokenizing string literals to return it with individual character
    # Instantiate the CharTokenizer
    if __name__ == '__main__':
        char_tokenizer = KhmerCharacterTokenizer()
        Tokenizing a string
        input_kh_text = "ខ្ញុំមកពីប្រទេសកម្ពុជា"
        tokens = char_tokenizer.tokenize(input_kh_text)
        Resulting string literals
        print(tokens)
    """

    def tokenize(self, string):
        return list(string)

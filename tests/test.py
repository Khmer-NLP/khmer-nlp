# Test
import unittest

import pytest

from khmer_nlp.tokenize.character import CharacterTokenizer


@pytest.fixture
def test_tokenizer():
    return CharacterTokenizer()


def test_khmer_word_tokenization(test_tokenizer):
    """Test khmer word"""
    khmer_word = "សួស្តី"
    expected_tokenized = ['ស', 'ួ', 'ស', '្', 'ត', 'ី']
    assert test_tokenizer.tokenize(khmer_word) == expected_tokenized


def test_english_word_tokenization(test_tokenizer):
    """Test khmer word"""
    english_word = "Hello"
    expected_tokenized = ['H', 'e', 'l', 'l', 'o']
    assert test_tokenizer.tokenize(english_word) == expected_tokenized


if __name__ == "__main__":
    unittest.main()

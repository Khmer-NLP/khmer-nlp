# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# _utils.py --
import re
from typing import List, Callable

_DIGITS_WITH_SEPARATOR = re.compile(r"(\d+[\.\,:])+\d+")


def apply_postprocessors(
        segments: List[str], postprocessors: Callable[[List[str]], List[str]]
) -> List[str]:
    """"
    Apply a list of callable to a raw segmentation result.
    """
    for func in postprocessors:
        segments = func(segments)
    return segments


def rejoin_formatted_number(segments: List[str]) -> List[str]:
    """
    Rejoin well-known formatted mumberic that are over-tokenized.
    The formatted numberic are numbers separated by ":", ",", or ".", such as time, decimal numbers, comma-added numbers, and IP addresses.

    """
    original = "".join(segments)
    matching_results = _DIGITS_WITH_SEPARATOR.finditer(original)
    tokens_joined = []
    pos = 0
    segment_idx = 0

    match = next(matching_results, None)
    while segment_idx < len(segments) and match:
        is_span_beginning = pos >= match.start()
        token = segments[segment_idx]
        if is_span_beginning:
            connected_token = ""
            while pos < match.end() and segment_idx < len(segments):
                connected_token += segments[segment_idx]
                pos += len(segments[segment_idx])
                segment_idx += 1
            tokens_joined.append(connected_token)
            match = next(matching_results, None)
        else:
            tokens_joined.append(token)
            segment_idx += 1
            pos += len(token)
    tokens_joined += segments[segment_idx:]
    return tokens_joined


def strip_whitespace(segments: List[str]) -> List[str]:
    """
    Strip whitespace(s) off each token and remove whitespace tokens.
    """
    segments = [token.strip(" ") for token in segments if token.strip(" ")]
    return segments

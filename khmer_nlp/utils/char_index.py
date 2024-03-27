# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# Utils/char_index.py
# Create a character-to-index dictionary and an index-to-character dictionary
from ..core import chars

character_to_index = {char: i for i, char in enumerate(chars.CHARS)}
index_to_character = {i: char for i, char in enumerate(chars.CHARS)}

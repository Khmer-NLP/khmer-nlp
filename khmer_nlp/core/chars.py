# Licensed under the Apache License, Version 2.0 (the "License");
# tokenizer.py

UNICODE_CHARS = [
    chr(i) for i in range(0x1780, 0x17ff)
]
LATIN_CHARS = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
CHARS = UNICODE_CHARS + LATIN_CHARS

# Declaration Character grouping
# The symbol to be used in separating the words in sentence
SEPARATOR = "\u200b"

KHMER_NUMBER = set(u"០១២៣៤៥៦៧៨៩")

# consonant and independent vowels
KHMER_CONSONANTS = set(u"កខគឃងចឆជឈញដឋឌឍណតថទធនបផពភមយរលវឝឞសហឡអឣឤឥឦឧឨឩឪឫឬឭឮឯឰឱឲឳ")

# subscript, diacritics
KHMER_SUBSCRIPT = set(u"្")

# Dependent vowel
KHMER_VOWELS = set(u"឴឵ាិីឹឺុូួើឿៀេែៃោៅ\u17c6\u17c7\u17c8")

KHMER_DIACRITIC = set(u"\u17c9\u17ca\u17cb\u17cc\u17cd\u17ce\u17cf\u17d0")
KHMER_SYMBOLS = set("៕។៛ៗ៚៙៘,.? ")  # add space
# Khmer Lunar is date count base on moon, characters Unicode from U+19E0 to U+19FF
KHMER_LUNAR = set("᧠᧡᧢᧣᧤᧥᧦᧧᧨᧩᧪᧫᧬᧭᧮᧯᧰᧱᧲᧳᧴᧵᧶᧷᧸᧹᧺᧻᧼᧽᧾᧿")

LATIN_CHARACTERS = set(u"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

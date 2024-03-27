# setup.py
from khmer_nlp import __version__
from setuptools import setup, find_packages

setup(
    name='khmer_nlp',
    version=__version__,
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'tensorflow',
        'numpy',
    ],
    author='Kuth Chi',
    author_email='kuthchi@outlook.com',
    description='A package for Khmer language natural language processing',
    url='https://github.com/Khmer-NLP/khmer-nlp',
    classifiers=[
        'Development Status :: Uninitialized',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU 3.0 License',
        'Operating System :: OS Independent',
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: Khmer",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: General",
        "Topic :: Text Processing :: Linguistic",
    ],
    keywords=[
        "khmernlp",
        "NLP",
        "natural language processing",
        "text analytics",
        "text processing",
        "localization",
        "computational linguistics",
        "KhmerNLP",
        "Khmer NLP",
        "Khmer language",
        "Chuon Nath",
        "Natural Language :: Khmer",
    ],
)

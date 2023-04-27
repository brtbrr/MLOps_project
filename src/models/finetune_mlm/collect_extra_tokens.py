import re
import typing as t
from collections import Counter

import razdel
from transformers import BertTokenizer


def is_like_english_word(char_seq:str)->bool:
    return re.search("[a-zA-Z]", char_seq)


def get_english_tokens(text:str)->t.List[str]:
    """
    :param text:
    :return: list of tokens, which look like English words
    """
    # toDo check if bert is cased
    return [
        tok.text.lower()
        for tok in razdel.tokenize(text)
        if is_like_english_word(tok.text)
    ]


def get_common_unknown_words(
    tokenizer: BertTokenizer, file_paths: t.List[str], threshold=50
)->t.List[str]:
    """
    :param tokenizer: previous version of tokenizer
    :param file_paths: train data plain text paths
    :param threshold: minimal corpus frequency of common word
    :return: list of common English words, which are not presented in
    previous version of tokenizer as single tokens
    """
    vocab = tokenizer.vocab.keys()
    unknown_words_counter = Counter()
    for path in file_paths:
        with open(path) as f:
            text = f.read()
            english_tokens = get_english_tokens(text)
            unknown_tokens = [tok for tok in english_tokens if tok not in vocab]
            unknown_words_counter.update(unknown_tokens)
    common_unknown_tokens = [
        tok for tok in unknown_words_counter if unknown_words_counter[tok] >= threshold
    ]
    return common_unknown_tokens

import typing as t
import razdel
from collections import Counter
from transformers import BertTokenizer
import re


def is_like_english_word(char_seq):
    return re.search("[a-zA-Z]", char_seq)


def get_english_tokens(text):
    # toDo check if bert is cased
    return [tok.text.lower() for tok in razdel.tokenize(text) if is_like_english_word(tok.text)]


def get_common_unknown_words(
    tokenizer: BertTokenizer, file_paths: t.List[str], threshold=50
):
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

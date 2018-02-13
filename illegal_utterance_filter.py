ILLEGAL_NGRAMS = {
    'uh oh',
    'oh oh',
    'oh dear',
    'oh no',
    'no no',
    'a b',
    'one two three',
    'two three four',
    'three four five',
    'four five six',
    'five six seven',
    'six seven eight',
    'seven eight nine',
    'eight nine ten',
    'nine ten eleven'}

def illegal_gram(gramstr):
    """ Returns false if ngram should be excluded from our analysis """
    if gramstr in ILLEGAL_NGRAMS:
        return True
    return False

def utterance_filter(words):
    """ Returns false if utterance should be excluded from our analysis """
    for i in range(2, 4):
        for j in range(0, len(words) - i + 1):
            if illegal_gram(' '.join(map(str, words[j:j+i]))):
                return False
    return True
import nltk
from nltk.corpus.reader import CHILDESCorpusReader
import illegal_utterance_filter

# C:\Users\ThinkPad\AppData\Roaming\nltk_data

corpus_root = nltk.data.find( 'corpora/CHILDES/Eng-NA-MOR/')
McCune = CHILDESCorpusReader(corpus_root, 'McCune/.*.xml')
def edit_age(age):
    if age == 21:
        Age = 20
    elif age == 27 or age == 25:
        Age = 26
    else:
        Age = age
    return Age

def wordlenth(corpus):
    file = corpus.fileids()
    wdlen_list = []
    for f in file:
        wdlen = {'fname': f, 'age': edit_age(corpus.age(f, month=True)[0]), 'one': 0, 'two': 0, 'three': 0, 'four': 0, 'five': 0}
        for sent in corpus.sents(f, speaker='CHI'):
            if not sent or not illegal_utterance_filter.utterance_filter(sent):  # in case there are empty utterances or utterances containing illegal ngrams.
                continue
            if len(sent) == 1:
                wdlen['one'] += 1
            elif len(sent) == 2:
                wdlen['two'] += 1
            elif len(sent) == 3:
                wdlen['three'] += 1
            elif len(sent) == 4:
                wdlen['four'] += 1
            elif len(sent) >= 5:
                wdlen['five'] += 1
        wdlen_list.append(wdlen)
    return(wdlen_list)
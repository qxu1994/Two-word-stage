import nltk
from nltk.corpus.reader import CHILDESCorpusReader
import illegal_utterance_filter
import pylangacq as pla
from illegal_utterance_filter import new

# C:\Users\ThinkPad\AppData\Roaming\nltk_data

child_name = ['ANT', 'BEL', 'HAR', 'TEA', 'CHI']

def wordlenth(corpus, illegal):
    file = corpus.fileids()
    wdlen_list = []
    for f in file:
        wdlen = {'fname': f, 'age': corpus.age(f, month=True)[0], 'one': 0, 'two': 0, 'three': 0, 'four': 0, 'five': 0}
        for sent in corpus.sents(f, speaker='CHI'):
            sent = new(sent)
            if not sent or not illegal_utterance_filter.unintel_filter(sent) or not illegal_utterance_filter.illegal_filter(sent, illegal):  # in case there are empty utterances or utterances containing illegal ngrams.
                continue
            if len(sent) == 1:
                wdlen['one'] += 1
                #print(sent)
            elif len(sent) == 2:
                wdlen['two'] += 1
                #print(sent)
            elif len(sent) == 3:
                wdlen['three'] += 1
                #print(sent)
            elif len(sent) == 4:
                wdlen['four'] += 1
                #print(sent)
            elif len(sent) >= 5:
                wdlen['five'] += 1
                #print(sent)
        wdlen_list.append(wdlen)
    return(wdlen_list)

def wdlen_no1(corpus):
    file = corpus.fileids()
    wdlen_list = []
    for f in file:
        wdlen = {'fname': f, 'age': corpus.age(f, month=True)[0], 'two': 0, 'three': 0, 'four': 0, 'five': 0}
        for sent in corpus.sents(f, speaker = 'CHI'):
            if not sent or not illegal_utterance_filter.unintel_filter(
                    sent):  # in case there are empty utterances or utterances containing illegal ngrams.
                continue
            if len(sent) == 2:
                wdlen['two'] += 1
                # print(sent)
            elif len(sent) == 3:
                wdlen['three'] += 1
                # print(sent)
            elif len(sent) == 4:
                wdlen['four'] += 1
                # print(sent)
            elif len(sent) >= 5:
                wdlen['five'] += 1
                # print(sent)
        wdlen_list.append(wdlen)
    return (wdlen_list)

def wdlen_mother(corpus):
    file = corpus.fileids()
    wdlen_list = []
    for f in file:
        wdlen = {'fname': f, 'age': corpus.age(f, month=True)[0], 'one': 0, 'two': 0, 'three': 0, 'four': 0, 'five': 0}
        for sent in corpus.sents(f, speaker='MOT'):
            if not sent or not illegal_utterance_filter.unintel_filter(sent):  # in case there are empty utterances or utterances containing illegal ngrams.
                continue
            if len(sent) == 1:
                wdlen['one'] += 1
                #print(sent)
            elif len(sent) == 2:
                wdlen['two'] += 1
                #print(sent)
            elif len(sent) == 3:
                wdlen['three'] += 1
                #print(sent)
            elif len(sent) == 4:
                wdlen['four'] += 1
                #print(sent)
            elif len(sent) >= 5:
                wdlen['five'] += 1
                #print(sent)
        wdlen_list.append(wdlen)
    return(wdlen_list)
#corpus_root = nltk.data.find( 'corpora/CHILDES/Thai/')
#Manchester = CHILDESCorpusReader(corpus_root, 'CRSLP/.*.xml')
#print(wordlenth(Manchester))

def speaker(corpus, f, name, illegal):
    wdlen = {'fname': f, 'age': corpus.age(f, month=True)[0], 'one': 0, 'two': 0, 'three': 0, 'four': 0, 'five': 0}
    for sent in corpus.sents(f, speaker=name):
        sent = new(sent)
        if not sent or not illegal_utterance_filter.unintel_filter(sent) or illegal_utterance_filter.illegal_filter(sent, illegal):  # in case there are empty utterances or utterances containing illegal ngrams.
            continue
        if len(sent) == 1:
            wdlen['one'] += 1
            # print(sent)
        elif len(sent) == 2:
            wdlen['two'] += 1
            # print(sent)
        elif len(sent) == 3:
            wdlen['three'] += 1
            # print(sent)
        elif len(sent) == 4:
            wdlen['four'] += 1
            # print(sent)
        elif len(sent) >= 5:
            wdlen['five'] += 1
            # print(sent)
    return wdlen

def wdlen_name(corpus, illegal):
    file = corpus.fileids()
    wdlen_list = []
    for f in file:
        #print(corpus.participants(file))
        for participant in corpus.participants(f):
            #print(participant)
            ID = [i for i in participant]
            #print(ID)
            name = ID[0]
            wdlen = speaker(corpus, f, name, illegal)
        wdlen_list.append(wdlen)
    return wdlen_list

def wordlenth_repeat(corpus):
    file = corpus.fileids()
    wdlen_list = []
    for f in file:
        wdlen = {'fname': f, 'age': corpus.age(f, month=True)[0], 'one': 0, 'two': 0, 'three': 0, 'four': 0, 'five': 0}
        for sent in corpus.sents(f, speaker='CHI'):
            sent = new(sent)
            if not sent or not illegal_utterance_filter.unintel_filter(sent): # or repeat_filter(sent, corpus, f)  # in case there are empty utterances or utterances containing illegal ngrams.
                continue
            if len(sent) == 1:
                wdlen['one'] += 1
                #print(sent)
            elif len(sent) == 2:
                wdlen['two'] += 1
                #print(sent)
            elif len(sent) == 3:
                wdlen['three'] += 1
                #print(sent)
            elif len(sent) == 4:
                wdlen['four'] += 1
                #print(sent)
            elif len(sent) >= 5:
                wdlen['five'] += 1
                #print(sent)
        wdlen_list.append(wdlen)
    return(wdlen_list)


def check(corpus, illegal):
    file = corpus.fileids()
    word_list = []
    for f in file:
        #wdlen = {'fname': f, 'age': corpus.age(f, month=True)[0], 'one': 0, 'two': 0, 'three': 0, 'four': 0, 'five': 0}
        age = corpus.age(f, month=True)[0]
        for sent in corpus.sents(f, speaker='CHI'):
            sent = new(sent)
            if not sent or not illegal_utterance_filter.unintel_filter(sent) or not illegal_utterance_filter.illegal_filter(sent, illegal):  # in case there are empty utterances or utterances containing illegal ngrams.
                continue
            if age and age < 21 and len(sent)>1:
                word_list.append(sent)
    return word_list

def print_u(corpus, illegal, set_age, u_len):
    u_list = []
    file = corpus.fileids()
    for f in file:
        #wdlen = {'fname': f, 'age': corpus.age(f, month=True)[0], 'one': 0, 'two': 0, 'three': 0, 'four': 0, 'five': 0}
        age = corpus.age(f, month=True)[0]
        for sent in corpus.sents(f, speaker='CHI'):
            utterance = {'fname': f, 'age': 0, 'sent': 0}
            sent = new(sent)
            if not sent or not illegal_utterance_filter.unintel_filter(sent) or not illegal_utterance_filter.illegal_filter(sent, illegal):  # in case there are empty utterances or utterances containing illegal ngrams.
                continue
            if age and age < set_age and len(sent) == u_len:
                utterance['age'] = age
                utterance['sent'] = sent
                u_list.append(utterance)
    return u_list
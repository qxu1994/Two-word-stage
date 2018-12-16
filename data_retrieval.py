import nltk
from nltk.corpus.reader import CHILDESCorpusReader
import illegal_utterance_filter
from tqdm import tqdm
import pickle


def data(corpus_name, illegal):
    '''the original nltk parser which will not produce speaker information within sents'''
    mother_sents = []
    for corpus in tqdm(corpus_name, 'overall'):
        file = corpus.fileids()
        for f in file:
            sents_list = list(corpus.sents(f, speaker=['MOT']))
            for sent in sents_list:
                #sent = new(sent)
                sent_list = []
                for i in sent:
                    if i:
                        sent_list.append(i.lower())
                if not sent_list or not illegal_utterance_filter.unintel_filter(sent_list) or not illegal_utterance_filter.illegal_filter(sent_list,illegal):  # in case there are empty utterances or utterances containing illegal ngrams.
                    continue
                else:
                    mother_sents.append(sent_list)
    return mother_sents

def vocab(train_list):
    vocab = {}
    for sent in train_list:
        for word in sent:
            vocab[word] = vocab.get(word, 0) + 1
    return vocab

def pad_train(train_list):
    new_list = []
    for sent in train_list:
        sent.insert(0, '<s>')
        sent.insert(len(sent), '</s>')
        new_list.append(sent)
    return new_list

def unk_train(train_list, vocab):
    once = {*()}
    for word in vocab:
        if vocab[word] == 1:
            once.add(word)
    unk_list = []
    for sent in train_list:
        for i in range(len(sent)):
            if sent[i] in once:
                sent[i] = 'unk'
        unk_list.append(sent)
    #print(len(once), n)
    return unk_list

def lower_test(test_list):
    '''take u_structure_three while returning real words in lowercase'''
    for sent in test_list:
        new_sent = []
        for word in sent['sent']:
            word = list(word)
            word[0] = word[0].lower()
            new_sent.append(tuple(word))
        sent['new sent'] = new_sent
    return test_list

def pad_test(test_list_lower):
    for sent in test_list_lower:
        new_sent = []
        for word in sent['new sent']:
            word = list(word)
            word.insert(0, '<s>')
            word.insert(len(word), '</s>')
            new_sent.append(tuple(word))
        sent['new sent'] = new_sent
    return test_list_lower

def unk_test(test_list, vocab_unk):
    ''' take a list of dictionaries in lowercase and sometimes padded, return unk (if the word does not in the training data or is empty and lowercase real words. e.g.[{'age': 19,
      'fname': 'Providence-xml/Alex/010707.xml',
      'sent': [('wee', 'adj', '1|3|MOD'),
               ('wee', 'adj', '2|3|MOD'),
               ('baby', 'n', '3|0|INCROOT')],
      'structure': 0}, ...]'''
    for sent in test_list:
        new_sent = []
        for word in sent['new sent']:
            word = list(word)
            if not word[0] or word[0] not in vocab_unk:
                word[0] = 'unk'
            new_sent.append(tuple(word))
        sent['new sent'] = new_sent
    return test_list


def data_retrieval():
    corpus_root = nltk.data.find('corpora/CHILDES/Eng-NA-MOR/')
    Bates = CHILDESCorpusReader(corpus_root, 'Bates/.*.xml')
    Bernstein = CHILDESCorpusReader(corpus_root, 'Bernstein/Children/.*.xml')
    Bloom70 = CHILDESCorpusReader(corpus_root, 'Bloom70/.*.xml')
    Bloom73 = CHILDESCorpusReader(corpus_root, 'Bloom73/.*.xml')
    Bohannon = CHILDESCorpusReader(corpus_root, 'Bohannon/.*.xml')
    Braunwald = CHILDESCorpusReader(corpus_root, 'Braunwald/.*.xml')
    Brent = CHILDESCorpusReader(corpus_root, 'Brent/.*.xml')
    Brown = CHILDESCorpusReader(corpus_root, 'Brown/.*.xml')
    Clark = CHILDESCorpusReader(corpus_root, 'Clark/.*.xml')
    Cornell = CHILDESCorpusReader(corpus_root, 'Cornell/.*.xml')
    Demetras2 = CHILDESCorpusReader(corpus_root, 'Demetras2/.*.xml')
    Feldman = CHILDESCorpusReader(corpus_root, 'Feldman/.*.xml')
    Hall = CHILDESCorpusReader(corpus_root, 'Hall/.*.xml')
    Higginson = CHILDESCorpusReader(corpus_root, 'Higginson/.*.xml')
    HSLLD = CHILDESCorpusReader(corpus_root, 'HSLLD-xml/.*.xml')
    Kuczaj = CHILDESCorpusReader(corpus_root, 'Kuczaj/.*.xml')
    MacWhinney = CHILDESCorpusReader(corpus_root, 'MacWhinney/.*.xml')
    Manchester = CHILDESCorpusReader(corpus_root, 'Manchester/.*.xml')
    McCune = CHILDESCorpusReader(corpus_root, 'McCune/.*.xml')
    McMillan = CHILDESCorpusReader(corpus_root, 'McMillan/.*.xml')
    Morisset = CHILDESCorpusReader(corpus_root, 'Morisset/.*.xml')
    Nelson = CHILDESCorpusReader(corpus_root, 'Nelson/.*.xml')
    NewEngland = CHILDESCorpusReader(corpus_root, 'NewEngland/.*.xml')
    NewmanRatner = CHILDESCorpusReader(corpus_root, 'NewmanRatner/.*.xml')
    NH = CHILDESCorpusReader(corpus_root, 'NH-xml/.*.xml')
    Post = CHILDESCorpusReader(corpus_root, 'Post/.*.xml')
    #Providence = CHILDESCorpusReader(corpus_root, 'Providence-xml/.*.xml')
    Rollins = CHILDESCorpusReader(corpus_root, 'Rollins/.*.xml')
    Sachs = CHILDESCorpusReader(corpus_root, 'Sachs/.*.xml')
    Snow = CHILDESCorpusReader(corpus_root, 'Snow/.*.xml')
    Soderstrom = CHILDESCorpusReader(corpus_root, 'Soderstrom/.*.xml')
    Suppes = CHILDESCorpusReader(corpus_root, 'Suppes/.*.xml')
    Tardif = CHILDESCorpusReader(corpus_root, 'Tardif/.*.xml')
    Valian = CHILDESCorpusReader(corpus_root, 'Valian/.*.xml')
    VanHouten = CHILDESCorpusReader(corpus_root, 'VanHouten/.*.xml')
    VanKleeck = CHILDESCorpusReader(corpus_root, 'VanKleeck/.*.xml')
    Weist = CHILDESCorpusReader(corpus_root, 'Weist/.*.xml')
    corpus_name = [Bates, Bernstein, Bloom70, Bloom73, Bohannon, Braunwald, Brent, Brown, Clark, Cornell, Demetras2,
                   Feldman, Hall, Higginson, HSLLD, Kuczaj, MacWhinney, Manchester, McCune, McMillan, Morisset, Nelson,
                   NewEngland, NewmanRatner, NH, Post, Rollins, Sachs, Snow, Soderstrom, Suppes, Tardif,
                   Valian, VanHouten, VanKleeck, Weist]
    illegal = [['b', 'i', 'o', 'b', 'b', 'b'], ['b', 'e', 'a', 'o'], ['e', 'a', 'u'], ['e', 'a'], ['a', 'boo'], ['hi', 'ho'],
               ['oh', 'ooh', 'ooh'], ['tee', 'kla'], ['bok', 'bok', 'there'], ['Y', 'T'], ['A', 'D'],
               ['bow', 'wow', 'bow', 'wow', 'bow', 'wow', 'eek', 'bow', 'wow', 'eek'], ['a', 'y'],
               ['k', 'k', 'k', 'k', "that's", 'a', 'k'], ['ho', 'ho', 'ho', 'hoo'], ['Ma', 'Ma', 'ma'],
               ['c', 'd', 'c', 'd', 'c', 'd'], ['cheesy', 'baby', 'big', 'big', 'big', 'big', 'puppy'],
               ['cheesy', 'baby', 'big', 'big', 'big', 'big'], ['water', 'water', 'water', 'Mommy', 'Mommy', 'water', 'water', 'Mama'],
               ['um', 'uh'], ['a', 'z'], ['a', 'b'], ['b', 'c'], ['i', 'o']]
    return data(corpus_name, illegal)

def get_three(three_list):
    '''retrieve all children's three-word utterances as the training data. Takes providence_three_chiperfin'''
    u_list = []
    for sent_dic in three_list:
        u_list.append(sent_dic['word'])
    return u_list

def three_train(three_list):
    '''save the list of three-word utterances as training_chithree.txt'''
    u_list = get_three(three_list)
    with open('providence_training_chithree.txt', 'w') as f:
        for i, sent in enumerate(u_list):
            f.write(' '.join(sent) + '\n')

def descriptive(list):
    des_dict = {'word':0, 'sent':0}
    n = 0
    for sent in list:
        n += len(sent)
    des_dict['word'] = n
    des_dict['sent'] = len(list)
    print(des_dict)

def save_list(list, fname):
    '''save data in txt'''
    with open(fname, "wb") as fp:  # Pickling
        pickle.dump(list, fp)

def load_list(fname):
    with open(fname, "rb") as fp:  # Unpickling
        return pickle.load(fp)

def save_to_file(list, fname):
    with open(fname, 'w') as f:
        for i, sent in enumerate(list):
            if i in [13456, 487119]:
                continue
            f.write(' '.join(sent) + '\n')

def test_unktest():
    voc = {'mother':0, 'father':0, 'sister':0}
    test_list = [{'age': 19,
      'fname': 'Providence-xml/Alex/010707.xml',
      'sent': [('wee', 'adj', '1|3|MOD'),
               ('wee', 'adj', '2|3|MOD'),
               ('baby', 'n', '3|0|INCROOT')],
      'structure': 0}, {'age': 19,
      'fname': 'Providence-xml/Alex/010707.xml',
      'sent': [('father', 'adj', '1|3|MOD'),
               ('mother', 'adj', '2|3|MOD'),
               ('baby', 'n', '3|0|INCROOT')],
      'structure': 0}]
    print(unk_test(test_list, voc))

def test_bug():
    train_unk = load_list('unk_train')
    vocab_trainunk = set(vocab(train_unk).keys())
    test_unk = load_list('unk_test')
    vocab_testunk = {}
    for sent in test_unk:
        #print(sent)
        for word in sent['new sent']:
            vocab_testunk[word[0]] = vocab_testunk.get(word[0], 0) + 1
    vocab_testunk = set(vocab_testunk.keys())

    #print(train_unk)
    #print(vocab_testunk - vocab_trainunk)

def mother_sent(corpus, n):
    file = corpus.fileids()
    u_list = []
    for f in tqdm(file, 'overall'):
        sents_list = list(corpus.sents(f, speaker='MOT'))
        for sent in sents_list:
            if len(sent) == n:
                utterance = {'fname': f, 'sent': sent}
                u_list.append(utterance)
    return u_list

def test_mother():
    corpus_root = nltk.data.find('corpora/CHILDES/Eng-NA-MOR/')
    Providence = CHILDESCorpusReader(corpus_root, 'Providence-xml/.*.xml')
    test_list = mother_sent(Providence, 3)
    save_list(test_list, 'providence_mother_three')

def main_nopad():
    original_train = load_list('training_data')
    unk_training = unk_train(original_train, vocab(original_train))
    save_list(unk_training, 'unk_train')
    original_test = load_list('u_structure_three')
    test_lower = lower_test(original_test)
    unk_testing = unk_test(test_lower, vocab(unk_training))
    save_list(unk_testing, 'unk_test')

def main_nopadunk():
    original_train = load_list('training_data')
    save_to_file(original_train, 'training_data.txt')
    original_test = load_list('u_structure_three')
    test_lower = lower_test(original_test)
    save_list(test_lower, 'unk_test_nopadunk')

def main_pad():
    #no, need to save them as a txt file. Each sentence is in a line
    #original_train = data_retrieval()
    #save_list(original_train, 'training_data')
    original_train = load_list('training_data')
    pad_training = pad_train(original_train)
    unk_training = unk_train(pad_training, vocab(pad_training))
    save_list(unk_training, 'unkpad_train')
    #print(load_list('unkpad_train'))
    original_test = load_list('u_structure_three')
    test_lower = lower_test(original_test)
    pad_testing = pad_test(test_lower)
    unk_testing = unk_test(pad_testing, vocab(pad_training))
    save_list(unk_testing, 'unkpad_test')


#main_nopadunk()
#main_nopad()
#test_unktest()
#test_bug()
#main_pad()
#a = load_list('training_data')
#descriptive(load_list('training_data'))
#print(load_list('training_data')[13456])
#print(load_list('unk_test_nopadunk'))
#test_mother()
three_train(load_list('providence_three_chiperfin'))
from new_parser import sents, age
import glob
import pickle
from new_childes import CHILDESCorpusReader
import nltk

# C:\Users\ThinkPad\AppData\Roaming\nltk_data

def contain(list1, list2):
    '''determine if list2 is a reduced imitation of list1'''
    string1 = ''.join(list1)
    string2 = ''.join(list2)
    if string2 in string1:
        return True
    else:
        return False
    #print('list:', list1, list2)
    #new_set = set(list1) & set(list2)
    #print('bingji:', new_set)
    #if new_set == set(list2):
        #print('test: ', new_set, set(list2))
        #return True
    #return False

def imitation_judge(index, sent, sents_list):
    '''determine if one sentence from the corpus is an imitation of the other sentence'''
    #index = sents_list.index(sent)
    if index != 0:
        if sent[1] == 'CHI':
            old_sent = sents_list[index - 1]
            #print('sent:', sent, 'old sent:', old_sent)
            if old_sent[1] == 'MOT':
                if sent[2:] == old_sent[2:] or contain(sent[2:], old_sent[2:]):
                    #print(old_sent, sent)
                    return True
    return False

def imitation_judge_pos(index, sent, sents_list):
    '''determine if one sentence from the corpus is an imitation of the other sentence'''
    #index = sents_list.index(sent)
    if index != 0:
        if sent[1] == 'CHI':
            old_sent = sents_list[index - 1]
            #print('sent:', sent, 'old sent:', old_sent)
            if old_sent[1] == 'MOT':
                sent_list = [i[0] for i in sent[2:]]
                old_list = [j[0] for j in old_sent[2:]]
                if sents_list == old_list or contain(old_list, sent_list):
                    #print(old_sent, sent)
                    return True
    return False

def get_imitation_list(index, corpus):
    '''get the children's immediate imitations that come from mother's speech'''
    imitation_list = []
    files = corpus.fileids()
    for f in files:
        for sent in corpus.sents(f):
            if imitation_judge(index, sent, corpus.sents(f)):
                #print(f)
                imitation_list.append(sent)
    return imitation_list

def pickle_list(list, fname):
    with open(fname, "wb") as output:
        pickle.dump(list, output)

def save_list_read():
    # Manchester
    corpus_root = nltk.data.find('corpora/CHILDES/Eng-NA-MOR/')
    Manchester = CHILDESCorpusReader(corpus_root, 'Manchester/.*.xml')
    pickle_list(get_imitation_list(Manchester), 'Manchester imitations')

'''
if __name__ == '__main__':
    #save_list_read()
def wdlen_imi(fpath):
    wdlen_list = []
    for f in glob.glob(fpath):
        wdlen = {'fname': f, 'age': age(f), 'one':0, 'two':0, 'three':0, 'four':0, 'five':0}
        for sent in get_imitation_list(f):
            if len(sent[2]) == 1:
                wdlen['one'] += 1
            elif len(sent[2]) == 2:
                wdlen['two'] += 1
            elif len(sent[2]) == 3:
                wdlen['three'] += 1
            elif len(sent[2]) == 4:
                wdlen['four'] += 1
            elif len(sent[2]) > 4:
                wdlen['five'] += 1
        #print(wdlen)
        wdlen_list.append(wdlen)
    return wdlen_list

def imi_per(fpath):
    percent = {}
    pass
    
def save_list(fname, string):
    with open(fname, mode='w', encoding='utf-8') as fp:
        content = string
        fp.write(content)
        
def load_list(fname):
    with open(fname, "rb") as data:
        list = pickle.load(data)
    return list

def get_imitation_text(fname):
    sents_list = sents(fname)
    imitation_list = []
    for sent in sents_list:
        if not sent[2]:
            continue
        if sent[0] == 'CHI':
            old_sent = sents_list[sents_list.index(sent) - 1]
            if old_sent[0] == 'MOT':
                if imitation(old_sent[2], sent[2]):
                    sent+=old_sent
                    imitation_list.append(sent)
    b = '\n'.join(map(str, imitation_list))
    return b

def all_imi_text(fpath):
    new_str = ''
    for f in glob.glob(fpath):
        new_str += f + '\n' + get_imitation_text(f) + '\n\n'
        print(new_str)
    return new_str
    '''













import re
import spacy
from tqdm import tqdm
import xl2dict
import pickle
import webcolors
import itertools

def save_list(list, fname):
    '''save data in txt'''
    with open(fname, "wb") as fp:  # Pickling
        pickle.dump(list, fp)

def load_list(fname):
    with open(fname, "rb") as fp:  # Unpickling
        return pickle.load(fp)

def structure_judge(sent):
    '''take a list of dictionaries. Each dictionary contains filename, age, and the two-word utterances with gra'''
    for word_gra in sent:
        #print(word_gra)
        if len(word_gra) >= 3:
            root = re.search('(?<=\|[0-9]\|).*$', word_gra[2])
            if root and root.group(0) == 'ROOT':
                return True
    return False

def predicate_judge(sent):
    '''take a list of dictionaries. Each dictionary contains filename, age, and the two-word utterances with pos'''
    # no longer be used
    verb = ['v', 'mod', '0aux']
    for word_gra in sent:
        if word_gra[1] in verb:
            return True
    return False

def number_co_judge(sent):
    number = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    color = ['red', 'blue', 'green', 'white', 'black', 'orange', 'pink', 'purple', 'yellow']
    n = 0
    for word_gra in sent:
        if word_gra[0].lower() in number or word_gra[0].lower() in color:
            n += 1
    return n > 1

def repetition_judge(sent):
    parent = ['mother', 'mommy', 'mom', 'mama', 'ma', 'father', 'dad', 'daddy', 'papa']
    word_sent = []
    n = 0
    for word_gra in sent:
        if word_gra[0].lower() in parent:
            n += 1
        word_sent.append(word_gra[0])
    combinations = list(itertools.combinations(word_sent, 2))
    for pair in combinations:
        if len(set(pair[0]) - set(pair[1])) == {'s'}: # may not work normally
            return True
    return len(set(word_sent)) < 3 or n > 1

def ohno_judge(sent):
    word_sent = [i[0].lower() for i in sent]
    return {'oh', 'no'}.issubset(set(word_sent))

def s_judge(sent):
    s = ["what's", "where's", "who's", "how's", "when's", "it's", "that's", "there's", "i'm", "they're", "she's",
         "he's", "you're"]
    for word_gra in sent:
        if word_gra[0].lower() in s:
            return True
    else:
        return False

def phrase_judge(sent):
    word_sent = [i[0].lower() for i in sent]
    return {'how', 'about'} in set(word_sent) or {'so', 'does'} in set(word_sent)

def compare_judge(sent, name, compare_list):
    '''sent is the sent from providence_three_gralm after word and pos are splited. Name
    is the key of sent. Compare_list is the corresponding list (i.e. name or pos)'''
    return sent[name] in compare_list

def excel_to_dict(fpath):
    myxlobject = xl2dict.XlToDict()
    return myxlobject.convert_sheet_to_dict(file_path= fpath, sheet='First Sheet')

def to_list(cor_list, name):
    '''takes elements from Providence_structure_cor after word and pos are splited, name is the name of the dictionary
    key.'''
    new_list = []
    for sent in cor_list:
        new_list.append(sent[name])
    return new_list

def word_pos_retrieve(alist, compare=True):
    '''takes Providence_structure_cor after excel_to_dict'''
    new_list = []
    for sent in alist:
        new_word = []
        new_pos = []
        if compare:
            for i in eval(sent['sent']):
                if len(i) > 1:
                    new_word.append(i[0])
                    new_pos.append(i[1])
                else:
                    print(i)
                word_str = ' '.join(new_word)
                word_str2 = re.sub(r'\\', '', word_str)
                sent['word'] = word_str2.split()
                pos_str = ' '.join(new_pos)
                pos_str2 = re.sub(r'\\', '', pos_str)
                sent['pos'] = pos_str2.split()
        else:
            for i in sent['sent']:
                if len(i) > 1:
                    new_word.append(i[0])
                    new_pos.append(i[1])
                else:
                    print(i)
                sent['word'] = new_word
                sent['pos'] = new_pos
        new_list.append(sent)
    return new_list


def structure(u_list, word_list, pos_list):
    '''take providence_three_gralm after word and pos are splitted. Refer to to_list for word_list and pos_list'''
    new_dic = []
    for dic in u_list:
        if number_co_judge(dic['sent']):
            dic['structure'] = 0
        elif ohno_judge(dic['sent']):
            dic['structure'] = 0
        elif s_judge(dic['sent']):
            dic['structure'] = 1
        elif phrase_judge(dic['sent']):
            dic['structure'] = 1
        elif predicate_judge(dic['sent']):
            dic['structure'] = 1
        elif repetition_judge(dic['sent']):
            dic['structure'] = 0
        elif structure_judge(dic['sent']):
            dic['structure'] = 1
        elif dic['trigram'] > -6.998:
            dic['structure'] = 1
        elif compare_judge(dic, 'word', word_list):
            dic['structure'] = 1
        elif compare_judge(dic, 'pos', pos_list):
            dic['structure'] = 1
        else:
            dic['structure'] = 0
        new_dic.append(dic)
    return new_dic

def pos_sentence(old_list):
    new_list = []
    for i in tqdm(old_list, 'overall'):
        sent = ' '.join([word[0] for word in i['sent'] if word])
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(sent)
        pos_list = []
        for token in doc:
            pos_list.append([token.text, token.pos_])
        i['pos_sent'] = pos_list
        new_list.append(i)
    return new_list



def test():
    old_list = [{'fname': 'Providence-xml/Alex/030006.xml', 'age': 36, 'sent': [['Ma', 'PROPN', '1|2|SUBJ'],
                ['watch', 'VERB', '2|0|ROOT'], ['this', 'DET', '3|2|OBJ']], 'structure': 1,
                 'new sent': [('ma', 'n:prop', '1|2|SUBJ'), ('watch', 'v', '2|0|ROOT'), ('this', 'pro:dem', '3|2|OBJ')],
                 3: -10.379233100648035, 2: -18.497320292877053}, {'fname': 'Providence-xml/Alex/030006.xml', 'age': 36,
                'sent': [('hi', 'co', '1|4|COM'), ('hi', 'co', '3|4|COM'), ('', 'n:prop', '4|0|ROOT')],
                'structure': 0, 'new sent': [('hi', 'co', '1|4|COM'), ('hi', 'co', '3|4|COM'),
                ('unk', 'n:prop', '4|0|ROOT')], 3: -13.394917918688353, 2: -27.585890218868364},
                {'fname': 'Providence-xml/Alex/030006.xml', 'age': 36, 'sent': [('um', ''),
                ('french', 'adj', '2|3|MOD'), ('fries', 'n', '3|0|INCROOT')],
                 'structure': 0, 'new sent': [('um', ''), ('french', 'adj', '2|3|MOD'),
                ('fries', 'n', '3|0|INCROOT')], 3: -13.179800995138725, 2: -22.254135461129195}]
    print(pos_sentence(old_list))

def main():
    word_list = to_list(word_pos_retrieve(excel_to_dict('Providence_structure_cor.xlsx')), 'word')
    pos_list = to_list(word_pos_retrieve(excel_to_dict('Providence_structure_cor.xlsx')), 'pos')
    u_list = word_pos_retrieve(load_list('providence_three_gralm'), compare=False)
    save_list(structure(u_list, word_list, pos_list), 'providence_three_finstr')
    #print(load_list('providence_three_finstr'))

#test()
#print(excel_to_dict('Providence_structure_cor.xlsx'))
main()
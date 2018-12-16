unintel = {
    'XXX',
    'YYY'}


'''
illegal = {
    ['嗯'],
    ['噢啊'],
    ['哼'],
    ['呷呷'],
    ['啊呜'],
    ['阿呜'],
    ['噢呜'],
    ['噢啊呵'],
    ['呜噢']
}'''


'''
def illegal_gram(gramstr):
    """ Returns false if ngram should be excluded from our analysis """
    if gramstr in ILLEGAL_NGRAMS:
        return True
    return False'''

def unintel_filter(sent):
    """ Returns false if utterance should be excluded from our analysis """
    if sent == ['xxx'] or sent == ['yyy']:
        return False
    else:
        return True

def unintel_filter_pos(sent):
    """ Returns false if utterance should be excluded from our analysis """
    if sent == ['xxx',''] or sent == ['yyy','']:
        return False
    else:
        return True

def unintel_filter_gra(sent):
    """ Returns false if utterance should be excluded from our analysis """
    if set(sent) == {('xxx','')} or set(sent) == {('yyy','')} or set(sent) == {('xxx',''), ('yyy', '')}:
        return False
    else:
        return True

def new(sent):
    new_sent = []
    for i in sent:
        if i == 'xxx' or i == 'yyy' or i == 'ss' or i == 'ow' or i == 'bok':
            continue
        else:
            new_sent.append(i)
    if len(new_sent)==4 and len(set(new_sent))==2 or len(new_sent)-len(set(new_sent))>2 or len(new_sent) == 3:
        new_sent = list(set(new_sent))
    return new_sent

def new_original(sent):
    new_sent = []
    for i in sent:
        if i == 'xxx' or i == 'yyy' or i == 'ss' or i == 'ow' or i == 'bok':
            continue
        else:
            new_sent.append(i)
    return new_sent

def new_original_gra(sent):
    new_sent = []
    for i in sent:
        if i[0] == 'xxx' or i[0] == 'yyy' or i[0] == 'ss' or i[0] == 'ow' or i[0] == 'bok':
            continue
        else:
            new_sent.append(i)
    return new_sent

def illegal_filter(sent, illegal):
    if (len(new(sent))>1 and len(set(new(sent))) == 1) or (set(new(sent)) == {'xxx', 'yyy'}) or sent in illegal:
        return False
    else:
        return True

def illegal_filter_pos(sent, illegal):   # also suits the gra analysis
    sent = [i[0] for i in sent]
    if (len(new_original(sent))>1 and len(set(new_original(sent))) == 1) or (set(new_original(sent)) == {'xxx', 'yyy'}) or sent in illegal:
        return False
    else:
        return True


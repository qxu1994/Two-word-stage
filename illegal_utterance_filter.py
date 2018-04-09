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
}
'''


'''
def illegal_gram(gramstr):
    """ Returns false if ngram should be excluded from our analysis """
    if gramstr in ILLEGAL_NGRAMS:
        return True
    return False'''

def unintel_filter(sent):
    """ Returns false if utterance should be excluded from our analysis """
    for i in unintel:
        if i in sent:
            return False
            break
        else:
            return True

def illegal_filter(sent):
    if sent in illegal:
        return False
    else:
        return True


    '''
    for i in range(2, 4):
        for j in range(0, len(words) - i + 1):
            if illegal_gram(' '.join(map(str, words[j:j+i]))):
                return False
    return True'''
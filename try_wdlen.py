from talkbank_parser import MorParser
import glob
import illegal_utterance_filter

parser = MorParser()

def age_transform(metadata):
    '''transform the original age into age in months'''
    ageday=0
    for i in metadata:    # get the location of 'Y', 'M', 'D'
        if i == 'Y':
            loc_Y = metadata.index(i)
        elif i == 'M':
            loc_M = metadata.index(i)
        elif i == 'D':
            loc_D = metadata.index(i)
    for i in metadata:   # get the number before 'Y', 'M', and 'D'
        if i == 'Y':
            age_year = int(metadata[loc_Y - 1])
        elif i == 'M':
            age_month = int(metadata[loc_Y + 1: loc_M])
        elif i == 'D':
            age_day = int(metadata[loc_M + 1: loc_D])
            if age_day >= 15:
                ageday = 1
            else:
                ageday = 0
    age_transformed = age_year * 12 + age_month + ageday
    return age_transformed

def wordlenth(filepath):
    wdlen_list = []
    for f in glob.glob(filepath):
        metadata = parser.parse_metadata(f)
        corpus = parser.tws_parse(f)
        corpus = list(corpus)

        wdlen = {'age': age_transform(metadata), 'one': 0, 'two': 0, 'three': 0, 'four': 0, 'five': 0}

        for uid, speaker, utterance in corpus:
            if speaker == 'CHI':
                words = [x.word for x in utterance]
                if not utterance or not illegal_utterance_filter.utterance_filter(words):  # in case there are empty utterances or utterances containing illegal ngrams.
                    continue
                if len(utterance) == 1:
                    wdlen['one'] += 1
                elif len(utterance) == 2:
                    wdlen['two'] += 1
                elif len(utterance) == 3:
                    wdlen['three'] += 1
                elif len(utterance) == 4:
                    wdlen['four'] += 1
                elif len(utterance) >= 5:
                    wdlen['five'] += 1
        wdlen_list.append(wdlen)
    return wdlen_list
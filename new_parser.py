# a parser which allows excluding imitations
import xml.etree.ElementTree as ET

def age_transform(metadata):
    '''transform age from years to months'''
    ageday = 0
    for i in metadata:  # get the location of 'Y', 'M', 'D'
        if i == 'Y':
            loc_Y = metadata.index(i)
        elif i == 'M':
            loc_M = metadata.index(i)
        elif i == 'D':
            loc_D = metadata.index(i)
    for i in metadata:  # get the number before 'Y', 'M', and 'D'
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

def age(fname):
    '''get the child's age from the file'''
    tree = ET.ElementTree(file=fname)
    root = tree.getroot()
    participant = root[0][0].attrib
    child_age = participant['age']
    return age_transform(child_age)

def sent(child_child, sent_list):  # ???need to keep words starting with 'g'. But unable to read with child.text. solved
    #print(sent_list)
    if child_child.tag[-1] == 'w':
        sent_list.append(child_child.text)
        #print(sent_list)
    return sent_list


def speaker(child):
    '''get the speaker of the individual sentence'''
    who_dict = child.attrib
    who = who_dict['who']
    return who

def uid(child):
    '''get the int of the uid of the individual sentence'''
    uid_dict = child.attrib
    uID = int(uid_dict['uID'][1:])
    return uID

def sents(fname):
    '''[speaker, uid, [sent]]'''
    all_sents = []
    tree = ET.ElementTree(file=fname)
    root = tree.getroot()
    for child in root:
        if 'who' in child.attrib:
            sents = []
            sent_list = []
            sents.extend((speaker(child), uid(child)))
            for child_child in child:
                if child_child.tag[-1] == 'g':
                    for child3 in child_child:
                        sent(child3, sent_list)
                #print(uid(child), child_child.tag, child_child.attrib, child_child.text)
                else:
                    sent(child_child, sent_list)
            sents.append(sent_list)
            all_sents.append(sents)
    return all_sents

def test(fname):
    print(sents(fname))
#test('e:/project/Manchester/anne/anne01a.xml')


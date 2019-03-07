import sys
import re
import nltk

"""
    Reads csv from path
     @return [
        [messageNumber: str, messageContent: str],
        ...
     ]
"""
def read_csv(csv_path):
    lines = [line.rstrip('\n') for line in open(csv_path)]
    csv_content = []
    for line in lines:
        csv_content.append(line.lower().split(','))

    return csv_content

"""
    Reads dict from path
    @return {
        <word:str> => <attributes:str>
        ...
    }
"""
def read_dict(dict_path):
    lines = [line.rstrip('\n') for line in open(dict_path)]
    dictionary = {}
    for line in lines:
        word, attributes = line.split('\\')
        word = word.lower()
        if word in dictionary:
            dictionary[word] += attributes
        else:
            dictionary[word] = attributes
    return dictionary

"""
    Enum for result score
"""
SCORE = {
    "NEGATIVE": -1,
    "POSITIVE": 1,
    "NEUTRAL": 0,
    "UNRELATED": 0
}
"""
    Defines the sentiment of a message and returns the associated score
    => IMPORTANT METHOD! <=
    All the rules of section Fonctionnalités of the pdf should be implemented here!
    @param message:String the message to score
    @param dictionary { <word:str> => <attributes:str> ... }
    @returns SCORE[sentiment]
"""
def score_message(message, dictionary):

    words = re.sub("[^\w]", " ",  message).split()

    '''
    # TODO debug this, the rest works (je crois que le split de la phrase sur la conjonction enleve pas la conjonction)
    for conjonction in ['and', 'but']:
        if conjonction in words:
            index_of_conjonction = words.index(conjonction)

            part1_score = score_message(' '.join(words[:index_of_conjonction]), dictionary)
            part2_score = score_message(' '.join(words[index_of_conjonction:]), dictionary)
            if part1_score + part2_score == 0:
                return SCORE['NEUTRAL']
            elif part1_score + part2_score < 0:
                return SCORE['NEGATIVE']
            else:
                return SCORE['POSITIVE']
    '''

    has_ideji = "ideji" in words
    #Rule 3 and 4
    has_ideji = has_ideji or any([w == 'your' and 's' in dictionary[words[i+1]] for i, w in enumerate(words[:-1])])

    has_competitor = False
    for word in words:
        if word not in dictionary:
            continue
        if 'c' in dictionary[word]:
            has_competitor = True
            break

    if has_ideji:
        for word in words:
            if word not in dictionary:
                continue
            word_attributes = dictionary[word]

            #Rule 1
            if 'b' in word_attributes:
                return SCORE["NEGATIVE"]

            #Rule 2
            elif 'g' in word_attributes:
                return SCORE['POSITIVE']

    if has_competitor:
        for word in words:
            if word not in dictionary:
                continue
            word_attributes = dictionary[word]

            #Rule 6
            if 'b' in word_attributes:
                return SCORE["POSITIVE"]

            #Rule 7
            elif 'g' in word_attributes:
                return SCORE['NEGATIVE']

    #Rule 5
    if not has_ideji and not has_competitor:
        return SCORE['UNRELATED']

    # TODO: IMPLEMENT RULES HERE!!!!
    # Rule 2...

    return SCORE["NEUTRAL"]


SCORE_OUTPUT = {-1: "negative", 0: "neutral", 1:"positive"}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path to csv message>")
        sys.exit()

    csv_path = sys.argv[1]
    dict_path = "dictionary.txt"
    csv_content = read_csv(csv_path)
    dictionary = read_dict(dict_path)
    for content in csv_content:
        id = content[0]
        message = content[1]
        score = score_message(message, dictionary)
        print(id+","+SCORE_OUTPUT[score])

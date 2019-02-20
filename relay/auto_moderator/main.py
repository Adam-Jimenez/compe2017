import sys
import re

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
    has_ideji = "ideji" in words
    # Rule 1
    if has_ideji:
        for word in words:
            if word not in dictionary:
                continue
            word_attributes = dictionary[word]
            if 'b' in word_attributes:
                return SCORE["NEGATIVE"]
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

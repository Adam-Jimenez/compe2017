import sys


"""
     @return [
        [messageNumber: str, messageContent: str],
        ...
     ]
"""
def read_csv(csv_path):
    lines = [line.rstrip('\n') for line in open(csv_path)]
    csv_content = []
    for line in lines:
        csv_content.append(line.split(','))

    return csv_content

def read_dict(dict_path):
    lines = [line.rstrip('\n') for line in open(dict_path)]
    dictionary = {}
    for line in lines:
        word, attributes = line.split('\\')
        if word in dictionary:
            dictionary[word] += attributes
        else:
            dictionary[word] = attributes
    return dictionary

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path to csv message>")
        sys.exit()

    csv_path = sys.argv[1]
    dict_path = "dictionary.txt"
    csv_content = read_csv(csv_path)
    dictionary = read_dict(dict_path)

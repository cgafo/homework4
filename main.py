import requests
import string


DQ = requests.get("https://www.gutenberg.org/cache/epub/996/pg996.txt")
with open("don_quixote.txt", "w", encoding='utf-8') as Don_Quixote:
    Don_Quixote.write(DQ.text)
H = requests.get("https://www.gutenberg.org/files/27761/27761-0.txt")
with open("hamlet.txt", "w", encoding='utf-8') as Hamlet:
    Hamlet.write(H.text)
def count_words_don_quixote(filename="don_quixote.txt"):
    """
    Count the words in the book
    :param filename:
    :return: a dictionary
    """
    words_dict_don_quixote = {}
    with open("don_quixote.txt", "r", encoding="utf-8") as f:
        for line in f:
            for p in string.punctuation:
                line = line.replace(p, "")
            line_words = line.split()
            for word in line_words:
                words_dict_don_quixote[word] = words_dict_don_quixote.get(word, 0) + 1
    return words_dict_don_quixote

def count_words_hamlet(filename="hamlet.txt"):
    """
    Count the words in the book
    :param filename:
    :return: a dictionary
    """
    words_dict_hamlet = {}
    with open("hamlet.txt", "r", encoding="utf-8") as g:
        for line in g:
            # remove punctuation from the line
            for q in string.punctuation:
                line = line.replace(q, "")
            line_words = line.split()
            for word in line_words:
                words_dict_hamlet[word] = words_dict_hamlet.get(word, 0) + 1
    return words_dict_hamlet

words_dict_don_quixote = count_words_don_quixote()
words_dict_hamlet = count_words_hamlet()
print(f"'Don Quixote has {len(words_dict_don_quixote)} unique words, whereas 'Hamlet' presents {len(words_dict_hamlet)} unique words.")
if len(words_dict_don_quixote) < len(words_dict_hamlet):
    print("Therefore, 'Don Quixote' has a lower number of unique words than 'Hamlet'.")
elif len(words_dict_don_quixote) > len(words_dict_hamlet):
    print("Therefore, 'Don Quixote' has a higher number of unique words than 'Hamlet'.")
else:
    print("Therefore, 'Don Quixote' has the exact same number of unique words than 'Hamlet'.")
ratio_quixote = len(words_dict_don_quixote)/sum(words_dict_don_quixote.values())
ratio_hamlet = len(words_dict_hamlet)/sum(words_dict_hamlet.values())
print(f"'Don Quixote presents a ratio of unique words/total words of {ratio_quixote}, while 'Hamlet' has {ratio_hamlet}.")
if ratio_quixote < ratio_hamlet:
    print("Therefore, 'Don Quixote' has a lower ratio of unique words/total words than 'Hamlet'.")
elif ratio_quixote > ratio_hamlet:
    print("Therefore, 'Don Quixote' has a higher ratio of unique words/total words than 'Hamlet'.")
else:
    print("Therefore, 'Don Quixote' has the same ratio of unique words/total words than 'Hamlet'.")

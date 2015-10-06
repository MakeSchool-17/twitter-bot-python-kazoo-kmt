import sys
import re

def histogram(filename):
    source_text = open(filename, "r")
    words_incl_mark = source_text.read()
    mark = re.compile(r"[^a-zA-Z0-9]")
    words_wo_mark = mark.sub(" ", words_incl_mark)
    words_wo_mark_wo_upper = words_wo_mark.lower()
    words_list = words_wo_mark_wo_upper.split()
    words_dictionary = {}
    for words_key in words_list:
        words_dictionary[words_key] = words_dictionary.get(words_key, 0) + 1
    return(words_dictionary)


def unique_words(histogram_arg):
    number_of_unique_words = len(histogram_arg.keys())
    return(number_of_unique_words)


def frequency(word_arg, histogram_arg):
    word_freq = histogram_arg.get(word_arg, 0)
    return(word_freq)


if __name__ == '__main__':
    filename = sys.argv[1]
    print(histogram(filename))
    print(unique_words(histogram(filename)))
    word_selected = sys.argv[2]
    print(frequency(word_selected, histogram(filename)))

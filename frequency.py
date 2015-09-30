# This is 2. Dictionary in tutorial5

# Advice from Alan: It's better to separate "read" as a function
# Question: How should I name each function and variables(little bit confusing...)
# Other Questions: see below
import sys
import re

def histogram(filename):
    # source_text = open("bushido_shortver.txt").read().split() #  It may better not to split before applying re
    source_text = open(filename, "r")
    words_incl_mark = source_text.read()
    # mark = re.compile("[^a-zA-Z0-9_\-]")
    # mark = re.compile(r"[^a-zA-Z0-9_\-]")
    mark = re.compile(r"[^a-zA-Z0-9]")
    # HOW CAN I TREAT Apostrophi????? IS IT OK TO IGNORE? e.g. You're
    words_wo_mark = mark.sub(" ", words_incl_mark)
    words_wo_mark_wo_upper = words_wo_mark.lower()
    words_list = words_wo_mark_wo_upper.split()

    words_dictionary = {}
    for words_key in words_list:
        words_dictionary[words_key] = words_dictionary.get(words_key, 0) + 1
    # for words_key in words_list:
    #     # if (words_key in words_dictionary) == False:
    #     if words_key not in words_dictionary:
    #         #note: I don't need double quotation when inputting key from the list
    #         words_dictionary[words_key] = 1
    #         # WHICH SHOULD I USE SINGLE OR DOUBLE QUOTATION????
    #     else:
    #         words_dictionary[words_key] += 1
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

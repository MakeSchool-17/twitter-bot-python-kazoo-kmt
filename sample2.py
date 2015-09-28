import sys
import random
import frequency
import time


def smpl_dstr(filename):
    words_histogram = frequency.histogram(filename)
    words_source = []
    for each_word in words_histogram:
        for i in range(0, frequency.frequency(each_word, words_histogram)):
            words_source.append(each_word)

    index = random.randint(0, len(words_source) - 1)
    return(words_source[index])


if __name__ == '__main__':
    start_time = time.clock()
    filename = sys.argv[1]

    for i in range(0, 1000):
        print(smpl_dstr(filename))


    end_time = time.clock()
    print(end_time - start_time)
    # wordname = sys.argv[2]
    # words_dictionary = frequency.histogram(filename)
    # number_unq_words = frequency.unique_words(words_dictionary)
    # frequency_word = frequency.frequency(wordname, words_dictionary)

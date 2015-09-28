import sys
import random
import frequency
# frequency.histogram()

def sample(filename):
    text_file = open(filename, "r")
    list_of_words = text_file.read().split()
    random.shuffle(list_of_words)
    random_index = random.randint(0, len(list_of_words) - 1)
    # print(list_of_words[random_index])
    return(list_of_words[random_index])

def sample_probability(filename):
    text_file = open(filename, "r")
    list_of_words = text_file.read().split()

    words_count = {}
    for each_word in list_of_words:
        words_count[each_word] = words_count.get(each_word, 0) + 1

    words_probability = {}
    for each_word in words_count:
        words_probability[each_word] = words_count[each_word] / len(list_of_words)

    print(words_probability)

if __name__ == '__main__':
    filename = sys.argv[1]
    print(sample(filename))
    print(sample_probability(filename))

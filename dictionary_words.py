import random
import sys

def pickup_words(number_of_output_words):

    text_file = open('text_for_test.txt', "r")
    list_of_words = list(text_file)
    chosen_words = []
    for i in range(0, number_of_output_words):
        random_index = random.randint(0, len(list_of_words) - 1)
        chosen_words_tmp = list_of_words[random_index]
        chosen_words.append(chosen_words_tmp[0:len(chosen_words_tmp)-1])
        list_of_words.pop(random_index)

    return(' '.join(chosen_words))

if __name__ == '__main__':
    number = sys.argv[1] #character
    actually_number = int(number) #convert to integer
    words = pickup_words(actually_number)
    print(words)

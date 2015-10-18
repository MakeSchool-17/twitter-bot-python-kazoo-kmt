import random
import sys

def pickup_words(number_of_output_words):

    text_file = open('text_for_test.txt', "r")
    list_of_words = list(text_file)

    # [brian] You forgot to close the file! In this program it'll get closed
    # when the script finishes, but in a larger program this could be a pretty
    # terrible mistake! Try writing:

    with open('text_for_test.txt', "r") as text_file:
        list_of_words = list(text_file)

    # and by the time the program reaches this line, the file will already
    # be closed.

    chosen_words = []
    for i in range(0, number_of_output_words):
        random_index = random.randint(0, len(list_of_words) - 1)
        chosen_words_tmp = list_of_words[random_index]
        chosen_words.append(chosen_words_tmp[0:len(chosen_words_tmp)-1])
        # [brian] You could also write: chosen_words_tmp[:-1]
        # Or even easier: chosen_words_tmp.strip()
        list_of_words.pop(random_index)

    return(' '.join(chosen_words))

if __name__ == '__main__':
    number = sys.argv[1] #character
    actually_number = int(number) #convert to integer
    words = pickup_words(actually_number)
    print(words)

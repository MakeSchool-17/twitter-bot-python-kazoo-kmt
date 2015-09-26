## HOW CAN I OMMIT "\n"????????
import random
import sys

def pickup_words(number_of_output_words):

    text_file = open('/usr/share/dict/words', "r")
    # list_of_words = text_file.read().split(' ')
    list_of_words = list(text_file)
    ## also working by using readlines
    #list_of_words = text_file.readlines()
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

# notes
#    random.shuffle(list_of_words)
#    list_of_number = [int(i) for i in range(list_of_words)]

# notes
# if __name__ == '__main__':
#     number = sys.argv[1:]
#     number = [int(i) for i in number]
#     #my_list = ['4', '5', '6']
#     #my_list = [4, 5, 6]
#     #for my_number in my_list:
#     #print(my_number)

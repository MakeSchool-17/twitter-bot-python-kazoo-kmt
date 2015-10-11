# Learn a Markov chain from a corpus
import hash_table
import parsing_tokenizing_byRE
import random


def store_to_hashtable(words_list):
    map_to_nexttoken = hash_table.HashTable()  # make hashtable which maps current token to next token
    map_to_frequency = hash_table.HashTable()  # make hashtable which maps next token to frequency
    for index in range(0, len(words_list) - 1):  # stop at the end of next_word
        current_word = words_list[index]
        # print("current_word: ", current_word)
        next_word = words_list[index + 1]
        # print("next_word: ", next_word)
        if map_to_nexttoken.get(current_word) is not None:
            list_of_next_word = map_to_nexttoken.get(current_word)
        else:
            list_of_next_word = None
        # print("list_of_next_word (before): ", list_of_next_word)
        if list_of_next_word is not None:
            for word_in_list in list_of_next_word:
                # print("word_in_list: ", word_in_list)
                if word_in_list == next_word:
                    key_for_frequency = str(current_word) + "-" + str(word_in_list)
                    # print("key_for_frequency: ", key_for_frequency)
                    # print("map_to_frequency.get(word_in_list): ", map_to_frequency.get(key_for_frequency))
                    updated_frequency = map_to_frequency.get(key_for_frequency) + 1
                    # print("updated_frequency: ", updated_frequency)
                    map_to_frequency.update(key_for_frequency, updated_frequency)
                    break
                else:
                    key_for_frequency = str(current_word) + "-" + str(next_word)
                    # print("key_for_frequency: ", key_for_frequency)
                    list_of_next_word.append(next_word)
                    map_to_nexttoken.set(current_word, list_of_next_word)
                    map_to_frequency.set(key_for_frequency, 1)
                    break
        else:
            map_to_nexttoken.set(current_word, [next_word])
            key_for_frequency = str(current_word) + "-" + str(next_word)
            map_to_frequency.set(key_for_frequency, 1)
        # # this is for checking. delete later
        # list_of_next_word = map_to_nexttoken.get(current_word)
        # print("list_of_next_word (after): ", list_of_next_word)
        # for pair_nextword in list_of_next_word:
        #     current_and_nextword_as_key = str(current_word) + "-" + str(pair_nextword)
        #     pair_frequency = map_to_frequency.get(current_and_nextword_as_key)
        #     print("pair of next word and frequency:", current_and_nextword_as_key, pair_frequency)
        # print("================one loop finished====================")
    return(map_to_nexttoken, map_to_frequency)


def next_word_and_frequency(tuple_of_hashtable, current_word):
    # next_words_list1 = tuple_of_hashtable[0].keys()
    # next_words_list2 = tuple_of_hashtable[0].values()
    # next_words_list3 = tuple_of_hashtable[1].keys()
    # next_words_list4 = tuple_of_hashtable[1].values()
    # print(next_words_list1)
    # print(next_words_list2)
    # print(next_words_list3)
    # print(next_words_list4)
    list_of_tuple_of_next_word_and_frequency = []
    list_of_next_word = tuple_of_hashtable[0].get(current_word)
    print("current_word: ", current_word)
    print("list_of_next_word: ", list_of_next_word)
    for next_word in list_of_next_word:
        current_and_nextword_as_key = str(current_word) + "-" + str(next_word)
        next_frequency = tuple_of_hashtable[1].get(current_and_nextword_as_key)
        list_of_tuple_of_next_word_and_frequency.append((next_word, next_frequency))
    return(list_of_tuple_of_next_word_and_frequency)



def random_walk(tuple_of_hashtable, words_list, tweet_length):
    output_words = []
# start from any one word
    list_wo_end = words_list[:-1]  # avoid end word
    initial_word = random.choice(list_wo_end)
    output_words.append(initial_word)
    # while words_list.index(initial_word) == len(words_list) - 1:
    #     initial_word = random.choice(xxxx)
# pick the list of next words & probability
# FIXME this is test. you can choose the number of words you choose
    for i in range(0, tweet_length):
        print("========================================")
        list_for_next = next_word_and_frequency(tuple_of_hashtable, initial_word)
        list_for_next_rev = []  # will revise for randint
# define the length of radint
        probability_index_initial = 0
        for next_tuple in list_for_next:
            probability_index_end = probability_index_initial + next_tuple[1]
            list_for_next_rev.append((next_tuple[0], probability_index_end))
            probability_index_initial = probability_index_end
# choose by random.randint
        random_index = random.randint(1, probability_index_end)
        print("random_index: ", random_index)
        range_initial = 0
        for i in range(0, len(list_for_next_rev)):
            # range_end = range_initial + list_for_next_rev[i][1]
            range_end = list_for_next_rev[i][1]
            print("range_initial: ", range_initial)
            print("list_for_next_rev[i][1]: ", list_for_next_rev[i][1])
            print("range_end(sum): ", range_end)
            if range_initial < random_index and random_index <= range_end:
                next_word = list_for_next_rev[i][0]
                print("if")
                break
            else:
                range_initial = range_end
                print("else")
# add to output_words
        output_words.append(next_word)
        if words_list[-1] == next_word:
            initial_word = random.choice(list_wo_end)
        else:
            initial_word = next_word
# choose next(for loop)
    return(output_words)


if __name__ == '__main__':
    # FIXME this corpus is for test. After the test, change corpus_obama.txt
    filename = "corpus.txt"
    words_list = parsing_tokenizing_byRE.parsing(filename)
    print(words_list)
    tuple_of_hashtable = store_to_hashtable(words_list)
    tweet_length = 20
    output_words = random_walk(tuple_of_hashtable, words_list, tweet_length)
    print(' '.join(output_words))

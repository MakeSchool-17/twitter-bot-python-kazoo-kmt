# Learn a Markov chain from a corpus
import hash_table
import parsing_tokenizing_byRE
import random


def store_to_hashtable(words_list):
    map_to_nexttoken = hash_table.HashTable()  # make hashtable which maps current token to next token
    map_to_frequency = hash_table.HashTable()  # make hashtable which maps next token to frequency
    for index in range(0, len(words_list) - 1):  # stop at the end of next_word
        current_word = words_list[index]
        next_word = words_list[index + 1]
        if map_to_nexttoken.get(current_word) is not None:
            list_of_next_word = map_to_nexttoken.get(current_word)
        else:
            list_of_next_word = None
        if list_of_next_word is not None:
            for word_in_list in list_of_next_word:
                if word_in_list == next_word:
                    key_for_frequency = str(current_word) + "-" + str(word_in_list)
                    updated_frequency = map_to_frequency.get(key_for_frequency) + 1
                    map_to_frequency.update(key_for_frequency, updated_frequency)
                    break
                else:
                    key_for_frequency = str(current_word) + "-" + str(next_word)
                    list_of_next_word.append(next_word)
                    map_to_nexttoken.set(current_word, list_of_next_word)
                    map_to_frequency.set(key_for_frequency, 1)
                    break
        else:
            map_to_nexttoken.set(current_word, [next_word])
            key_for_frequency = str(current_word) + "-" + str(next_word)
            map_to_frequency.set(key_for_frequency, 1)
    return(map_to_nexttoken, map_to_frequency)


def next_word_and_frequency(tuple_of_hashtable, current_word):
    list_of_tuple_of_next_word_and_frequency = []
    list_of_next_word = tuple_of_hashtable[0].get(current_word)
    for next_word in list_of_next_word:
        current_and_nextword_as_key = str(current_word) + "-" + str(next_word)
        next_frequency = tuple_of_hashtable[1].get(current_and_nextword_as_key)
        list_of_tuple_of_next_word_and_frequency.append((next_word, next_frequency))
    return(list_of_tuple_of_next_word_and_frequency)


def random_walk(tuple_of_hashtable, words_list, tweet_length):
    output_words = []
    list_wo_end = words_list[:-1]  # avoid end word
    initial_word = random.choice(list_wo_end)
    output_words.append(initial_word)
    for i in range(0, tweet_length):
        list_for_next = next_word_and_frequency(tuple_of_hashtable, initial_word)
        list_for_next_rev = []  # will revise for randint
        probability_index_initial = 0
        for next_tuple in list_for_next:
            probability_index_end = probability_index_initial + next_tuple[1]
            list_for_next_rev.append((next_tuple[0], probability_index_end))
            probability_index_initial = probability_index_end
        random_index = random.randint(1, probability_index_end)
        range_initial = 0
        for i in range(0, len(list_for_next_rev)):
            range_end = list_for_next_rev[i][1]
            if range_initial < random_index and random_index <= range_end:
                next_word = list_for_next_rev[i][0]
                break
            else:
                range_initial = range_end
        output_words.append(next_word)
        if words_list[-1] == next_word:
            initial_word = random.choice(list_wo_end)
        else:
            initial_word = next_word
    return(output_words)


if __name__ == '__main__':
    # PLEASE SET THE CORPUS.txt AND TWEET LENGTH
    filename = "corpus.txt"
    words_list = parsing_tokenizing_byRE.parsing(filename)
    print(words_list)
    tuple_of_hashtable = store_to_hashtable(words_list)
    tweet_length = 20
    output_words = random_walk(tuple_of_hashtable, words_list, tweet_length)
    print(' '.join(output_words))

import random
import sys #to get argv


def random_python_rearrange(input_words,number_of_output_words):
    # create an empty list
    list_of_words = []
    #shuffle(list_of_words)
    #print(number_of_output_words)

    # create a loop that will run number_of_output_words times
    for i in range(0,number_of_output_words): #exclusive
        # print(i)
        # generate random_index from 0 to len(input_words)
        random_index = random.randint(0,len(input_words) -1)
        # use random_index to grab word from input_words
        # add grabbed word to list
        # list_of_words[i] = input_words[random_index]
        list_of_words.append(input_words[random_index])
        # remove the word from input_words
        input_words.pop(random_index)
        #print(list_of_words)
    # return the rearranged word list
    return (' '.join(list_of_words))

#    rand_index = random.randint(0, lenRearrangements -1)
#    # choose the number randomly then insert them to the tuples?
#    return rearrangements[rand_index]
#    # then return the new order's numbers


if __name__ == '__main__':#start from here
    #print(shuffle(sys.argv))
    rearrangements = sys.argv #to get the list from command line
#    print(rearrangements)
    rearrangements = sys.argv[1:]
    lenRearrangements = len(rearrangements) #to get the number of arguments
#    print(lenRearrangements)
    rearrange = random_python_rearrange(rearrangements, lenRearrangements)
    print(rearrange)

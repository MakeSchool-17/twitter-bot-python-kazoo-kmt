import random
import sys #to get argv


def random_python_rearrange(input_words,number_of_output_words):
    # create an empty list
    list_of_words = []

    # create a loop that will run number_of_output_words times
    for i in range(0,number_of_output_words): #exclusive
        random_index = random.randint(0,len(input_words) -1)
        list_of_words.append(input_words[random_index])
        input_words.pop(random_index)
    return (' '.join(list_of_words))


if __name__ == '__main__':#start from here
    rearrangements = sys.argv #to get the list from command line
    rearrangements = sys.argv[1:]
    lenRearrangements = len(rearrangements) #to get the number of arguments
    rearrange = random_python_rearrange(rearrangements, lenRearrangements)
    print(rearrange)

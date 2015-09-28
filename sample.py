import sys
import random

def sample(filename):
    text_file = open(filename, "r")
    list_of_words = text_file.read().split()
    random.shuffle(list_of_words)
    random_index = random.randint(0, len(list_of_words) - 1)
    # print(list_of_words[random_index])
    return(list_of_words[random_index])
    
if __name__ == '__main__':
    filename = sys.argv[1]
    print(sample(filename))

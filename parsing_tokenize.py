# parsing and tokenize
import re
FILENAME = "corpus.txt"

def parsing():
    source_text = open(FILENAME, "r")
    words_incl_mark = source_text.read()
    # mark = re.compile(r"[^a-zA-Z0-9]\-\'")
    # words_wo_mark = mark.sub(" ", words_incl_mark)
    mark = re.compile(r"[a-zA-Z0-9]+[,|’|'|:|\.|\-]?[a-zA-Z0-9]+")
    words_wo_mark = mark.findall(words_incl_mark)
    return(words_wo_mark)
    # words_list = words_wo_mark.split()
    # print(words_list)
    # words_wo_mark_wo_upper = words_wo_mark.lower()
    # words_list = words_wo_mark_wo_upper.split()
    # return(words_list)

    # words_dictionary = {}
    # for words_key in words_list:
    #     words_dictionary[words_key] = words_dictionary.get(words_key, 0) + 1
    # return(words_dictionary)



if __name__ == '__main__':
    # print("=========NEW TEST==========")
    parsing()

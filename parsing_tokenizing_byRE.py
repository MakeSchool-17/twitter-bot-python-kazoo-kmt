# parsing and tokenize
import re
FILENAME = "corpus_obama.txt"

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


if __name__ == '__main__':
    # print("=========NEW TEST==========")
    parsing()

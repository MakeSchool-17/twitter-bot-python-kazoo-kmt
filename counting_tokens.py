import hash_table
import parsing_tokenizing


if __name__ == '__main__':
    word_counts = hash_table.HashTable()
    words_list = parsing_tokenizing.parsing()
    print(hash_table.histogram(words_list))

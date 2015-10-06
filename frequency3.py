# linked list
import sys
import re
import timeit


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, key, value):
        key_value_pair = (key, value)
        new_node = Node(key_value_pair)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count


    def search(self, key):
        current = self.head
        found = False
        while current and found is False:
            data_key = current.data[0]
            if data_key == key:
                found = True
            else:
                current = current.next_node
        return current


    def update(self, key, value):
        current = self.search(key)
        if current is not None:
            current.data = (key, value)


    def get(self, key):
        current = self.search(key)
        if current is not None:
            return current.data[1]
        else:
            return None


def list(length):
    dict_words = '/usr/share/dict/words'
    words_str = open(dict_words, 'r').read()
    all_words = words_str.split("\n")
    return all_words[0:length]


def histogram(words):
    words_list = LinkedList()
    for word in words:
        node_for_test = words_list.search(word)
        if node_for_test is None:
            words_list.insert(word, 1)
        else:
            words_list.update(word, words_list.get(word) + 1)
    return words_list


def frequency(word, hgram):
    count = hgram.get(word)
    if count is not None:
        return count
    else:
        return 0


if __name__ == '__main__':
    hundred_words = list(100)
    ten_thousand_words = list(10000)

    hundred_hgram = histogram(hundred_words)
    ten_thousand_hgram = histogram(ten_thousand_words)

    hundred_search = hundred_words[1]
    ten_thousand_search = ten_thousand_words[1]

    stmt = "frequency('{}', hundred_hgram)".format(hundred_search)
    setup = "from __main__ import frequency, hundred_hgram"
    timer = timeit.Timer(stmt, setup=setup)

    iterations = 10000
    result = timer.timeit(number=iterations)
    print("frequency() time for 100-word histogram: " + str(result))

    stmt = "frequency('{}', ten_thousand_hgram)".format(ten_thousand_search)
    setup = "from __main__ import frequency, ten_thousand_hgram"
    timer = timeit.Timer(stmt, setup=setup)

    iterations = 10000
    result = timer.timeit(number=iterations)
    print("frequency() time for 10,000-word histogram: " + str(result))

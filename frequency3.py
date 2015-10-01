# This is 3. linked list in tutorial5
# Stacked..........Need advice from instrudtor
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
    def __int__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.data == data:
                found = True
            else:
                current = current.next_node
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


    def list(length):
        dict_words = '/usr/share/dict/words'
        words_str = open(dict_words, 'r').read()
        all_words = words_str.split("\n")
        return all_words[0:length]


    def histogram(words):
        words_list = LinkedList()
        for word in words:
            current = self.head
            found = False
            while current and found is False:
                if current.data == data:
                    found = True
                    before_add = words_list.get_data(word)
                    count = before_add[1]
                    words_list.data = (word, count + 1)
                else:
                    current = current.next_node
            if current is None:
                    words_list.insert((word, 1))
        return words_list


    def frequency(word, hgram):
        found = False
        while hgram and found is False:
            if hgram.data == word:
                found = True
                count = hgram.data[1]
                return count
            else:
                hgram = hgram.next_node
        if hgram is None:
            return 0


if __name__ == '__main__':
    hundred_words = LinkedList.list(100)
    ten_thousand_words = LinkedList.list(10000)

    hundred_hgram = LinkedList.histogram(hundred_words)
    ten_thousand_hgram = linkedList.histogram(ten_thousand_words)

    print(hundred_hgram)

'''
    hundred_search = hundred_words[-1]
    ten_thousand_search = ten_thousand_words[-1]

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
'''

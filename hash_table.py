import sys
import re
import timeit


class HashTable(Object):
    def get(key):
        pass

    def set(key, value):
        pass

    def update(key, value):
        pass

    def keys():
        pass

    def values():
        pass


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

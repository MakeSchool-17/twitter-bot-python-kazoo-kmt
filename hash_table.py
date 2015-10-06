class HashTable(object):
    def __init__(self):
        self.size = 8
        self.bucket = []
        for i in range(self.size):
            self.bucket.append(LinkedList())

    def set(self, key, value):
        bucket_number = hash(key) % self.size
        print(bucket_number)
        self.bucket[bucket_number].append(key, value)

    def get(self, key):
        for i in range(0, self.size):
            value = self.bucket[i].get(key)
            if value is not None:
                break
        return value

    def update(self, key, value):
        for i in range(0, self.size):
            self.bucket[i].update(key, value)

    def keys(self):
        keys_list = []
        for i in range(0, self.size):
            new_key = self.bucket[i].head
            while new_key:
                keys_list.append(new_key.data[0])
                new_key = new_key.next
        return keys_list

    def values(self):
        values_list = []
        for i in range(0, self.size):
            new_value = self.bucket[i].head
            while new_value:
                values_list.append(new_value.data[1 ])
                new_value = new_value.next
        return values_list


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        head_str = 'head: ' + str(self.head) if self.head else ''
        tail_str = ', tail: ' + str(self.tail) if self.tail else ''
        return 'LinkedList({}{})'.format(head_str, tail_str)

    def head(self):
        self.head = head

    def tail(self):
        self.tail = tail

    def append(self, key, value):
        # Node()
        key_value_pair = (key, value)
        new_node = Node(key_value_pair, None)
        previous_node = self.tail
        if previous_node is not None:
            previous_node.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert(self, key, value):
        key_value_pair = (key, value)
        new_node = Node(key_value_pair)
        new_node.set_next(self.head)
        self.head = new_node

    def find(self, key):
        current_node = self.head
        found = False
        while current_node and found is False:
            data_key = current_node.data[0]
            if data_key == key:
                found = True
            else:
                current_node = current_node.next
        return current_node

    def get(self, key):
        current_node = self.find(key)
        if current_node is not None:
            return current_node.data[1]
        else:
            return None

    def delete(self, key):
        current_node = self.head
        previous_node = None
        found = False
        while current_node and found is False:
            if current_node.data[0] == key:
                found = True
            else:
                previous_node = current_node
                current_node = current_node.next
        if current_node is None:
            raise ValueError("Key not in list")
        if previous_node is None:
            self.head = current_node.next
        else:
            previous_node = current_node.next

    def update(self, key, value):
        current_node = self.find(key)
        if current_node is not None:
            current_node.data = (key, value)


def list(length):
    dict_words = '/usr/share/dict/words'
    words_str = open(dict_words, 'r').read()
    all_words = words_str.split("\n")
    return all_words[0:length]


def histogram(words):
    words_list = LinkedList()
    for word in words:
        node_for_test = words_list.find(word)
        if node_for_test is None:
            words_list.append(word, 1)
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
    roman = HashTable()
    roman.set('I', 2)
    roman.get('I')          # => 1
    print(roman.get('I'))
    roman.set('V', 5)
    roman.set('X', 9)
    roman.update('X', 10)   # Oops, let's fix that.
    roman.get('X')          # => 10
    print(roman.get('X'))          # => 10
    roman.keys()            # => ['I', 'V', 'X']
    print(roman.keys())            # => ['I', 'V', 'X']
    roman.values()
    print(roman.values())

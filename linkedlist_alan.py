#!/usr/local/bin/python3


class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        has_next = ', has next' if self.next else ''
        return 'Node({}{})'.format(self.data, has_next)
        # don't do this, you could fill the stack with recursion!
        # return 'Node({}, {})'.format(self.data, self.next)


class LinkedList(object):

    def __init__(self):
        # empty LinkedList
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        head_str = 'head: ' + str(self.head) if self.head else ''
        tail_str = ', tail: ' + str(self.tail) if self.tail else ''
        return 'LinkedList({}{})'.format(head_str, tail_str)

    def is_empty(self):
        return self.size == 0

    def is_valid(self):
        head_good = self.head is not None
        tail_good = self.tail is not None
        size_good = self.size > 0
        if head_good and tail_good and size_good:
            return True
        elif not head_good and not tail_good and not size_good:
            return True
        else:
            return False

    def insert_at_head(self, data):
        # create a new node with the data
        new_node = Node(data)
        new_node.next = self.head
        # reassign head reference
        self.head = new_node
        self.size += 1
        # assign tail reference if list is empty
        if self.tail is None:
            self.tail = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            # assign head reference
            self.head = new_node
        else:
            # append new node after tail
            self.tail.next = new_node
        # reassign tail reference
        self.tail = new_node
        self.size += 1

    def remove_head(self):
        if self.head is None:
            raise ValueError('List is empty')
        self.head = self.head.next
        self.size -= 1

    # running time: O(n)
    def calculate_size(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count


def test_node():
    print('==== Node class tests =====')
    node1 = Node({'Alan': 4})
    print('node1:', node1)
    node2 = Node(['Abe', 'Ignat'])
    print('node2:', node2)
    node1.next = node2
    node2.next = node1
    print('node1:', node1)
    print('node2:', node2)


def test_linked_list():
    def check_linked_list(ll):
        print('ll:', ll)
        print('ll.is_valid:', ll.is_valid())
        print('ll.calculate_size:', ll.calculate_size())
        print('ll.size:', ll.size)

    print('==== LinkedList class tests =====')
    ll = LinkedList()
    check_linked_list(ll)

    try:
        ll.remove_head()
    except ValueError as error:
        print('Could not remove head, error:', error)
    check_linked_list(ll)

    ll.insert_at_head('hello')
    check_linked_list(ll)

    ll.insert_at_head('goodbye')
    check_linked_list(ll)

    ll.insert_at_tail('the end')
    check_linked_list(ll)

    ll.remove_head()
    check_linked_list(ll)


if __name__ == '__main__':
    test_node()
    test_linked_list()

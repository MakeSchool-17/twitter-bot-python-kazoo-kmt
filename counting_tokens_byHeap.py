import hash_table
import parsing_tokenizing

class Heap(object):
    def __init__(self):
        self.size = 0
        self.list = [None]
        # self.list = [None, (3, "the"), (2, "a"), (1, "b")]

    def __str__(self):
        return 'Heap(List:{})'.format(self.list)

    def get_size(self):
        self.size = len(self.list)
        return(self.size)

    # def get_index(self, count, word):
    #     for i in range(1, self.size):  # skip None
    #         if self.list[i][0] == count and self.list[i][1] == word:
    #             return(i)
    #     return None

    def peek(self):  # inspect the root node
        if self.get_size() > 1:
            return(self.list[1])
        else:
            return None

    def insert(self, count_and_word):  # add a new node
        current_index = self.get_size()  # insert at the last of the list
        self.list.append(count_and_word)
        self.size += 1
        if current_index > 1:
            parent_index = current_index // 2
            current_node = self.list[current_index]
            parent_node = self.list[parent_index]
            # [brian] The `and parent_node is not None` part is superfluous.
            # If it's None you'll have already gotten a TypeError :)
            while current_node[0] > parent_node[0] and parent_node is not None:
                self.swap(current_index, parent_index)
                current_index = parent_index
                parent_index = current_index // 2
                if parent_index == 0:
                    break
                else:
                    current_node = self.list[current_index]
                    parent_node = self.list[parent_index]
        else:
            pass

    def swap(self, index_target_child, index_target_parent):  #just switch two nodes
        target_child = self.list[index_target_child]
        target_parent = self.list[index_target_parent]
        self.list[index_target_parent] = target_child
        self.list[index_target_child] = target_parent

    def delete_max(self):  # remove the root node (internally, heap will need to be balanced)
        self.list.pop(1)
        self.size -= 1
        current_index = 1
        child_index_1 = current_index * 2
        child_index_2 = current_index * 2 + 1
        if self.list[child_index_2] is not None:
            child_index = max(child_index_1, child_index_2)
        else:
            child_index = child_index_1
        # if self.get_size() > 2:
        while self.list[current_index][0] < self.list[child_index][0]:
            swap(current_index, child_index)
            current_index = child_index
            child_index_1 = current_index * 2
            child_index_2 = current_index * 2 + 1
            if self.list[child_index_2] is not None:
                child_index = max(child_index_1, child_index_2)
            else:
                child_index = child_index_1


if __name__ == '__main__':
    # word_counts = hash_table.HashTable()
    # words_list = parsing_tokenizing.parsing()
    # print(hash_table.histogram(words_list))

    counts = Heap()             # create a new heap
    test = counts.get_size()
    counts.insert((3, "the"))   # insert some tuples of count/word pairs
    counts.insert((2, "dog"))
    counts.insert((1, "apple"))
    counts.insert((5, "red"))
    counts.insert((1, "ate"))
    # print("=====Check the contents of the list=====\n", counts)
    counts.peek()               # => (5, "red")
    # print("counts.get_size(): ", counts.get_size())
    counts.delete_max()         # => (5, "red")
    # print("counts.get_size(): ", counts.get_size())
    counts.peek()               # => (3, "the")
    # print(counts.peek())

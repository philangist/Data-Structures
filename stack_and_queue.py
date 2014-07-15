from linked_lists import Node


class Queue(object):

    def __unicode__(self):
        return '<Queue: %s>' % self.items

    def __str__(self):
        return self.__unicode__().encode('UTF-8')

    __repr__ = __str__

    def __init__(self):
        self.items = {}
        self.head_pointer = 0
        self.tail_pointer = 0

    def pop(self):
        if not (self.head_pointer and self.items):
            return None

        item = self.items.pop(self.head_pointer)
        self.pointer -= 1
        return  item

    def push(self, item):
        self.tail_pointer += 1
        self.items[self.tail_pointer] = item


class Stack(object):

    def __unicode__(self):
        return '<Stack: %s>' % self.items

    def __str__(self):
        return self.__unicode__().encode('UTF-8')

    __repr__ = __str__

    def __init__(self):
        self.items = []
        self.frame = 0  # for bookkeeping and debugging

    def pop(self):
        data = None

        if self.items:
            data = self.items[self.frame]
            self.frame -= 1

        return data

    def push(self, data):
        self.values.append(data)
        self.frame += 1


class LinkedListStack(object):

    def __unicode__(self):
        return '<LinkedListStack: %s>' % self.data

    def __str__(self):
        return self.__unicode__().encode('UTF-8')

    __repr__ = __str__

    def __init__(self):
        self.head = None

    def push(self, data):
        head = Node(data)
        head.next = self.head
        self.head = head

    def pop(self):
        data = None
        if self.head:
            data = self.head.data

        return data

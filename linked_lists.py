class Node(object):

    def __unicode__(self):
        return u'%s(data: %s)' % (self.__class__.__name__, self.data)
    __str__ = __unicode__
    __repr__ = __unicode__

    def __init__(self, data=None):
        self.next = None
        self.data = data

    def append_to_tail(self, value):
        new_node = Node(value)
        cur_node = self
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node
        return new_node

    def delete_node_from_list(self, data):
        head = self
        if head.data == data:
            return head.next
        while head.next:
            if head.next.data == data:
                head.next = head.next.next
            else:
                head = head.next
        return head

    def remove_duplicates(self):
        head = self
        if not head.next:
            return head
        seen_data = set()
        while head.next:
            if head.next.data in seen_data:
                head.next = head.next.next
            else:
                seen_data.add(head.next.data)
                head = head.next
        return head

    def walk_list(self):
        head = self
        output = ''
        if not head.next:
            return head.data
        while head:
            output += '%s, ' % head.data
            head = head.next
        return output[:-2]


def recursively_remove_duplicates(head, seen_data=set()):
    print 'head is %s, seen_data is %s ' % (head, seen_data)

    if not head.next:
        if head.data in seen_data:
            head = None
        return head

    if head.data in seen_data:
        head = recursively_remove_duplicates(head.next, seen_data)
    else:
        seen_data.add(head.data)
        head.next = recursively_remove_duplicates(head.next, seen_data)

    return head


def convert_linked_list_to_integer(head):
    if not head.next:
        return head.data

    place = 0
    total = 0

    while head:
        total += head.data * (10 ** place)
        head = head.next
        place += 1

    return total

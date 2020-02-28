from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None            # the marker/pointer
        self.storage = DoublyLinkedList()

        # adds items to the buffer
    def append(self, item):
        # let's define the base cases
        # if there are less items then the capacity, we can simply add an item
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        # however, if the storage is full to the capacity
        elif len(self.storage) == self.capacity:
            # remove the oldest entry i.e. head
            oldest = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            # reset the position again:
            if oldest == self.current:
                self.current = self.storage.tail


        # returns the elements in order, does not return any None values.
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # let's get a starting point
        first = self.current
        # we append that value
        list_buffer_contents.append(first.value)
        # if there is a value next to the first
        if first.next:
            next_one = first.next
        else:
            next_one = self.storage.head
        # keep adding the items while the next_one is not equal to first
        while next_one != first:
            list_buffer_contents.append(next_one.value)
            if next_one.next:                # set the next_one
                next_one = next_one.next
            else:
                next_one = self.storage.head    # at the end, we go to head
        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        # self.storage = []
        pass

    def append(self, item):
        pass

    def get(self):
        pass

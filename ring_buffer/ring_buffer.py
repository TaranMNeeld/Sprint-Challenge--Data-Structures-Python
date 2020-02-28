from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.head is None:
            self.storage.add_to_head(item)
            self.current = self.storage.head
            print(f'set head value to: {item}, set current to: {self.current.value}')
        else:
            if self.storage.length == self.capacity:
                print(f'tail: {self.storage.tail.value}, current: {self.current.value}')
                if self.current == self.storage.tail:
                    self.storage.head.value = item
                    self.current = self.storage.head
                else:
                    self.current.next.value = item
                    self.current = self.current.next
                    print(f'set current to: {self.current.value}, storage len: {self.storage.length}')
            else:
                self.storage.length += 1
                self.current.insert_after(item)
                self.current = self.current.next
                self.storage.tail = self.current
                print(f'set current to: {self.current.value}, storage len: {self.storage.length}')

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # TODO: Your code here
        current_node = self.storage.head
        while current_node is not None:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next
        print(list_buffer_contents)
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

class node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prvs_node = None

    def __repr__(self):
        return str(self.value)



class linked_list:
    def __init__(self, arg=None):
        self.length = 0
        self.head = None
        self.tail = None
        if arg:
            for val in arg:
                self.append(val)

    def prepend(self, value):
        before = self.head
        self.head = node(value)
        before.prvs_node = self.head
        self.head.next_node = before
        self.length += 1

    def append(self, value):
        n = node(value)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next_node = n
            last = self.tail
            self.tail = n
            self.tail.prvs_node = last
        self.length += 1

    def get(self, pos):
        current = self.head
        count = 0
        while current:
            if count == pos:
                return current.value
            current = current.next_node
            count += 1
        raise IndexError

    def insert(self, value, pos=None):
        if pos > self.length:
            raise IndexError
        if pos == self.length:
            self.append(value)
            return
        if pos is None or pos == 0:
            self.prepend(value)
            return
        current = self.head
        count = 0
        while current:
            if count == pos:
                before = current.prvs_node
                new = node(value)
                new.prvs_node = before
                before.next_node =current.prvs_node = new
                new.next_node = current
                self.length += 1
                return
            current = current.next_node
            count += 1

    def pop(self):
        before = self.tail.prvs_node
        before.next_node = None
        val=self.tail.value
        del self.tail
        self.tail = before
        self.length -= 1
        return val


    def delete(self, pos=None):
        if pos is None:
            self.pop()
        elif pos >= self.length or pos < 0:
            raise IndexError
        elif pos == 0:
            current = self.head.next_node
            val=self.head.value
            self.head = current
            self.length -= 1
            return val
        else:
            current = self.head
            count = 0
            while current:
                if count == pos:
                    before = current.prvs_node
                    next = current.next_node
                    before.next_node = next
                    next.prvs_node = before
                    del current
                    self.length -= 1
                    break
                current = current.next_node
                count += 1

    def __repr__(self):
        current = self.head
        output = list()
        while current:
            output.append(str(current.value))
            current = current.next_node
        return " , ".join(output)

    def __len__(self):
        return self.length

    def __add__(self, other):
        self.append(other)

    def __iter__(self):
        self.count=0
        self.current_node=self.head
        return self

    def __next__(self):
        if self.count == self.length:
            self.count = 0
            self.current_node = self.head
            raise StopIteration
        else:
            val =self.current_node.value
            self.current_node=self.current_node.next_node
            return val

    def __getitem__(self, key):
        self.get(key)

    def __setitem__(self, key, value):
        if key >=self.head:
            raise IndexError
        current = self.head
        count = 0
        while current:
            if count == key:
                current.value=value
                return
            current = current.next_node
            count += 1







if __name__ == '__main__':
    ln = linked_list([1, 2, 3, 4, 5, 6, 7])
    ln.append(100)
    ln.insert(30, 1)
    ln.prepend(200)
    ln.delete()
    print(f"{len(ln) = }")
    print(f"{ln.get(10) = }")

    print(ln)

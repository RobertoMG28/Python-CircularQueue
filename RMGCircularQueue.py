class CircularQueue:

    def __init__(self, total_size):
        self.__data = [None] * total_size
        self.__total_size = total_size
        self.__size = 0
        self.__first = 0
        self.__rear = 0
    
    def __str__(self):
        return str(self.__data)

    def enqueue(self, element):
        assert not self.is_full()
    
        self.__size += 1
        self.__data[self.__rear] = element
        self.__rear = (self.__rear + 1) % self.__total_size

    def dequeue(self):
        assert not self.is_empty()

        self.__size -= 1
        element = self.__data[self.__first]
        self.__data[self.__first] = None
        self.__first = (self.__first + 1) % self.__total_size

        return element

    def is_empty(self) -> bool:
        return self.__size == 0

    def is_full(self) -> bool:
        return self.__size == self.__total_size


# Implementation Examples
test_object = CircularQueue(5)

test_object.enqueue(2)
print(test_object)

test_object.enqueue(31)
print(test_object)

test_object.dequeue()
print(test_object)

test_object.enqueue(32)
print(test_object)

test_object.enqueue(33)
print(test_object)

test_object.enqueue(34)
print(test_object)

test_object.dequeue()
print(test_object)

test_object.enqueue(35)
print(test_object)
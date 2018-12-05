'''
    - Circular Queue is an extension of queue with following properties
        - Operations are performed based on FIFO (First In First Out)
        - Last position in the queue is connected back to the first position
        - Also called as 'Ring Buffer'
    - Priority Queue operations:
        - Enqueue O(1)
        - Dequeue O(1)
    - Applications:
        - CPU Scheduling
        - Automated Traffic control systems
        - Memory Management
'''

class UnderflowException(Exception):
    pass

class OverflowException(Exception):
    pass

class CircularQueue(object):
    def __init__(self, capacity):
        self.__rear     = -1
        self.__front    = -1
        self.__size     = 0
        self.__capacity = capacity
        self.__queue    = [None] * self.__capacity

    def __str__(self):
        return ', '.join([str(i) for i in self.__queue])

    def is_empty(self):
        return self.__size == 0

    def is_full(self):
        return self.__size == self.__capacity

    def enqueue(self, element):
        '''
            :param element: element to be inserted (enqueued) in the queue
        '''
        if self.is_full():
            self.__rear = -1
        self.__rear += 1
        self.__size += 1
        self.__queue[self.__rear] = element

    def dequeue(self):
        '''
            :return: popped element from the front of queue
        '''
        if self.is_empty():
            raise UnderflowException
        self.__front += 1
        return self.__queue[self.__front]

    def get_rear(self):
        '''
            :return: rear element from the queue
        '''
        return self.__rear

    def get_front(self):
        '''
            :return: front element from the queue
        '''
        return self.__front

if __name__ == '__main__':
    queue = CircularQueue(10)       # Queue with capacity of 10 elements
    for i in range(12):             # We are inserting 12 elements
        queue.enqueue(i)

    print(queue)                    # 10, 11, 2, 3, 4, 5, 6, 7, 8, 9
    print(queue.dequeue())          # 10
    print(queue)
    print(queue.dequeue())          # 11
    print(queue)
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from queue.queue import Queue

'''
    Algorithm:
        - First we dequeue all the elements from queue one and enqueue them in queue two
        - Once queue one is empty we enqueue the current element in the queue one
        - We then again dequeue all the elements from queue two and enqueue them back in queue one
        - This way, the element that is entered currently will occupy the first element in the queue
        - Time complexity of this operation is O(n) and pop will be O(1)
        - Same can be done with pop, in that case time complexity of push will be O(1)
'''

class StackUsingQueue(object):
    def __init__(self):
        self._queue_one = Queue()
        self._queue_two = Queue()
    
    def __str__(self):
        return self._queue_one.__str__()

    def push(self, element):
        '''
            :param element: element to be pushed onto stack
        '''
        while not self._queue_one.is_empty():
            self._queue_two.enqueue(self._queue_one.dequeue())

        self._queue_one.enqueue(element)

        while not self._queue_two.is_empty():
            self._queue_one.enqueue(self._queue_two.dequeue())
        return

    def pop(self):
        return self._queue_one.dequeue()

if __name__ == '__main__':
    stack = StackUsingQueue()
    for i in range(10):
        stack.push(i)
    print(stack)
    print(stack.pop())
    print(stack)
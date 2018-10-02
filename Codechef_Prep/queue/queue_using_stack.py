import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from stack.stack import Stack

'''
    Algorithm:
        - First we pop all the elements from stack one and store them in stack two
        - Once stack one is empty we push the current element in the stack one
        - We then again pop all the elements from stack two and push them back in stack one
        - This way, the element that is entered currently will occupy the last element in the stack
        - Time complexity of this operation is O(n) and dequeue will be O(1)
        - Same can be done with dequeue, in that case time complexity of enqueue will be O(1)
'''

class UnderflowException(Exception):
    pass

class QueueUsingStack(object):
    def __init__(self):
        self._stack_one = Stack()
        self._stack_two = Stack()
    
    def __str__(self):
        return self._stack_one.__str__()
    
    def enqueue(self, element):
        '''
            :param element: element to be enqueued in the queue
        '''
        while not self._stack_one.is_empty():
            self._stack_two.push(self._stack_one.pop())
        
        self._stack_one.push(element)

        while not self._stack_two.is_empty():
            self._stack_one.push(self._stack_two.pop())
        return

    def dequeue(self):
        if self._stack_one.is_empty():
            raise UnderflowException
        return self._stack_one.pop()

if __name__ == '__main__':
    queue = QueueUsingStack()
    for i in range(10):
        queue.enqueue(i)
    print(queue)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue)
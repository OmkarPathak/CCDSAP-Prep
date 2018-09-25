'''
    - Stack is a linear data structure which follows a particular order in which the operations are performed
    - The order may be LIFO(Last In First Out) or FILO(First In Last Out)
    - Stack operations:
        - Push
        - Pop
        - Empty
'''

class UnderflowException(Exception):
    pass

class OverflowException(Exception):
    pass

class Stack(object):
    def __init__(self):
        self._stack = []
        self.top = -1

    def __str__(self):
        return ', '.join([str(i) for i in self._stack])

    def push(self, element):
        '''
            :param element: data element to be pushed onto stack
        '''
        self._stack.append(element)
        self.top += 1
        return

    def pop(self):
        '''
            pops the topmost element from stack
        '''
        if not self.is_empty():
            self.top -= 1
            value = self._stack[self.top + 1]
            del self._stack[self.top + 1]
            return value
        else:
            raise UnderflowException

    def is_empty(self):
        '''
            returns True if stack is empty else returns false
        '''
        return len(self._stack) == 0

    def peek(self):
        '''
            returns the top element from the stack
        '''
        return self._stack[self.top]
        
if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack)
    print(stack.top)
    stack.pop()
    stack.pop()
    print(stack)

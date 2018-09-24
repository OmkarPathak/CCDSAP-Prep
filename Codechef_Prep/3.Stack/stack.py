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
        self._S = []
        self.top = -1

    def push(self, element):
        self._S.append(element)
        self.top += 1
        return

    def pop(self):
        if not self.is_empty():
            self.top -= 1
            value = self._S[self.top + 1]
            del self._S[self.top + 1]
            return value
        else:
            raise UnderflowException

    def is_empty(self):
        return len(self._S) == 0

    def __str__(self):
        return ', '.join([str(i) for i in self._S])
        
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
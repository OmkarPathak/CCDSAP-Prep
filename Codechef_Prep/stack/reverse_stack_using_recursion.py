import stack

class ReverseStackUsingRecursion(object):
    def __init__(self, elements=[]):
        self._stack = stack.Stack()
        for element in elements:
            self._stack.push(element)
        self._reverse()

    def __str__(self):
        return self._stack.__str__()

    def _reverse(self):
        if not self._stack.is_empty():
            item = self._stack.pop()
            self._reverse()
            self._insert_at_bottom(item)
        return

    def _insert_at_bottom(self, item):
        if self._stack.is_empty():
            self._stack.push(item)
        else:
            temp_item = self._stack.pop()
            self._insert_at_bottom(item)
            self._stack.push(temp_item)
        return

if __name__ == '__main__':
    print(ReverseStackUsingRecursion([1, 2, 3, 4]))
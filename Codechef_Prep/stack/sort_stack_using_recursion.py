import stack

class SortStackUsingRecursion(object):
    def __init__(self, elements=[]):
        self._stack = stack.Stack()
        for element in elements:
            self._stack.push(element)
        self._sort()

    def __str__(self):
        return self._stack.__str__()

    def _sort(self):
        if not self._stack.is_empty():
            item = self._stack.pop()
            self._sort()
            self._sorted_insert(item)
        return

    def _sorted_insert(self, item):
        if self._stack.is_empty() or item > self._stack.peek():
            self._stack.push(item)
        else:
            temp_item = self._stack.pop()
            self._sorted_insert(item)
            self._stack.push(temp_item)
        return

if __name__ == '__main__':
    print(SortStackUsingRecursion([4, 2, 3, 1]))
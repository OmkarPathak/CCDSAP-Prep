'''
    -Priority Queue is an extension of queue with following properties
        - Every item has a priority associated with it
        - An element with high priority is dequeued before an element with low priority
        - If two elements have the same priority, they are served according to their order in the queue
    - Priority Queue operations:
        - Insertion O(n)
        - Deletion O(1)
'''

class UnderflowException(Exception):
    pass

class OverflowException(Exception):
    pass

class Node(object):
    def __init__(self, item, priority):
        '''
            :param item: The data to be stored in queue
            :param priority: Corresponding priority of the item 
        '''
        self.item       = item
        self.priority   = priority

class PriorityQueue(object):
    def __init__(self):
        self.__queue = list()

    def __str__(self):
        return ' '.join([str(i.item) for i in self.__queue])

    def is_empty(self):
        '''
            returns true of queue is empty else false
        '''
        return self.__queue == []

    def size(self):
        '''
            returns the number of elements in the queue
        '''
        return len(self.__queue)

    def insert(self, item, priority):
        '''
            :param item: The data to be stored in queue
            :param priority: Corresponding priority of the item 
        '''
        node = Node(item, priority)
        self.__queue.append(node)
        return

    def delete(self):
        '''
            :return: the item of type Node which has the highest priority amongst the elements in queue
        '''
        max = 0
        for index, current_node in enumerate(self.__queue):
            if self.__queue[index].priority > self.__queue[max].priority:
                max = index
        item = self.__queue[max]
        del self.__queue[max]
        return item        

if __name__ == '__main__':
    pqueue = PriorityQueue()
    pqueue.insert(1, 10)
    pqueue.insert(2, 9)
    print(pqueue)
    pqueue.delete()         # 1 will be deleted first as it has higher priority than 2
    print(pqueue)
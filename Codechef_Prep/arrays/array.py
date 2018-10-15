'''
    - Array is a collection of homogeneous data elements (means each array element has same data type)
    - Elements of array are stored in successive memory locations
    - Each array element can be accessed using index number
    - Array operations:
        - Accessing  O(1)
        - Insertion  O(n)
        - Deletion   O(n)
        - Sorting    O(n)
        - Searching  O(n)
'''

class Array(object):
    def __init__(self, data_type=int, size=0):
        '''
            Create an array of size 'size' with data type 'type'

            :param data_type: denotes the data type of each element in the array
            :param size: denotes the size of the array
        '''
        # all elements have to be in successive position hence we need to initialize the array with 0
        self.elements = [data_type(0)] * size
        self.array_size = size
        self.count = len(self.elements)

    def __str__(self):
        return '[' + ', '.join([str(i) for i in self.elements]) + ']'

    def __len__(self):
        '''
            returns the length of the array
        '''
        return self.count

    def __setitem__(self, index, value):
        '''
            to set an element in the array
        '''
        self.elements[index] = value

    def __getitem__(self, index):
        '''
            to retrieve an array element
        '''
        return self.elements[index]


if __name__ == '__main__':
    array = Array(int, 10)
    print(array)
    array[1] = 20
    print(array)


    
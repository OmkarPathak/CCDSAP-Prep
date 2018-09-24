'''
    Here we will see how to rotate array to left
'''

def method_one(array, d):
    '''
        :param array: Array on which rotation is to be performed
        :param d: number of elements that need to be rotated
        :return array: Modified array after rotation

        Time Complexity of this method: O(n)
    '''
    temp = array.copy()             # make a copy of the array so elements are not lost after rotation
    for i in range(len(array)):
        array[i - d] = temp[i]      # replace the elements say d = 2 and i = 0, then array[-2] = temp[0]

    return array

if __name__ == '__main__':
    test = [i for i in range(20)]
    print('Original Array:', test)
    print('Array after rotation:', method_one(test, 5))

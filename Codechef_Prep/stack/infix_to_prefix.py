'''
    Algorithm:
    - Reverse the string (infix)
    - Find the postfix of the reversed string
    - Again reverse the resultant string to get the prefix
'''
from infix_to_postfix import InfixToPostfix

class InfixToPrefix(object):
    def __init__(self, expression):
        self._expression = expression
        self._prefix = []
    
    def __str__(self):
        return ' '.join(self._prefix)

    @staticmethod
    def _reverse(string):
        '''
            function to reverse the given string
            :param string: expression to be reversed in string
        '''
        string = [string[i] for i in range(len(string) - 1, -1, -1)]
        reverse = []
        for char in string:
            if char == '(':
                reverse.append(')')
            elif char == ')':
                reverse.append('(')
            else:
                reverse.append(char)
        return reverse

    def infix_to_prefix(self):
        '''
            :return: prefix expression of type string
        '''
        infix = InfixToPostfix(self._reverse(self._expression)).infix_to_postfix()
        self._prefix = self._reverse(infix)
        return ''.join(self._prefix)

if __name__ == '__main__':
    intopre = InfixToPrefix('(a-b/c)*(a/k-l)')
    print(intopre.infix_to_prefix())
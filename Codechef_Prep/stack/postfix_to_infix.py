'''
    Algorithm:
    - For each literal or character in an expression:
        - If the literal is an operand, push it onto the stack
        - Else pop two operand from the stack, make a string by concatenating the 
          second_operand + operator + first_operand and push it back to stack
'''
import stack

class PostfixToInfix(object):
    def __init__(self, expression):
        '''
            :param expression: Expression in postfix form that needs to be converted to infix
        '''
        self._infix = []
        self._stack = stack.Stack()
        self._expression = expression

    def __str__(self):
        return ' '.join([i for i in self._infix[0]])
    
    @staticmethod
    def _is_operand(char):
        '''
            :param char: a single literal or character
        '''
        return (ord(char) >= ord('A') and ord(char) <= ord('Z')) or ((ord(char) >= ord('a') and ord(char) <= ord('z')))

    def postfix_to_infix(self):
        '''
            :return: infix expression of type string
        '''
        for char in self._expression:
            if self._is_operand(char):
                self._stack.push(char)
            else:
                first_operand = self._stack.pop()
                second_operand = self._stack.pop()
                self._stack.push(second_operand + char + first_operand)

        while not self._stack.is_empty():
            self._infix.append(self._stack.pop())

        return ''.join(self._infix)

if __name__ == '__main__':
    posttoin = PostfixToInfix('abcd^e-fgh*+^*+i-')
    posttoin.postfix_to_infix()
    print(posttoin)
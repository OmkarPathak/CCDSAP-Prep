'''
    Algorithm:
    - For each literal or character in an expression:
        - Check whether the literal is an operand or a operator
        - If it is operand push it on our final list
        - If it is equal to '(' operator then push that character onto stack
        - If it is equal to ')' operator, then pop the elements and append them in our final list
          till we encounter a '(' operator
        - Else check for its precedence with the operator on top of stack. If the operator 
          precedence is less than that the one on the top of stack then:
            - pop all the elements from the stack and append them to our final list and push the 
              current operator on to stack
    - At the end pop all the elements that are remaining in the stack
'''
import stack

class InfixToPostfix(object):
    def __init__(self, expression):
        '''
            :param expression: Expression in infix form that needs to be converted to postfix
        '''
        self._postfix = []
        self._stack = stack.Stack()
        self._expression = expression

    def __str__(self):
        return ' '.join(self._postfix)
    
    @staticmethod
    def _is_operand(char):
        '''
            :param char: a single literal or character
        '''
        return (ord(char) >= ord('A') and ord(char) <= ord('Z')) or ((ord(char) >= ord('a') and ord(char) <= ord('z')))

    @staticmethod
    def _precedence(char):
        '''
            :param char: a single literal or character
        '''
        if char == '+' or char == '-':
            return 1
        elif char == '*' or char == '/':
            return 2
        elif char == '^' or char == '**':
            return 3
        return -1

    def infix_to_postfix(self):
        '''
            :return: postfix expression of type string
        '''
        for char in self._expression:
            if(self._is_operand(char)):
                self._postfix.append(char)
            elif char == '(':
                self._stack.push(char)
            elif char == ')':
                top = self._stack.pop()
                while not self._stack.is_empty() and top != '(':
                    self._postfix.append(top)
                    top = self._stack.pop()
            else:
                while not self._stack.is_empty() and self._precedence(char) <= self._precedence(self._stack.peek()):
                    self._postfix.append(self._stack.pop())
                self._stack.push(char)

        while not self._stack.is_empty():
            self._postfix.append(self._stack.pop())
            
        return ''.join(self._postfix)

if __name__ == '__main__':
    intopost = InfixToPostfix('a+b*(c^d-e)^(f+g*h)-i')
    intopost.infix_to_postfix()
    print(intopost)
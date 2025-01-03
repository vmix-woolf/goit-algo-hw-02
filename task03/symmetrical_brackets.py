import re
from stack import Stack

class Check:
    def __init__(self):
        self.stack = Stack()

    def is_symmetrical(self, string: str) -> bool:
        for char in string:
            # handle only brackets
            if not is_bracket(char):
                continue
            # push opening bracket into the stack
            if is_opening_bracket(char):
                self.stack.push(char)
            else:
                # if closing bracket forms a pair, remove opening bracket from the top of the stack
                if is_pair(self.stack.peek(), char):
                    self.stack.pop()
                # otherwise is non-symmetrical
                else:
                    return False
        # after handling should not to be extra brackets in the stack
        return self.stack.is_empty()

def is_pair(opening_bracket, closing_bracket) -> bool:
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    return pairs.get(opening_bracket) == closing_bracket


def is_opening_bracket(symbol) -> bool:
    pattern = r'[\[\(\{]'
    return True if re.match(pattern, symbol) else False


def is_bracket(symbol) -> bool:
    pattern = r'[\[\(\{\]\)\}]'
    return True if re.match(pattern, symbol) else False


if __name__ == '__main__':
    check = Check()
    print(check.is_symmetrical('( ){[ 1 ]( 1 + 3 )( ){ }}:')) # symmetrical - True
    print(check.is_symmetrical('( 23 ( 2 - 3);:')) # non-symmetrical - False
    print(check.is_symmetrical('( 11 }:')) # non-symmetrical - False




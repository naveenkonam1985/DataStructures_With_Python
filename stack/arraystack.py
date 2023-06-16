# Implementation of Stack with Lists

class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass


class ArrayStack:
    """Stack Implementation using Lists"""
    
    
    def __init__(self):
        "Create an empty stack"
        self._data = []


    def __len__(self):
        """Returns number of elements in the stack"""
        return len(self._data)
    

    def is_empty(self):
        """Returns True if the stack is empty"""
        return len(self._data) == 0
    

    def push(self, e):
        """Add element e to the stack"""
        self._data.append(e)


    def pop(self):
        """Remove and return the element from the top of the stack
        Raise Empty Exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._data.pop()
    

    def top(self):
        """Return the element from the top of the stack
        Raise Empty Exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._data[-1]
    


if __name__ == '__main__':
    s=ArrayStack()
    
    s.push(5)
    s.push(6)
    s.push(7)
    print(s.top())
    s.push(8)
    print(s.pop())
    


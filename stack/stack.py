# stack.py
# Implementation of Stack in Python
# Author: Naveen Kumar Konam
# Date: 15/03/2023

import sys

class stack:
    '''
    This is simple implementation of stack with list structure
    It gives the following functionality push(i), pop(), peek(), isEmpty(), numElements(),
    printElements() and sizeofStack() for Stack implementation.
    '''

    def __init__(self):
        self.__elements = []
        self.top = -1
        self.count = 0

    def push(self, i):
        self.__elements.append(i)
        self.count += 1
        print(f"Element {i} pushed to stack")

    def pop(self):
        if self.isEmpty():
            print("Stack underflow")
            sys.exit()

        else:
            self.count -= 1
            print("Popped element is: ", self.__elements.pop())

    def peek(self):
        return self.__elements[self.top]

    def printElements(self):
        print("Printing elements")
        for i in self.__elements[::self.top]:
            print(i)

    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False

    @property
    def numElements(self):
        if self.isEmpty():
            return 0
        else:
            return self.count

    @property
    def sizeofStack(self):
        return sys.getsizeof(self.__elements)


if __name__ == '__main__':
    s = stack()
    s.push(1)
    s.push(2)
    s.pop()
    s.printElements()
    print("Number of elements: ", s.numElements)
    print("Size of stack: ", s.sizeofStack)
    s.push(28)
    s.push(99)
    s.push(33)
    s.printElements()
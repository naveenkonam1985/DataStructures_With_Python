# stack.py
# Implementation of Stack in Python
# Author: Naveen Kumar Konam
# Date: 11/03/2023

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

    def push(self, i):
        self.__elements.append(i)
        print(f"Element {i} pushed to stack")

    def pop(self):
        if self.isEmpty():
            print("Stack underflow")
            sys.exit()

        else:
            print("Popped element is: ", self.__elements.pop())

    def peek(self):
        return self.__elements[-1]

    def isEmpty(self):
        if len(self.__elements) == 0:
            return True
        else:
            return False

    def numElements(self):
        if self.isEmpty():
            print("Empty stack")
        else:
            print("The number of elements: ", len(self.__elements))

    def printElements(self):
        print("Printing elements")
        for i in self.__elements[::-1]:
            print(i)

    def sizeofStack(self):
        print(sys.getsizeof(self.__elements))


if __name__ == '__main__':
    s = stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.printElements()
    s.pop()
    s.push(4)
    s.pop()
    s.push(5)
    s.printElements()
    s.numElements()
    s.sizeofStack()
    s.push(28)
    s.push(99)
    s.sizeofStack()
    s.push(33)
    s.printElements()

# Implementation of Queue 
# Naveen Kumar Konam

from typing import List

# class for Node
class Node:
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next


# class for Queue
class Queue:
    def __init__(self):
        pass


    def add(self, elem):
        pass

    
    def pop(self):
        pass


    def peek(self, elem):
        pass

    
    def isEmpty(self):
        pass


    def isFull(self):
        pass


    def clear(self):
        pass
        

    def __contains__(self, elem):
        pass


    def __len__(self):
        pass


    def __str__(self):
        pass

    def __repr__(self):
        pass



class ListQueue(Queue):
    def __init__(self, elements = None):
        if elements:
            if isinstance(elements, List):
                self.__elements = elements
                self.__length = len(elements)
            else:
                raise Exception("Not a List")
        else:
            self.__elements = elements
            self.__length = 0

    def add(self, elem):
        self.__elements.append(elem)
        self.__length += 1
        return self.__elements
    
    def pop(self):
        if self.isEmpty():
            return Exception
        else:
            self.__length -= 1
            return self.__elements.pop(0)
        
    
    def isEmpty(self):
        if len(self.__elements) == 0:
            return True
        else:
            return False
        
    def clear(self):
        self.__elements = list()
        self.__length = 0
        
    def __len__(self):
        return self.__length
        
    def __str__(self):
        return f"Queue with length {self.__length} and elements {self.__elements}"
    
    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}: elements {self.__elements}"


if __name__ == '__main__':
    customers = ListQueue()
    customers.add('a')
    customers.clear()

    print(customers)
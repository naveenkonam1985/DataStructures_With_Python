# Queues implemented with Linked Lists in Python
# Naveen Kumar Konam

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class QueueWithNodes:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0


    def enqueue(self, elem):
        new_node = Node(elem)
        if self.head == None:
            self.head = new_node
            self.tail = self.head

        else:
            new_node.prev=self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    
    def dequeue(self):
        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None

        elif self.count > 1:
            self.count -= 1
            self.head = self.head.next
            self.head.prev = None

        elif self.count < 1:
            print("Queue is Empty")
        
        


if __name__ == '__main__':
    q = QueueWithNodes()
    q.dequeue()

    print("Elements in Queue: ", q.count) 

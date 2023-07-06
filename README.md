# Data Structures With Python

## Data Structures
Data Structures are a way of organizing data for effective and efficient usage. 

This repo is to practice and understand data structures and this repo will be home for data structure implementations such as such as Stacks, Queues, Linked Lists, Trees and their implementations in Python language.

## Types of Data Structures:
* Linear data structures such as Arrays, Stacks, Queues, Linked Lists etc
* Non Linear data structures such as Trees and Graphs

## Arrays
An array is basically, a collection of (index, value) pairs, where the index will be starting from 0 or 1 based on programming language design. Arrays are usually stored in contigous locations in memory. Arrays contain homogenous elements.

In Python, There is no built in data type for Arrays, but **array** module and **numpy** library can be utilized for array computations.

## Linked List
Linked lists are alternative to arrays, where the elements are stored in non-contigous locations in memory. Linked list elements consist of data to be stored and a pointer to the next element or node.

A chain is a linked list where each node contains a pointer to the next node in the list. The last node in the list contains a null (or zero) pointer. A circular list is identical to a chain except that the last node contains a pointer to the first node. A doubly linked circular list differs from the chain and the circular list in that each node contains two pointers. One points to the next node (as before), while the other points to the previous node.

## Stacks and Queues
Stacks inserts and deletes data from one end only. It follows the principle of LIFO (Last In First Out). On the Other hand Queues follow FIFO (First In First Out) principle. Queues inserts data at one end and deletes the data from the other end.

Stacks and Queues can be implemented with arrays or Linked lists. 

## Trees
Trees are nonlinear hierarchical data structure consisting nodes connected by edges.

Trees consist of Nodes in a heirarchical format. Nodes form a parent-child relationship between them. Root Node is the first node from which all other nodes will descend.

Tree Terminology

Node: An item stored in a tree.
Root: The topmost node in a tree. It is the only node     without parent.
Child: A node immediatley below and directly connected to a given node.
Parent: A node immediately above and connected to a give  node.
Siblings: The children nodes of a common parent.
Leaf: A node that has no children.
Interior node: A node that has atleast one child.
Edge/Branch : The line that connects parent t its child.
Descendant: A node's children, and down the line.
Ancestor: A node's parent and up to the root.
Path: The sequence of edges that connect a node and its descendants.
Depth: The depth of a node equals the length of the path connectinf it to the root.
Height: The length of the longest path in the tree.
Subtree: The tree fromed by a node and descendants.

A binary tree is a collection of nodes, where the nodes in the tree can have zero, one, or two child nodes.


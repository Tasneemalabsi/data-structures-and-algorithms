# Trees

Trees are non-linear data structures, a tree whose elements have at most 2 children is called a binary tree.

## Challenge
Create a Node class that has properties for the value stored in the node, the left child node, and the right child node. And create a Binary Tree class

## Approach & Efficiency
- create a class for the Node
- Create a class for the binary tree which has these methods:
    - bfs method(breadth first): returns the items of the tree as a list in the breadth first order

                    big O of n for time // O(n) -> linear

                    big O of n for space // O(n) -> linear

    - pre order method: returns the items of the tree as a list in the pre-order

                        big O of n for time // O(nlogn) -> logarithmic

                        big O of n for space // O(n) -> linear

    - in-order method: returns the items of the tree as a list in the in-order

                        big O of n for time // O(nlogn) -> logarithmic

                        big O of n for space // O(n) -> linear
    - post order method: returns the items of the tree as a list in the post-order

                        big O of n for time // O(nlogn) -> logarithmic

                        big O of n for space // O(n) -> linear

- Create a class for the binary search tree which has these methods:
    - add method: adds nodes to the tree, either to the root if the tree was empty at first, or to the left if the added node's value was smaller than the root node's value, or to the right if the node's value was larger than the root node's value .

                    big O of n for time // O(n) -> linear

                    big O of n for space // O(1) -> constant

    - contains method: returns true if the given value exists in the tree, otherwise returns false

                        big O of n for time // O(n) -> linear

                        big O of n for space // O(1) -> constant

## API
- bfs() method: returns the items of the tree as a list in the breadth first order
- pre_order() method: returns the items of the tree as a list in the pre-order
- in_order() method :returns the items of the tree as a list in the in-order
- post_order() method : returns the items of the tree as a list in the post-order
- add() method: adds nodes to the tree, either to the root if the tree was empty at first, or to the left if the added node's value was smaller than the root node's value, or to the right if the node's value was larger than the root node's value .
- contains() method: returns true if the given value exists in the tree, otherwise returns false

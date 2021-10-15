# Singly Linked List
singly linked list describes a linked list that only moves in one direction

## Challenge
create a singly linked list with inserting a new node into it, check existing values, and a string that represents all the values in the linked list .

## Approach & Efficiency
- create a class for the linked list
- create a constructor function to implement data in the first node, create functions to add new nodes, check whether values exist or not and print all of the values as a string .
- for insert method:

                    big O of n for time // O(1) -> constant

                    big O of n for space // O(1) -> constant

- for includes method:

                       big O of n for time // O(1) -> linear

                       big O of n for space // O(1) -> constant

-  for includes method:

                        big O of n for time // O(n) -> linear

                        big O of n for space // O(n) -> linear

## API
- insert() method: adds a new node .
- includes() method: returns a boolean that indicates if a node has a certain value or not
- to_string method : show all the values that were inserted in the linked list as a string

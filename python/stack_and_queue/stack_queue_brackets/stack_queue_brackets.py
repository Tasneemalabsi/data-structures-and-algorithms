from stack_and_queue.stack import Stack


def validate_brackets(str):
    """
    this function checks whether a given string is balanced or not, if every opening bracket has a relatively closing one, then the string is balanced and returns true, otherwise returns false

    arguments:
    value : string

    returns: boolean
    """
    parantheses = ["[","{","("]
    closing_parantheses = ["]","}",")"]
    stack = Stack()
    if not str:
        raise Exception ('the input string is empty')
    else:
        for char in str:
            if char in parantheses:
                stack.push(char)
            if char in closing_parantheses:
                if stack.top and(parantheses[closing_parantheses.index(char)] == stack.top.value):
                    stack.pop()
                else:
                    return False
        return stack.is_empty()



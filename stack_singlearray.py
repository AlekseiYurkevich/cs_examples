# Implement n stacks using a single array
# Are the stacks and array a fixed size?
# Yes
# Are the stacks equally sized?
# Yes
# Does pushing to a full stack result in an exception?
# Yes
# Does popping from an empty stack result in an exception?
# Yes
# Can we assume the user passed in stack index is valid?
# Yes
# Can we assume this fits memory?
# Yes

# return stack size * stack index + stack pointer
# Complexity:

# Time: O(1)
# Space: O(1)


class Stack:
    def __init__(self, num_stack, stack_size):
        self.num_stack = num_stack
        self.stack_size = stack_size
        self.stack_pointers = [-1] * self.num_stack
        self.stack_array = [None] * self.num_stack * self.stack_size

    def abs_index(self, stack_index):
        return stack_index * self.stack_size + self.stack_pointers[stack_index]


"""
Data Structures: Stack, Queue, and Two-Way Queue
- Stack principle of "last in, first out" (LIFO: Last In, First Out)
- A queue in programming is an abstract data structure that operates on the principle of "first in, first out" (FIFO: First In, First Out)
Queue operations:
Enqueue - add an element to the end of the queue.
Dequeue - remove an element from the beginning of the queue.
Front/Peek - view the first element of the queue without removing it.
Is Empty - check if the queue is empty.
Size - determine the number of elements in the queue.
Queue can be done with the help of list but its not optimized way becasue when you add element to the list the cost is too expensive

A more efficient option is to use deque from the collections module as a queue.
"""

##############------STACK------######################


# Create a stack
def create_stack():
    return []


# Check for emptiness
def is_empty(stack):
    return len(stack) == 0


# Add an item
def push(stack, item):
    stack.append(item)


# Remove an item
def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        print("Stack is empty")


# View the top item
def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        print("Stack is empty")


stack = create_stack()
push(stack, "a")
push(stack, "b")
push(stack, "c")


print(peek(stack))  # Print 'c'
print(pop(stack))  # Print 'c'
print(peek(stack))  # Print 'b'

##############------QUEUE----######################

from collections import deque

# Create a queue
queue = deque()

# Enqueue: Add elements
queue.append("a")
queue.append("b")
queue.append("c")

print("Queue after adding elements:", list(queue))

# Dequeue: Remove element
print("Element removed:", queue.popleft())

print("Queue after removing element:", list(queue))

# Peek: View the first element
print("First element in queue:", queue[0])

# IsEmpty: Check for emptiness
print("Is the queue empty:", len(queue) == 0)

# Size: Size of the queue
print("Queue size:", len(queue))


# also you can limit the queue size
from collections import deque

d = deque(maxlen=5)
for i in range(10):
    d.append(i)

print(d)


"""
Two-way queues combine the capabilities of stacks and queues, allowing elements to be added and removed from both ends. Its more effective on comparison with regular lists
"""


from collections import deque


# List of tasks where each task is a dictionary
tasks = [
    {"type": "fast", "name": "Wash the dishes"},
    {"type": "slow", "name": "Watch a TV series"},
    {"type": "fast", "name": "Walk the dog"},
    {"type": "slow", "name": "Read a book"},
]

# Initialize the task queue
task_queue = deque()

# Allocation of tasks into a queue according to their priority
for task in tasks:
    if task["type"] == "fast":
        task_queue.appendleft(task)
        # Adding to high priority
        print(f"Quick task added: {task['name']}")
    else:
        task_queue.append(task)  # Adding to low priority
        print(f"Added slow task: {task['name']}")

# Task execution
while task_queue:
    task = task_queue.popleft()
    print(f"Task running: {task['name']}")

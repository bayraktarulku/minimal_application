# class stack operations (pop && push)
# Last-in-First-Out (LIFO)
class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

    def print(self):
        return self.stack


# class queue operations (enqueue && dequeue)
# First-in-First-Out (FIFO) principle.
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def print(self):
        return self.queue


# Let's review 2 examples for stacks and queues

# Stack
# In a stack, the last item we enter is the first to come out.
favourite_films = Stack()

# enters the elements of the list
favourite_films.push("Forrest Gump (1994)")
favourite_films.push("Inception (2010) ")
favourite_films.push("The Shawshank Redemption (1994)")
favourite_films.push("The Silence of the Lambs (1991)")
favourite_films.push("The Prestige (2006)")

# print the elements of the list
print(favourite_films.print())
print(favourite_films.size())

favourite_films.pop()
print(favourite_films.print())

# Queue
# In a queue, the first item we enter is the first come out.

favourite_films = Queue()

# enters the elements of the list
favourite_films.enqueue("Forrest Gump (1994)")
favourite_films.enqueue("Inception (2010) ")
favourite_films.enqueue("The Shawshank Redemption (1994)")
favourite_films.enqueue("The Silence of the Lambs (1991)")
favourite_films.enqueue("The Prestige (2006)")

# print the elements of the list
print(favourite_films.print())
print(favourite_films.size())

favourite_films.dequeue()
print(favourite_films.print())

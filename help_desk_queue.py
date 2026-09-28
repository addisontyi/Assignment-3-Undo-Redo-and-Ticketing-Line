# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None

        value = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return value

    def peek(self):
        if self.front is None:
            return None

        return self.front.value

    def print_queue(self):
        current = self.front

        while current is not None:
            print(current.value)
            current = current.next

def run_help_desk():
    # Create an instance of the Queue class
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            queue.enqueue(name)
            
            print(f"{name} added to the queue.")
        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            customer = queue.dequeue()

            if customer is not None:
                print(f"{customer} has been helped.")
            else:
                print("No customers in the queue.")

        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            customer = queue.peek()

            if customer is not None:
                print(f"Next customer: {customer}")
            else:
                print("No customers in the queue.")

        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            queue.print_queue()

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()

#Design Memo

#A stack is a good choice for a undo/redo system because
#It follows the Last In First Out principle. When the user 
#performs an action, often time the last action they did is
#the one they want to undo. For example, if a user does something
#in order like 1 2 3, then they go to undo it, it will undo 3 then 2 then 1.
#Therefore, using a stack makes this system very efficient because
#the most recent action will always be at the top. The redo stack also works
#the same because it stores the actions that were undone.
#A queue is a good choice for a help desk system because it follows the 
#First In First Out principle. The idea is that customers should be helped
#in the order they arrive. Therefore, the first customer added to the queue
#will be the first one removed. This creaates a fair and organized system
#that handles help desk requests. My implementations are different from
#the Python built in lists because I made the data structures from scratch
#using Node objects and pointers instead of relying on the built in list methods.
#The stack uses a top pointer that keeps track of the most recent node
#The queue uses a front and rear pointer to keep track of the first and last nodes.
#This helps show how stacks and queues work on the inside, instead of using
#the built in list methods that hide the implementation details.
#Using linked nodes also allows each of the structures to be able to connect 
#other elements through their next pointers.

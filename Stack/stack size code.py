class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LimitedStack:
    def __init__(self, limit):
        self.top = None
        self.size = 0
        self.limit = limit

    def display(self):
        if self.top == None:
            print("The stack is empty!!!")
        else:
            temp = self.top
            while temp !=None:
                print(temp.data, end=" ")
                temp = temp.next

    def push(self, data):
        if self.size >= self.limit:
            print("Stack is full")
            return
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return
        return self.top.data

    def is_empty(self):
        return self.top is None

    def get_size(self):
        return self.size


mystack = LimitedStack(5)
mystack.push(10)
mystack.push(20)
mystack.push(30)
mystack.push(40)
mystack.push(50)
mystack.display()
print()
mystack.push(60)


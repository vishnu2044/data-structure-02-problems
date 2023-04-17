class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class StackValues:
    def __init__(self):
        self.top = None

    def display(self):
        if self.top == None:
            print("The stack is empty!!!")
        else:
            temp = self.top
            while temp !=None:
                print(temp.value, end=" ")
                temp = temp.next

    def push(self, data):
        newval = Node(data)
        newval.next = self.top
        self.top = newval

    def pop(self):
        self.top = self.top.next

    def is_empty(self):
        if self.top == None:
            print("The stack is empty!!")
        else:
            print("the stack has values!!")

    def count(self):
        temp = self.top
        count = 0
        while temp != None:
            count +=1
            temp = temp.next
        print("The count of the stack : ", count)

    def peek(self):
        print(self.top.value)

mystack = StackValues()
mystack.push(10)
mystack.push(20)
mystack.push(30)
mystack.push(40)
mystack.pop()
mystack.count()
mystack.peek()
mystack.display()
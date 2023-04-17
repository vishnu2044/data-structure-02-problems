

stack=[]
def push():
   if len(stack)==n:
       print("The stack is full !")
   else:
       ele = int(input('Enter the element for the stack :'))
       stack.append(ele)
       print(stack)
def pop():
   if not stack:
       print("The stack is empty !")
   else:
       rem=stack.pop()
       print(f'The removed element is :{rem}')
       print(stack)
n=int(input('Enter the limit for the stack :'))
while True:
   cho=int(input('Choose the operation you want to do : 1 for push element into the stack , 2 for pop an element in stack , 3 for quit\n '))
   if cho==1:
       push()
   elif cho==2:
       pop()
   elif cho==3:
       break
   else:
       print("choose the correct value ")


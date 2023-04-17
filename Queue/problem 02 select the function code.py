queue=[]
def enqueue():
   if len(queue)==n:
       print("The queue is full ")
   else:
       ele=int(input("Enter the element you want to add in queue :"))
       queue.append(ele)
       print(queue)
def dequeue():
   if not queue:
       print('The queue is empty ')
   else:
       queue.pop(0)
       print(queue)
n=int(input("Enter the limit of the queue"))
while True:
   cho=int(input("choose which operation you want to do : 1. Enqueue , 2. dequeue , 3. exit\n"))
   if cho==1:
       enqueue()
   elif cho==2:
       dequeue()
   elif cho==3:
       break
   else:
       print("invalid entry ")

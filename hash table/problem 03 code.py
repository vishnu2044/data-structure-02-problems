class HashTable:
   def __init__(self, size):
       self.size = size
       self.table = [None] * self.size

   def hash(self, key):
       return key % self.size

   def insert(self, key, value):
       index = self.hash(key)
       i = 1
       while self.table[index] is not None:
           index = (index + i * i) % self.size
           i += 1
       self.table[index] = (key, value)

   def search(self, key):
       index = self.hash(key)
       i = 1
       while self.table[index] is not None:
           if self.table[index][0] == key:
               return self.table[index][1]
           index = (index + i * i) % self.size
           i += 1
       return None

   def delete(self, key):
       index = self.hash(key)
       i = 1
       while self.table[index] is not None:
           if self.table[index][0] == key:
               self.table[index] = None
               return
           index = (index + i * i) % self.size
           i += 1
obj=HashTable(10)
obj.insert(5,23)
obj.insert(4,25)
obj.insert(2,3)
obj.insert(1,2)
obj.insert(7,223)
print(obj.search(5))
print(obj.search(2))
print(obj.search(1))
print(obj.search(4))
print(obj.search(7))
obj.delete(7)
print(obj.search(7))

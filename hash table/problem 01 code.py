class HashTable:
   def __init__(self, size):
       self.size = size
       self.table = [[] for _ in range(size)]

   def hash_function(self, key):
       return hash(key) % self.size

   def insert(self, key, value):
       index = self.hash_function(key)
       for entity in self.table[index]:
           if entity[0] == key:
               entity[1] = value
               return
       self.table[index].append([key, value])

   def get(self, key):
       index = self.hash_function(key)
       for entity in self.table[index]:
           if entity[0] == key:
               return entity[1]
       raise KeyError(key)

   def remove(self, key):
       index = self.hash_function(key)
       for i, entity in enumerate(self.table[index]):
           if entity[0] == key:
               del self.table[index][i]
               return
       raise KeyError(key)

   def print(self):
       print(self.table)


obj = HashTable(10)
obj.insert(5, 13)
obj.insert(4, 123)
obj.insert(1, 136)
obj.insert(2, 3)
obj.insert(7, 1)
obj.insert(3, 133)
print(obj.get(5))
print(obj.get(1))
print(obj.get(2))
print(obj.get(7))
obj.print()

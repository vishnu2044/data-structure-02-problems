class Hashtable:
   def __init__(self, size):
       self.size = size
       self.keys = [None] * size
       self.values = [None] * size

   def hash_function(self, key):
       return hash(key) % self.size

   def insert(self, key, value):
       index = self.hash_function(key)
       while self.keys[index] is not None:
           if self.keys[index] == key:
               self.values[index] = value
               return
           index = (index + 1) % self.size
       self.keys[index] = key
       self.values[index] = value

   def get(self, key):
       index = self.hash_function(key)
       while self.keys[index] is not None:
           if self.keys[index] == key:
               return self.values[index]
           index = (index + 1) % self.size
       return None

   def remove(self, key):
       index = self.hash_function(key)
       while self.keys[index] is not None:
           if self.keys[index] == key:
               self.keys[index] = None
               self.values[index] = None
               return
           index = (index + 1) % self.size
       raise KeyError(key)


ht = Hashtable(10)
ht.insert("apple", 3)
ht.insert("banana", 2)
ht.insert("cherry", 5)
ht.insert("grapes", 10)
ht.insert("mango", 15)
print(ht.get("apple"))
ht.remove("banana")
print(ht.get("cherry"))
print(ht.get("grapes"))
print(ht.get("banana"))
print(ht.size)
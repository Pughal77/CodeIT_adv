

'''
Problem #1: Implement a Hash Table
    - You are to implement the following methods:
        -> constructor
        -> insert
        -> search

    - Each method comes with instructions on how to implement them. 
    - The hash function has been implemented for you. You should make use of this to implement your insert and search methods
    - The class HashItem has been implemented for you. Each key value pair should be stored as a HashItem in the hash table
    - To test your hash table, run `python hash_test.py`
'''

class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
    def __str__(self):
        return "({}, {})".format(self.key, self.value)

def hash(key):
    if not isinstance(key, str) or not key[0].isalpha():
        print('key should be a string & first char should be an alphabet')
        return None
    
    firstLetter = key[0].lower()
    index = ord(firstLetter) - 97
    return index
    
class HashTable():
    
    def __init__(self):
        """Initialise hash table

        Attributes
        ----------
        table: type `array`, length 26

        Arguments: None
        Return: None
        """
        self.table = [None] * 26
      
    
    def insert(self, key, value):
      """Insert into hash table
  
          Arguments
          ----------
          key: type `string`, first character should be an alphabet
          value: type `any`
  
          Returns True if item has been successfully added to the hash table and False if not
          """
          # Ben: Can try this
          # index = hash(key)
          # if index is not None:
          #   self.table[index] = HashItem(key,value)
      if hash(key) != None and hash(key)<=25:
        self.table[hash(key)] = HashItem(key,value) # idx = hash(key), then check if idx is not None, then do this line
        return True
      else:
        return False
      
      
      
          
        
      

        # PSEUDO CODE

        # 1. Convert key to hash index

        # 2. If hash index is valid, index into table attribute and insert key-value pair as HashItem
        

    def search(self, key):
        """Search hash table

        Arguments
        ----------
        key: type `string`

        Returns HashItem associated with key in the hash table if there is one, else None
        """

        # PSEUDO CODE

        # 1. Convert key to hash index

        # 2. Return HashItem at index in hash table if exists and key matches, else None

        # Ben: Can try something like that :)
        # idx = hash(key)
        # if idx is not None and self.table[idx].key == key:
        #    return self.table[idx]
        # else:
        #    return None
        term = hash(key)
        if term is not None and self.table[term].key == key:
          return self.table[term]
        else:
          return None

'''
Problem #2: Implement a Hash Table with Linear Probing
    - You are to implement the following methods:
        -> constructor
        -> insert
        -> search
        -> delete

    - Each method comes with instructions on how to implement them. 
    - The hash function has been implemented for you. You should make use of this to implement your insert and search methods
    - The class HashItem has been implemented for you. Each key value pair should be stored as a HashItem in the hash table
'''


class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({}, {})".format(self.key, self.value)


def hash(key, cap):
    if not isinstance(key, str) or not key[0].isalpha():
        print('key should be a string & first char should be an alphabet')
        return None

    firstLetter = key[0].lower()
    index = ord(firstLetter) - 97
    return index % cap


class LPHashTable:
    
    def __init__(self, capacity):
        """Initialise hash table

        Attributes
        ----------
        table: type `array`, length = capacity
        size: type `int` -> number of existing HashItems in table

        Arguments
        ----------
        capacity: type `int`, starting capacity of the hash table

        Return: None
        """
        self.table = [None] * capacity
        
        self.size = 0
    
    def insert(self, key, value):
        """Insert into hash table

        Arguments
        ----------
        key: type `string`, first character should be an alphabet
        value: type `any`

        Returns True if item has been successfully added to the hash table and False if not
        """

        # PSEUDO CODE

        # 1. If size is equals to capacity, resize hash table to twice it's size

        # 2. Convert key to hash index

        # 3. Increment index while position in hash table is not empty

        # 4. If empty slot is found / wildcard value encountered, insert key-value pair as HashItem

        # 5. Increment size and return True
        if self.size == len(self.table):
          capacity = len(self.table) * 2
          new_table = [None] * capacity
          for i in range(len(self.table)):
            idx = hash(self.table[i].key, len(new_table))
            for a in range(len(new_table)):
              if idx > len(new_table)-1:
                  idx = 0
              if new_table[idx] == None or new_table[idx] == "%":
                new_table[idx] = self.table[i]
                break
                return self.table[i]
              else:
                idx += 1
          self.table = new_table
      
        idx = hash(key,len(self.table))
        if idx != None:
          for i in range(len(self.table)):
            if idx > len(self.table)-1:
              idx = 0
            if self.table[idx] == None or self.table[idx] == "%":
              self.table[idx] = HashItem(key,value)
              self.size += 1
              return HashItem(key,value)
              break
            else:
              idx += 1
          
        else:
          return print("key not inserted to table")

    def search(self, key):
        """Search hash table

        Arguments
        ----------
        key: type `string`

        Returns HashItem associated with key in the hash table if there is one, else None
        """

        # PSEUDO CODE

        # 1. Convert key to hash index

        # 2. Iterate through hash table from starting index until keys are matched

        # 3. If blank space or entire hash table has been traversed, return None

        # 4. If matching key is encountered, return the HashItem
        foo = hash(key,len(self.table))
        if self.table[foo] == None:
          return None
        if key != self.table[foo].key or self.table[foo].key == "%":
          for i in range(len(self.table)):
            if self.table[foo] == None:
              return None
            if key == self.table[foo].key:
              return self.table[foo]
              break
            if foo > len(self.table)-1:
              foo = 0
            foo+=1
          return print("key doesnt exist")
        if key == self.table[foo].key:
          return self.table[foo]
        
    def delete(self, key):
        """Delete key from hash table

        Arguments
        ----------
        key: type `string`

        Returns True if key has been deleted and False if not
        """

        # PSEUDO CODE

        # 1. Convert key to hash index

        # 2. Search for key in hash table starting from index

        # 3. If key does not exist, return False

        # 4. If matching key is encountered, replace with a wild card `HashItem("%", None)` to indicate null key

        # 5. Decrement size and return True
        #searching if key exists
        foo = hash(key,len(self.table))
        if self.table[foo] == None:
          return None
        if key == self.table[foo].key:
          pass
        if key != self.table[foo].key or self.table[foo].key == "%":
          for i in range(len(self.table)):
            foo += 1
            if foo > len(self.table)-1:
              foo = 0
            if self.table[foo] == None:
              return None
            if key == self.table[foo].key:
              break
            if i == range(len(self.table)):
              return print("key does not exist")
        #del the key
        self.table[foo] = HashItem("%",None)
        self.size -= 1
        #rehashing if size is half of table
        if self.size == len(self.table) // 2:
          capacity = len(self.table) // 2
          new_table = [None] * capacity
          final_table = [None] * capacity
          #removing elements that are None or hve wild char from the list and put remaining elements into new_list
          y=0
          for x in range(len(self.table)):
            if self.table[x] == None:
              continue
            if self.table[x].key == "%":
              pass
            else:
              new_table[y] = self.table[x]
              y += 1
          #hashing the elements in thhat list to give output of final list
          for i in range(len(final_table)):
            idx = hash(new_table[i].key,len(final_table))
            for x in range(len(final_table)):
              if idx > len(final_table)-1:
                idx = 0
              if final_table[idx] == None:
                final_table[idx] = new_table[i]
                break
              idx += 1
          self.table = final_table
          return True
        #del_item = self.search(key)
        #del_item = HashItem("%",None)

'''
    Implement a minimum binary heap with changing keys
    - You are to implement the following methods:
        -> constructor
        -> sink, swim
        -> insert, getMin

    - Each method comes with instructions on how to implement them. 
    - You are given helper functions from the util folder:
        -> parent: get parent index
        -> left, right: get left & right child index respectively
        -> HeapItem: contains key & value attributes. HeapItems in MinHeap are sorted accoridng to value
    - The higherPriority method has been implemented to help compare two HeapItems in the MinHeap
    - You may reference from min_heap1.py and make the appropriate adjustments
    - To test your implementation, run `python utils/mh2_test.py`
'''

from utils.helpers import parent, left, right, HeapItem

class MinHeap:
    def higherPriority(self, index1, index2):
        """Compare two indices in heap

        Returns
        ----------
        - None if index1 or index2 are invalid
        - True if value of item at index1 is higher priority (lower in the case of MinHeap) 
        compared to value of item at index 2 & False if not
        """
        if self.heap[index1] is None or self.heap[index2] is None:
            return 

        if self.heap[index1].value < self.heap[index2].value:
            return True
        else:
            return False
    def swap_index(self,index1,index2):
      key_1 = self.heap[index1].key
      key_2 = self.heap[index2].key
      self.positions[key_1],self.positions[key_2] = index2,index1
      
      self.heap[index1],self.heap[index2] = self.heap[index2],self.heap[index1]
      

    def __init__(self, maxsize):
        """Initialise heap

        Attributes
        ----------
        heap: type `array`, length = maxsize + 1, begins empty
            -> binary heap representation
        size: type `int` 
            -> number of existing items in heap, begins at 0
        maxsize: type `int` 
            -> max number of items in heap, begins with argument
        positions: type `dict`
            -> stores the positions (indices) of keys in the heap, begins empty

        Arguments
        ----------
        maxsize: type `int`

        Return: None
        """
        self.maxsize = maxsize
        self.size = 0
        a = maxsize + 1
        self.heap = [None] * a
        self.positions = {}
        pass

    def swim(self, index):
        """Move a HeapItem up the heap

        Arguments
        ----------
        index: type `int` -> starting index of HeapItem to swim

        Returns None
        """

        # PSEUDO CODE

        # while:
        #   - item is not at the top of the heap AND
        #   - item's key has higher priority than parent's key
        # swap with parent (ensure to update positions attribute accordingly)
        while index != 1 and self.higherPriority(index, parent(index)):
          self.swap_index(index, parent(index))

    def sink(self, index):
        """Move a HeapItem down the heap

        Arguments
        ----------
        index: type `int` -> starting index of HeapItem to sink

        Returns None
        """

        # PSEUDO CODE

        # while item is not a child node:
        #   if item's key has lower priority than children's key:
        #       swap with children with highest priority
        #       (ensure to update positions attribute accordingly)
        while left(index) <= self.maxsize and index <= self.maxsize and self.higherPriority(left(index),index):
          if right(index) < self.maxsize and self.higherPriority(right(index),left(index)):
            self.swap_index(index, right(index))
          else:
            self.swap_index(index, left(index))

    def insert(self, newKey, newValue):
        """Insert a new key-value pair into heap, 
        or change key if already exists

        Arguments
        ----------
        newKey: type `string` -> new key to insert
        newValue: type `int` -> new value to insert

        Returns None

        Note: Items in Heap are sorted according to their VALUE 
        """
        
        # PSEUDO CODE

        # 1. Check if key already exists in heap
        # 2. If yes, assign the key it's new value, and swim / sink the item to it's appropriate position
        # 3. If no, insert new HeapItem
        new_item = HeapItem(newKey,newValue)
        if self.positions.get(newKey) ==None:
          if self.size == self.maxsize:
            return False
          else:
            self.positions[newKey] = self.size + 1
            self.heap[self.size+1] = new_item
            self.swim(self.size+1)
            
            print(self.positions)
            self.size += 1
        
        if self.positions.get(newKey) !=None:
          index = self.positions[newKey]
          self.heap[index] = new_item
          self.sink(index)
          self.swim(index)
          

    def removeMin(self):
        """Extracts HeapItem with highest priority value 
        (i.e. lowest value in Min Heap)

        Arguments: None

        Returns HeapItem with highest priority in min heap, or None if heap is empty
        """
        
        # PSEUDO CODE

        # 1. Save item with highest priority (first item in heap)
        # 2. Swap first and last item in heap
        # 3. Delete last item (decrement size attribute)
        # 4. Sink the first item to appropriate position
        highest_priority = self.heap[1]
        
        if highest_priority == None:
          return None
        else:
          self.heap[1],self.heap[self.size] = self.heap[self.size] ,self.heap[1]
          self.heap[self.size] = None
          #after removing highest priority
          self.size-=1
          self.sink(1)
          return highest_priority

        pass
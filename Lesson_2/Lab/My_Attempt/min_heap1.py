'''
    Implement a minimum binary heap
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
    - To test your implementation, run `python utils/mh1_test.py`
'''

from utils.helpers import parent, left, right, HeapItem

class MinHeap1:
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

    def __init__(self, maxsize):
        """Initialise heap

        Attributes
        ----------
        heap: type `array`, length = maxsize + 1 
            -> binary heap representation
        size: type `int` 
            -> number of existing items in heap
        maxsize: type `int` 
            -> max number of items in heap

        Arguments
        ----------
        maxsize: type `int`

        Return: None

        Note: Items should be inserted starting from index 1 for ease of use
        """
        self.maxsize = maxsize
        array_size = maxsize + 1
        self.heap = [None] * array_size
        self.size = 0
        

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
        # swap with parent
        while index != 1 and self.higherPriority(index, parent(index)):
         self.heap[parent(index)],self.heap[index] = self.heap[index],self.heap[parent(index)]
         index = parent(index)
            

    def sink(self, index):
        """Move a HeapItem down the heap

        Arguments
        ----------
        index: type `int` -> starting index of HeapItem to sink

        Returns None
        """
      
        while left(index) <= self.maxsize and index <= self.maxsize and self.higherPriority(left(index),index):
          if right(index) < self.maxsize and self.higherPriority(right(index),left(index)):
            self.heap[right(index)],self.heap[index] = self.heap[index],self.heap[right(index)]
            index = right(index)
          else:
            self.heap[left(index)],self.heap[index] = self.heap[index],self.heap[left(index)]
            index = left(index)
        
        
        

        # PSEUDO CODE

        # while item is not a child node:
        #   if item's key has lower priority than children's key:
        #       swap with children with highest priority
        #       (ensure to update positions attribute accordingly)
      
        pass

    def insert(self, newKey, newValue):
        """Insert a new key-value pair into heap

        Arguments
        ----------
        newKey: type `string` -> new key to insert
        newValue: type `int` -> new value to insert

        Returns None

        Note: Items in Heap are sorted according to their VALUE 
        """
        
        # PSEUDO CODE

        # 1. Check if heap is already at max size
        # 2. Insert new HeapItem at next unfilled index of heap
        # 3. Swim the inserted HeapItem 
        # 4. Increment size attribute
        new_item = HeapItem(newKey,newValue)
        if self.size == self.maxsize:
          return False
        self.heap[self.size+1] = new_item
        self.swim(self.size+1)
        self.size += 1

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
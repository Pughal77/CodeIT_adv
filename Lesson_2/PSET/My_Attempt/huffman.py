from heap import MinHeap


class TreeNode:
    def __init__(self, char, frequency, left=None, right=None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right


'''
    calculateFrequencies:
        - This function takes in the data string and returns a dictionary which 
        contains each character in the string as keys and it's frequency as the value
'''


def calculateFrequencies(data):
    # TO IMPLEMENT
    freq_dict = {}
    for x in data:
        if freq_dict.get(x) == None:
            freq_dict[x] = 1
        else:
            freq_dict[x] += 1
    return freq_dict
    pass


'''
    createHuffmanTree:
        - This function takes in char frequencies and inserts each character as a TreeNode 
        into a MinPQ sorted according to character frequency
        - Then, while the PQ has more than one item:
            -> Extract the 2 min nodes and create a new tree node where its 
            left is the node with smallest frequency and right is the node with second smallest frequency
            -> Insert the new node back into the priority queue
        - Once the tree has been build, this function should return the root node of the tree as a TreeNode
'''


def createHuffmanTree(charFrequencies):
    # implement priority queue

    Pq = MinHeap(len(charFrequencies.keys()))

    for x in charFrequencies.keys():
        node = TreeNode(x, charFrequencies[x])
        Pq.insert(node, charFrequencies[x])

    # have a nested array with all the tree nodes
    while Pq.size > 1:
        no_1 = Pq.getMin()
        no_2 = Pq.getMin()
        parent = TreeNode(f"{no_1.key.char}{no_2.key.char}",
                          no_1.value + no_2.value, no_1.key, no_2.key)
        Pq.insert(parent, parent.frequency)
    root_node = Pq.heap[1].key
    return root_node

    pass


'''
    calculateCodes:
        - This function takes in the root node from the Huffman tree
        - It should traverse the tree, and determine the code for each character in the string:
            -> A left path is considered '0'
            -> A right path is considered '1'
            -> Traverse a tree until you find a leaf node, and that character's code will be its path. 
            -> For instance, to get to C, we first go right, then left. Thus, C's code will be '10'
        - This function should should return a dictionary with each character as keys and it's code as the value
'''


def traverse(huffmanRoot, codes, code):

    if huffmanRoot.right == None and huffmanRoot.left == None:
        codes[huffmanRoot.char] = code
    if huffmanRoot.left != None:
        traverse(huffmanRoot.left, codes, code + "0")
    if huffmanRoot.right != None:
        traverse(huffmanRoot.right, codes, code + "1")


def calculateCodes(huffmanRoot):

    codes = {}
    code = ""
    traverse(huffmanRoot, codes, code)

    return codes


'''
    encodeString(data, codes):
        - This function takes in the original string (data) and the dictionary of codes for each char
        - It should return the string with each character replaced with its corresponding code
        - E.g. If we have:
            -> codes = {'A': '0', 'C': '10', 'B': '11'}
            -> message = "AAABBC"
            Our encoded string will be: "000111110"
'''


def encodeString(data, codes):
    # TO IMPLEMENT
    encoded_data = ""
    for char in data:
        code = codes[char]
        encoded_data += code
    return encoded_data


def HuffmanEncoding(data):

    # 1. Determine frequencies of characters
    charFrequencies = calculateFrequencies(data)

    # 2. Build Huffman tree
    huffmanRoot = createHuffmanTree(charFrequencies)

    # 3. Traverse Huffman tree to determine code for each char
    codes = calculateCodes(huffmanRoot)
    print("codes:", codes)

    # 4. Build encoded string using codes
    encodedOutput = encodeString(data, codes)

    return encodedOutput, huffmanRoot


def main():

    data = input('input a string to encode via huffman: ')
    encoded_output, _ = HuffmanEncoding(data)

    print('encoded data:', encoded_output)
    print('space usage before compression:', len(data) * 8)
    print('space usage after compression:', len(encoded_output))


if __name__ == '__main__':
    main()

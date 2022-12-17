'''
NOTE 1: The number of unique characters is given in a constant variable. Do make use of this to initialise your 2D list!
'''
NO_OF_CHARS = 256

'''
NOTE 2: To convert a character to it's ASCII number, you can use the ord() function in python, and to convert from it, you can use the chr() function
'''
# ord('A') # convert char to ascii number: 65
# chr(65)  # convert ascii number to char: 'A'

'''
    - This function takes in a substring and builds the appropriate finite automata for the KMP string matching algorithm
    - It should return the DFA as a 2D list, with 256 rows (number of ASCII characters) and M (length of substring) + 1 columns, which is the number of states
    - All values in rows of chars not in the substring should be 0
'''
def buildDFA(substring):
    # TO IMPLEMENT
    chars_list = {}
    for char in substring:
      chars_list.setdefault(char,char)
    DFA = []
    for i in range(NO_OF_CHARS):
      n = []
      for x in range(len(substring)+ 1):
        n.append(0)
      DFA.append(n)
    if substring == "":
      return DFA
    # moving right in the graph
    for x in range(len(substring)):
      DFA[ord(substring[x])][x] = x+1
    #moving left in graph
    #iterate thru states in dfa(start from 1 cos no need do anything to state 0)
    for x in range(1,(len(substring)+1)):
      if x == len(substring):
        common_part = substring[1:]
      else:
        common_part = substring[1:x]
      copy_which_state = 0  
      for char in common_part:
        copy_which_state = DFA[ord(char)][copy_which_state]
      for char in chars_list:
        if x != len(substring):
          if char == substring[x]:
            continue
        DFA[ord(char)][x] = DFA[ord(char)][copy_which_state]
    return DFA
      


def KnuthMorrisPratt(text, substring):
    dfa = buildDFA(substring)
    i = 0
    j = 0
    M = len(substring)

    while (i < len(text)):
        charIndex = ord(text[i])
        j = dfa[charIndex][j]
        i += 1
      
        if j == M:
            print("substring found at index {}".format(i - M))
            
        

def main():
    substring = input('substring: ')
    text = input('text: ')
    KnuthMorrisPratt(text, substring)

if __name__ == '__main__':
    main()
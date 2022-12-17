'''
    Problem #1: Implement Knuth-Morris Pratt's Substring Match Algorithm (using LPS) 
    - You are to implement both functions below
    - To test your implementation, run `python utils/kmp_test.py`
'''

def buildLPS(substring: str):
    """Build longest prefix suffix table for KMP algorithm

    Arguments
    ----------
    substring: type `str`

    Return: 
    - lps: length M array, where M is the length of substring,
    representing longest prefix suffix table of substring
    """
    lps = [0] * len(substring)
    lps[0] = 0
    j=0
    i=1

    while i < len(substring):
      if substring[i] == substring[j]:
        j += 1
        lps[i] = j
        i += 1
      else:
        if j == 0:
          lps[i] = j
          i += 1
        else:  
          j = lps[j - 1]
    
    # PSEUDO CODE
    
    # 1. Initialise lps array of length M (set each index to 0)
    # 2. Initialise variables j = 0
    # 3. Iterate through substring:
        # While char at j and char at i don't match, move j back to lps[j - 1]
        # If char at j and chat at i match, then lps[j] = lps[j - 1] + 1
    
        
    return lps

def KnuthMorrisPratt(text: str, substring: str):
    """KMP algorithm using lps table

    Arguments
    ----------
    text: type `str`
    substring: type `str`

    Return: 
    Let M = len(substring)
    - found: array of ints, where for each i, text[i: i + M] = substring,
    aka. list of start indices for substring matches
    - Your array should be in ascending order
    """
    lps = buildLPS(substring)
    i,j = 0,0
    out = []
    while i < len(text):
        if text[i] == substring[j]:
            i += 1
            j += 1
            if j == len(substring):
                out.append(i - j)
                j = lps[j - 1]
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]

    return out
    # PSEUDO CODE
    
    # 1. Initialise lps using buildLPS function
    # 2. Initialise variable j to 0 (j keeps track of matched chars)
    # 3. Iterate through text:
        # a. If encounter match, increment j
        # b. If mismatch, j = lps[j - 1] until j = 0 or text[i] = substring[j]
        # c. If j is length of substring, then substring match has occured,
        # add index of start of substring within text to result arr

NO_OF_CHARS = 256

# ord('A') # convert char to ascii number: 65
# chr(65)  # convert ascii number to char: 'A'

def buildDFA(substring):
    # TO IMPLEMENT
	M = len(substring)
	dfa = [[0 for j in range(M + 1)] for i in range(NO_OF_CHARS)]
 
	if substring == "":
		return dfa

	dfa[ord(substring[0])][0] = 1
 
	for j in range(1, M + 1):
		
		if j == M:
			charIndex = None
		else:
			charIndex = ord(substring[j])
		
		for i in range(NO_OF_CHARS):
			if i == charIndex:
				dfa[i][j] = j + 1
				
			else:
				toSimulate = substring[1 : j]
				reached = 0
				for char in toSimulate:
					reached = dfa[ord(char)][reached]

				reached = dfa[i][reached]
				dfa[i][j] = reached
    
	return dfa


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
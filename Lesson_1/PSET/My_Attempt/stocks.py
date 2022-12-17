import csv
from sys import argv

'''
    This function should 
        1. Return a list containing all pairs of companies that sum up to budget
        2. Make use of a python dict / set (hash table)
        3. Have worst case time complexity O(N) [Assuming hash table insertion is constant]
'''
def doubles(companies, prices, budget):
    # TO IMPLEMENT
  #
  out_list = []
  h_t = {}
  #for each comp-price pair...
  for x in range(len(companies)):
    no_1 = prices[x]
    no_2 = budget - no_1
    #if complement doesnt exist
    if h_t.get(no_2) == None:
      #add no_1 into the h_t
      h_t[no_1] = companies[x]
    else:
        out_list.append([h_t[no_2],companies[x]])
  return out_list

'''
    This function should
        1. Return a list containing all triplets of stock names with prices that sum up to budget
        2. Have worst case time complexity O(N^2) [Assuming hash table insertion is constant]

    Hint: If your doubles function runs in O(N) time, think about how you can call it in triples
'''

def triples(companies, prices, budget):
    # TO IMPLEMENT
  out_list = []
  for x in range(len(prices)):
    no_3 = prices[0]
    company_3 = companies[0]
    two_sum = budget - no_3
    #prepping inputs for doubles function that takes two_sum as input
    del companies[0]
    del prices[0]
    list_2_sum = doubles(companies,prices,two_sum)
    #appending no_3 to every element list in list_2_sum
    for x in list_2_sum:
      x.append(company_3)
    out_list.extend(list_2_sum)
  return out_list


def main():
    if len(argv) != 3:
        print('missing filename or budget as command line argument')
        return

    filename = argv[1]
    budget = int(argv[2])

    companies = []
    prices = []
    with open('prices/' + filename, 'r') as csv_file:
        myReader = csv.reader(csv_file)
        lineCount = 0
        for row in myReader:
            if lineCount == 0:
                lineCount += 1
                continue

            companies.append(row[0])
            prices.append(int(row[1]))

    print("doubles result:", doubles(companies, prices, budget))
    print()
    print("triples result:", triples(companies, prices, budget))

if __name__ == "__main__":
    main()

from collections import deque

#----------#

allwords = [i for i in open('englishwords.txt').read().split('\n') if len(i) == 4]

word1 = ''
word2 = ''
count = 0

def check1():
  
  global word1
  global word2
  global count
  
  while len(word1) != 4 and word1 not in allwords or len(word1) == 4 and word1 not in allwords:
    if count == 0:
      print('Word 1: ')
    word1 = input()
    count += 1
    
    if len(word1) != 4:
      print('Word must be 4 characters long. Re-enter Word 1: ')
    if len(word1) == 4 and word1 not in allwords:
      print('Word is not valid. Re-enter Word 1: ')
    if len(word1) == 4 and word1 in allwords:
      count = 0

def check2():
  
  global word1
  global word2
  global count
  
  count = 0
  
  while len(word2) != 4 and word2 not in allwords or len(word2) == 4 and word2 not in allwords:
    if count == 0:
      print('Word 2: ')
    word2 = input()
    count += 1
    
    if len(word2) != 4:
      print('Word must be 4 characters long. Re-enter Word 2: ')
    if len(word2) == 4 and word2 not in allwords:
      print('Word is not valid. Re-enter Word 2: ')
  



check1()
check2()

print('Your words are: ' + word1+ ', ' + word2)

#-----------------------------------#

word1_2 = [*word1]
word2_2 = [*word2]

print(word1, word2)

graph = {}
adjacentwords = []
keys = []
values = []

#making new words; populating "values" w/ them

#make keys (adjacent words to input
def listadjacent(w):
  adjacentwords = []
  for i in range(4):
    for a in range(97, 123):
      w = [*word1]
      
      w[i] = chr(a)
      
      #joins the word; checks if it exists
      w = ''.join(w)
      if w in allwords:
        adjacentwords.append(w)



keys = allwords

tree = {keys[w]: listadjacent(allwords[w]) for w in range(len(keys))}

print(tree)

"""def shortestpath(word1, word2, tree):

  if word1 == word2:
    print(word1, word2)

#current level; cosmetic
level = 0
ladder = []

Q = deque()
Q.append(word1)

while (len(Q) > 0):
  level += 1

  for i in range(len(Q)):
    word = [a for a in Q.popleft()]
    Q.append(''word)
  """

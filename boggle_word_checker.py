"""
This is a problem as described on CodeWars by user evan-eleven

"Boggle Word Checker"

Write a function that determines whether a string is a valid guess in a Boggle board, as per the rules of Boggle. 
A Boggle board is a 2D array of individual characters, e.g.:

[ ["I","L","A","W"],
  ["B","N","G","E"],
  ["I","U","A","O"],
  ["A","S","R","L"] ]

Valid guesses are strings which can be formed by connecting adjacent cells (horizontally, vertically, or diagonally) 
without re-using any previously used cells. For example, in the above board "BINGO", "LINGO", and "ILNBIA" would all 
be valid guesses, while "BUNGIE", "BINS", and "SINUS" would not. Your function should take two arguments (a 2D array 
and a string) and return true or false depending on whether the string is found in the array as per Boggle rules.

SOLUTION:

Uses a variation of BFS (breadth-first search). At each point, we have all possible paths stored up until the ith letter
of the word. Then we look at the (i+1)th letter, and see if it can be reached from any of the ends of the existing paths 
*without* overlapping with the existing path. If so we store all possible longer paths and repeat with the next letter 
of the word. If there's a path at the end, this means we have found the full word. If not, then a path does not exist.
"""

import numpy as np

def find_letter(board, c, x, y):
    return {(i+x-(1 if x!=0 else 0),j+y-(1 if y!=0 else 0)) for i in range(board.shape[0]) for j in range(board.shape[1]) if board[i,j]==c}

def find_word(board, word , returnPath = False):
    board = np.array(board)
    ithLetterPos = [[(x,y)] for x in range(board.shape[0]) for y in range(board.shape[1]) if board[x,y]==word[0]]
    nextLetterPos = []
    for i in range(1,len(word)):
        for path in ithLetterPos:
            x,y = path[-1]
            nextLetterPos += [ path + [tpl] for tpl in find_letter(board[max(x-1,0):x+2,max(y-1,0):y+2], word[i],x,y) if tpl not in path]
        ithLetterPos, nextLetterPos = nextLetterPos, []
    return ithLetterPos != [] if not returnPath else (ithLetterPos != [], ithLetterPos)

def main():
    board = [ ["I","L","A","W"],
              ["B","N","G","E"],
              ["I","U","A","O"],
              ["A","S","R","L"] ]
    print(find_word(board, 'BINGO'))

if __name__=='__main__':
    main()

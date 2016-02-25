#!/usr/bin/python
import numpy as np
#convert from strings to numpy array of chars
#fname = "sudoku-task1.txt"
fname = "sudoku-task2.txt"
with open(fname) as f:
    array = []
    for line in f:
        if (len(line)>9):
            splitted = line.split()
            joined = ""
            for numbers in splitted:
                joined += numbers
            array.append(joined)
joined = ""
for numbers in array:
    joined += numbers
numbers = []
for char in joined:
    numbers.append(int(char))
field = np.asarray(numbers)
field = np.reshape(field,(9,9))
print("Sudoku to solve")
print(field)

def isInArray(array, char):
    if char in array:
        return True
    else:
        return False
    
def get_row(array, index):
    return array[index]

def get_column(array, index):
    return array[:,index]


def get_subsell(array, index):
    if index > 8 or index < 0:
        print("ERROR!!! Subsell index is not in 0..8 range")
        raise
    row = int(index/3)
    column = index % 3
    return array[row*3:row*3+3, column*3:column*3+3]

def get_subcell_index(row,column):
    sub_row = int(row/3)
    sub_column = int(column/3)
    return sub_row*3 + sub_column
    
def isValueUsed(array, value, row, column):
    verbose = False
    # if row == 3 and column == 2:
    #         verbose = True
    if verbose:
        print(get_row(array,row))
    if isInArray(get_row(array,row),value) :
        return True
    if verbose:
        print()
    if isInArray(get_column(array,column),value) :
        return True
    if verbose:
        print()
    if isInArray(get_subsell(array,
        get_subcell_index(row,column)
        ),value) :
        return True
    return False

#print simple solve
def simple_solve (field):
    changes = True
    while changes:
        changes = False
        for column in range(9):
            for row in range(9):
                if not (field[row,column] == 0):
                    continue
                counts = 0
                new_value = 0
                for value in range(1,10):
                    if not isValueUsed(field,value,row,column):
                        counts += 1
                        new_value = value
                    if counts > 1:
                        break
                if counts == 1:
                    field[row,column] = new_value
                    changes = True
    return field

def isSolved (array):
    return not isInArray(array,0)

def GetZeroPosition(array):
    for column in range(9):
        for row in range(9):
            if field[row,column] == 0:
                return row,column
    return 9,9

def GetGuesses(array, row, column):
    guesses = []
    for value in range(1,10):
        if not isValueUsed(field,value,row,column):
            guesses.append((value,row,column))
    return guesses

def UseGuess(array, guess):
    array[guess[1],guess[2]] = guess[0]
    return array
    
field = simple_solve(field)
row,column = GetZeroPosition(field)
stack = []
guesses = []
stack.append(field)
guesses.append(GetGuesses(field,row,column))
#guesses[-1].pop() ## TODO remove debug
while not isSolved(field):
    # Stop if there is no guesses.
    if len(guesses) == 0:
        print("No more guesses")
        break
    # Return to previous branch if current branch failed to solve
    if len(guesses[-1]) == 0:
        field = stack.pop()
        guesses.pop()
        continue
    # try a guess
    field = np.copy(stack[-1])
    guess = guesses[-1].pop()
    field = UseGuess(field,guess)
    field = simple_solve(field)
    if isSolved(field):
        break
    row,column = GetZeroPosition(field)
    stack.append(field)
    guesses.append(GetGuesses(field,row,column))
    print("Stack size = "+str(len(stack)))
    
if isSolved(field):
    print("Solution result:")
    print(field)
else:
    print("Solution FAILED! Last state:")
    print(field)

#!/usr/bin/python
import numpy as np
#convert from strings to numpy array of chars
fname = "sudoku-task1.txt"
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
    array = np.reshape(array,9)
    #print(array)
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
for value in range(1,10):
    print value

#print simple solve
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
    

print("Sudoku to solve")
print(field)



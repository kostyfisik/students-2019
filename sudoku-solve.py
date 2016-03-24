import numpy as np
import copy as cp
#fname = "sudoku-task1.txt"
fname = "sudoku-task2.txt"

def get_options_temp(array):
    temp=np.array([1,2,3,4,5,6,7,8,9])
    options=[]
    for i in range(9):
        for j in range(9):
            if array[i,j]==0:
                options.append(a)
            else:
                options.append(0)   
    print(a)
    print(options)
    
def is_in_array(array, char):
    if char in array:
        return True
    else:
        return False

def get_row(array, index):
    return array[index]

def get_column(array, index):
    return array[:, index]

def get_cell(array, row, column):
    temp = np.zeros(9, dtype=np.int8)
    count=0
    for i in range((row//3)*3, (row//3)*3+3):
        for j in range((column//3)*3, (column//3)*3+3):
            temp[count]=array[i,j]
            count+=1
    return temp
         
                
def get_options(array, row, column):
    temp=[]
    for value in range(1,10):
        if (not is_in_array(get_row(array, row), value) 
            and not is_in_array(get_column(array, column), value) 
            and not is_in_array(get_cell(array, row, column), value)):
            temp.append(value)
    answer=np.array((temp), dtype=np.int8)
    return answer
            
def step_1(array):
    changed = True
    while changed:
        changed = False
        list_of_options=[]
        for i in range(9):
            for j in range(9):
                list_of_options.append(get_options(array, i, j))
        count=0
        for i in range(9):
            if changed:
                break            
            else:
                for j in range(9):
                    if changed:
                        break
                    else:
                        if len(list_of_options[count])==1 and array[i,j]==0:
                            array[i,j] = int(list_of_options[count])                            
                            changed = True                        
                        count+=1                        
    return array

def step_2(array):
    temp1=cp.copy(array)
    changed = True
    while changed:
        changed = False
        list_of_options=[]
        for i in range(9):
            for j in range(9):
                list_of_options.append(get_options(array, i, j))
        count=0
        for i in range(9):
            if changed:
                break            
            else:
                for j in range(9):
                    if changed:
                        break
                    else:
                        if len(list_of_options[count])==2 and array[i,j]==0:
                            row=i
                            column=j
                            value=list_of_options[2]
                            temp1[i,j] = int(list_of_options[count][1])
                            step_1(temp1)
                            if is_correct(temp1):
                                return temp1                                
                            else:
                                array[row, column] = value
                                step_1(array)
                                return array
                            changed = True                
                        count+=1                        

def is_solved(array):
    if 0 in array:
        return False
    else:
        return True

def validation(array):   
    if is_correct(array):        
        return(array)       
    else:
        print('ERROR! Last statement:')
        print(array2)
        raise
                                                   
def is_correct(array):
    for row in range(9):
        for value in range(1,10):
            if get_row(array, row).tolist().count(value)>1:
                return False
            else:
                for column in range(9):
                    for value in range(1,10):
                        if get_column(array, column).tolist().count(value)>1:
                            return False
                        else:
                            for row in [0,3,6]:
                                for column in [0,3,6]:
                                    for value in range(1,10):
                                        if get_cell(array, row, column).tolist().count(value)>1:
                                            return False
                                        else:
                                            return True

sudoku = np.zeros((9,9), dtype=np.int8)
f = open(fname)
inputmas= f.read()
splitted=inputmas.split()
joined=""
for numbers in splitted:
    joined+=numbers
i=0
j=0
for numbers in joined:
    sudoku[i,j]=int(numbers)
    j+=1
    if j>8:
        j=0
        i+=1
print('Sudoku to solve:')
print(sudoku)
temp_sudoku=cp.copy(sudoku)
temp_sudoku=step_1(temp_sudoku)
sudoku=np.copy(validation(temp_sudoku))
sudoku=np.copy(validation(temp_sudoku))
if is_solved(sudoku):
    print('Sudoku is solved. Ansewer: ')
    print(sudoku)
    raise
count=0
while not is_solved(temp_sudoku):
    temp_sudoku=step_2(temp_sudoku)
    sudoku=np.copy(validation(temp_sudoku))
    count+=1
    if count>5:
        break
if is_solved(sudoku):
    print('Sudoku is solved. Ansewer: ')
    print(sudoku)    
else:
    print('Sudoku is not solved. The last statement: ')
    print(sudoku)    

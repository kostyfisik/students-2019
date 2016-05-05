#Pkg.update()
#Pkg.add("DataStructures")

using DataStructures

function load_field(filename)
    file = open(filename)
    lines = readlines(file)
    close(file)

    field = zeros(Int, (9,9))
    row = 1
    for line in lines
        line = chomp(line)
        if line != ""
            column = 1
            for s in line
                assert(column <= 9)
                if s != ' '
                    field[row, column] = parse(Int, s)
                    column += 1
                end
            end
            row += 1
        end
    end
    return field
end

function print_field(f)
    for i in 1:9
        if mod(i-1, 3) == 0
            print("-------------------------\n")
        end
        for j in 1:9
            if mod(j-1, 3) == 0
                print("| ")
            end
            print(f[i, j], ' ')
        end
        print("|\n")
    end
    print("-------------------------\n")
end

function get_row(field,i,j)
    return field[i, :]
end

function get_column(field,i,j)
    return reshape(field[:, j], 9)
end

function get_block(field,i,j)
    rows = 1:3
    columns = 1:3
    if i <= 3
        rows = 1:3
    elseif i <= 6
        rows = 4:6
    elseif i <= 9
        rows = 7:9
    end

    if j <= 3
        columns = 1:3
    elseif j <= 6
        columns = 4:6
    elseif i <= 9
        columns = 7:9
    end
    return reshape(field[rows, columns], 9)
end

function number_counter(set)
    count = zeros(Int, 10)

    for i in set
        count[i+1] += 1
    end
    return count
end

function is_valid_set(set)
    count = number_counter(set)
    if count[1] > 0
        return false
    end
    for i in count[2:10]
        if i > 1
            return false
        end
    end
    return true
end

function is_valid_field(field)
    for i in 1:9
        if !is_valid_set(get_row(field, i, 1))
            return false
        end
    end
    for j in 1:9
        if !is_valid_set(get_column(field, 1, j))
            return false
        end
    end
    for i in 1:9
        for j in 1:9
            if mod(i, 3) == 0 && mod(j, 3) == 0
                if !is_valid_set(get_block(field, i,j))
                    return false
                end
            end
        end
    end
    return true
end

function valid_numbers(field, i, j)
    valid = []
    row_counter = number_counter(get_row(field, i, j))
    column_counter = number_counter(get_column(field, i, j))
    block_counter = number_counter(get_block(field, i, j))
    for n in 2:10
        if row_counter[n] == 0 && column_counter[n] == 0 && block_counter[n] == 0
            push!(valid, n-1)
        end
    end
    return valid
end

function next_vacant(field)
    for i in 1:9
        for j in 1:9
            if field[i, j] == 0
                return i,j
            end
        end
    end
    return -1, -1
end

function solve_sudoku(field)
    field_stack = Stack(Any)
    push!(field_stack, field)
    do_shit = true
    while do_shit
        curr_field = pop!(field_stack)
        i, j = next_vacant(curr_field)
        if i == -1 && j == -1
            return curr_field
        end
        guesses = valid_numbers(curr_field, i, j)
        if length(guesses) == 0
            continue
        else
            for g in guesses
                guess = copy(curr_field)
                guess[i, j] = g
                push!(field_stack, guess)
            end
        end
        if length(field_stack) == 0
            do_shit = false
        end
    end
    return None
end


cd(dirname(@__FILE__))

#
# Solve Easy
#
field = load_field("./sudoku-task1.txt")
print_field(field)
f = solve_sudoku(field)
print_field(f)
print(is_valid_field(f))

#
# Solve Hard
#
field = load_field("./sudoku-task2.txt")
print_field(field)
f = solve_sudoku(field)
print_field(f)
print(is_valid_field(f))


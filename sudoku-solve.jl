

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
cd(dirname(@__FILE__))
pwd()
field = load_field("./sudoku-task1.txt")
print_field(field)


mod(3, 3)


# https://www.codewars.com/kata/536a155256eb459b8700077e
# Easier to understand solution would have been to assign directions, E,S,W,N
# Afterwards while loop through directions when obstacle is met. Currently, when obstacle is met, whole grid is
# being rotated.

def create_spiral(n):
    if not str(n).isnumeric() or n<1:
        return []
    # Generating empty grid
    grid = []
    for row in range(n):
        line = []
        for column in range(n):
            line.append(0)
        grid.append(line)

    # Empty x*x grid has been generated

    def rotate_grid(grid, n):
        if n == 1:
            return grid
        temp_grid = []
        for row in range(n):
            temp_line = []
            for column in range(n):
                temp_line.append(grid[column][n - row - 1])
            temp_grid.append(temp_line)
        return temp_grid

    # Generating Spiral
    num = 1
    while True:
        row_changed = False
        for row in range(n):
            for column in range(n):
                if grid[row][column] == 0:
                    grid[row][column] = num
                    num += 1
                    row_changed = True
            if row_changed:
                break
        if not row_changed:
            break
        grid = rotate_grid(grid, n)

    # Rotating grid to start at number 1

    while True:
        if grid[0][0] == 1:
            break
        grid = rotate_grid(grid, n)

    return grid


print(create_spiral(1))
print(create_spiral(2))
print(create_spiral(3))

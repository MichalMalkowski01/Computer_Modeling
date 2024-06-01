import numpy as np
import matplotlib.pyplot as plt

ROWS = 100
COLS = 100

grid = np.zeros((ROWS, COLS), dtype=int)

ant_row = ROWS // 2
ant_col = COLS // 2

direction = 0  

def langtons_ant_step(row, col, direction, grid):
    grid[row, col] = 1 - grid[row, col]
    
    if grid[row, col] == 0: 
        direction = (direction + 1) % 4  # turn right
    else: 
        direction = (direction - 1) % 4  # turn left
    
    if direction == 0:  # up
        row -= 1
    elif direction == 1:  # right
        col += 1
    elif direction == 2:  # down
        row += 1
    elif direction == 3:  # left
        col -= 1
    
    row %= ROWS
    col %= COLS
    
    return row, col, direction

iterations = 10000
for _ in range(iterations):
    ant_row, ant_col, direction = langtons_ant_step(ant_row, ant_col, direction, grid)

plt.imshow(grid, cmap=None, interpolation='nearest')
plt.show()

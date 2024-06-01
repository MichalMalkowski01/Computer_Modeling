import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ROWS = 256
COLS = 512

grid = np.random.randint(0,2,(ROWS,COLS))

def count_neighbors(grid):
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])
    neighbors_count = np.zeros_like(grid)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            neighbors_count += np.roll(np.roll(grid, i, axis=0), j, axis=1)
    return neighbors_count

def apply_rule(cell, neighbors_count):
    if cell == 1 and (neighbors_count == 2 or neighbors_count == 3):
        return 1
    elif cell == 0 and neighbors_count == 3:
        return 1
    else:
        return 0

vectorized_apply_rule = np.vectorize(apply_rule)

def update(frameNum, img, grid):
    neighbors_count = count_neighbors(grid)
    newGrid = vectorized_apply_rule(grid, neighbors_count)
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid),
                              frames=10,
                              interval=50,
                              save_count=50)

plt.show()


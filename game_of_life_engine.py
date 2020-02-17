import random
import time


def get_random_state(height, width):
    # fills a life_matrix by 1s and 0s based on 50/50 chance
    # and returns it
    life_matrix = []
    for i in range(height):
        arr = []
        for j in range(width):
            random_num = random.random()
            if random_num >= 0.5:
                arr.append(1)
            else:
                arr.append(0)
        life_matrix.append(arr)
    return life_matrix


def render_state(life_matrix):
    for row in life_matrix:
        string = ''
        for col in row:
            if col == 1:
                string += '██'
            else:
                string += '  '
        print(string)


def get_next_state(life_matrix):
    next_life_matrix = []
    for y in range(len(life_matrix)):
        arr = []
        # based on the given conditions of 'game of life', kill a  living cell, revive a dead cell, or do nothing
        for x in range(len(life_matrix[0])):
            alive_neighbors = get_alive_neighbors(life_matrix, [y, x])
            if life_matrix[y][x] == 1:
                if alive_neighbors < 2 or alive_neighbors > 3:
                    arr.append(0)
                else:
                    arr.append(1)
            else:
                if alive_neighbors == 3:
                    arr.append(1)
                else:
                    arr.append(0)
        next_life_matrix.append(arr)
    return next_life_matrix


def get_alive_neighbors(life_matrix, cell_indices):
    # the indices of a cell's neighbors relative to its own indices
    neighbors_relative_indices = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    count = 0
    # max index values for the x and y in the life_matrix
    max_y = len(life_matrix) - 1
    max_x = len(life_matrix[0]) - 1

    # checks to see if the neighbors of a cell are alive and increments count, if so
    for indices in neighbors_relative_indices:
        neighbor_y = cell_indices[0] + indices[0]
        neighbor_x = cell_indices[1] + indices[1]
        # checks to see if the particular neighbor's indices are within the allowable values for the given life_matrix
        if (0 <= neighbor_y <= max_y) and (0 <= neighbor_x <= max_x):
            if life_matrix[neighbor_y][neighbor_x] == 1:
                count = count + 1
    return count


def play_game_of_life(life_matrix):
    while True:
        render_state(life_matrix)
        life_matrix = get_next_state(life_matrix)
        time.sleep(0.2)


def load_state(file_path):
    life_matrix = []
    with open(file_path, 'r') as life_file:
        for line in life_file:
            arr = []
            for char in line:
                if char == '1':
                    arr.append(1)
                elif char == '0':
                    arr.append(0)
            life_matrix.append(arr)
    return life_matrix


def main():
    pass
    # life_matrix = load_state('ggg.txt')
    # play_game_of_life(life_matrix)


if __name__ == '__main__':
    main()
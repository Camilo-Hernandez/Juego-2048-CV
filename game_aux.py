from random import choice
ROW = 4

# ------------- Funciones para 2048 ------------- #

def show(board):
    """Print the 2048 board."""
    print("")
    for i in range(0, len(board), ROW):
        print("".join(("{0:^5}".format(cell) for cell in board[i:i+ROW])))
    print("")


def round(board):
    """
    Insert a 2 at a random available position (where a 0 sits).

    Return a new board.
    """
    index = choice(tuple(all_indices(board, 0)))
    return tuple(board[:index]) + (2,) + tuple(board[index+1:])


def shake(board, direction, max=2048):
    """
    Shake the board in a given direction in wasd.

    Return a new board.
    """
    rows = [*board]
    direction = direction.lower()
    if direction not in 'wasd':
        raise ValueError("{} does nothing".format(direction))

    for i in range(ROW):
        if direction == 'a':
            start = i * ROW
            end = start + ROW
            rows[start:end] = shake_row(board[start:end], max)

        elif direction == 'd':
            start = i * ROW - 1
            end = start + ROW
            # -1 is the last element and not the one before the first one.
            # None must be used instead.
            if start == -1:
                start = None
            rows[end:start:-1] = shake_row(board[end:start:-1], max)

        elif direction in 'w':
            rows[i::ROW] = shake_row(board[i::ROW], max)

        elif direction in 's':
            start = (ROW - 1) * ROW + i
            rows[start::-ROW] = shake_row(board[start::-ROW], max)
    return tuple(rows)


def shake_row(row, max=2048):
    """
    Shake a given row towards its beginning.

    Return a new row.
    """
    l = len(row)
    row = [i for i in row if i != 0]
    m = 2
    while m < max:
        indices = tuple(all_indices(row, m))
        n = m*2
        for i in indices[:-1]:
            if row[i] == row[i+1] == m:
                row[i] = n
                row[i+1] = None
        row = [i for i in row if i is not None]
        m = n

    row.extend([0] * (l - len(row)))
    return tuple(row)


def all_indices(haystack, needle):
    """Like list.index but for all the indices."""
    try:
        indice = -1
        while True:
            indice = haystack.index(needle, indice+1)
            yield indice
    except ValueError:
        pass


def cli():
    """Play the CLI version of the game."""
    board = tuple([0] * ROW**2)
    board = round(round(board))
    s = "w"
    while s in "wasd":
        show(board)
        s = input("Shake the board with WASD: ").lower()
        board = shake(board, s)
        board = round(board)



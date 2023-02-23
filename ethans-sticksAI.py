inf = float('inf')

def print_board(layout):
    '''Prints the board'''
    for i,row in enumerate(layout):
        print(f'Row: {i+1} {int(layout[i]) * "|"}')


def is_win(layout):
    '''Returns True if the game is won, False otherwise'''
    # check if only one row has a stick
    if sum(layout) == 1:
        return True
    else:
        return False


def is_loss(layout):
    '''Returns True if the game is lost, False otherwise'''
    # check if all rows have no sticks
    if sum(layout) == 0:
        return True
    else:
        return False


def get_next_states(layout):
    '''Returns all possible next game states'''
    # get all next possible moves and puts them into a list
    possibilites = []
    for row in range(3):
        for nums in range(1, layout[row] + 1):
            temp = list(layout)
            new = temp[row] - nums
            temp[row] = new
            possibilites.append(tuple(temp))
    return possibilites



def minimax(layout, p):
    def max_val(layout, player):
        if is_win(layout):
            return -player
        elif is_loss(layout):
            return player
        v = -inf
        for state in get_next_states(layout):
            v = max(v, min_val(state, -player))
        return v

    def min_val(layout, player):
        if is_win(layout):
            return -player
        elif is_loss(layout):
            return player
        v = inf
        for state in get_next_states(layout):
            v = min(v, max_val(state, -player))
        return v

    if p == 1:
        return max(get_next_states(layout), key=lambda s: min_val(s, -p))
    elif p == -1:
        return min(get_next_states(layout), key=lambda s: max_val(s, -p))



def test():
    assert minimax((0, 5, 3), 1) == (0, 3, 3)
    assert minimax((1, 3, 4), 1) == (1, 3, 2)
    assert minimax((0, 0, 4), 1) == (0, 0, 1)
    #assert minimax((3, 5, 7), 1) == (2, 5, 7)
    print('All tests passed.')


def run():
    # game loop
    STICKS = (3, 5, 7)
    while True:
        print()
        print_board(STICKS)
        print()
        print("AI's move:")
        STICKS = minimax(STICKS, 1)
        print_board(STICKS)
        # check if game is over
        if is_win(STICKS):
            print('You lose!')
            break
        elif is_loss(STICKS):
            print('You win!')
            break
        # get user input
        print('\nYour move:')
        while True:
            row = int(input('Row: '))
            sticks = int(input('Sticks: '))
            if row in range(1, 4) and sticks in range(1, STICKS[row - 1] + 1):
                break
            else:
                print('Invalid move.')
        # update board
        temp = list(STICKS)
        new = temp[row - 1] - sticks
        temp[row - 1] = new
        STICKS = tuple(temp)
        print_board(STICKS)
        # check if game is over
        if is_win(STICKS):
            print('You win!')
            break
        elif is_loss(STICKS):
            print('You lose!')
            break

#testing
#test()

#running the game
run()
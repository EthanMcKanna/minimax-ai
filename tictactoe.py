# tic tac toe AI using Minimax Algorithm
inf = float('inf')

LAYOUT = '_' * 9

def print_board(layout):
    print()
    for i in range(0, 9, 3):
        print(f" {layout[i]} | {layout[i+1]} | {layout[i+2]}")
        if i < len(layout) - 3: print('-' * 11)
    print()

def is_win(layout):
    '''True if a layout represents a game win, else False'''
    r1, r2, r3 = layout[:3], layout[3:6], layout[6:]
    rows = [r1, r2, r3]
    cols = list(zip(r1, r2, r3))
    diags = [(r1[0], r2[1], r3[2]), (r1[2], r2[1], r3[0])]
    for g in rows + cols + diags:
        if '_' not in g and len(set(g)) == 1:
            return True
    return False
    


def get_next_states(layout, val):
    '''Returns all possible next game states'''
    if val == 1:
        piece = 'x'
    else:
        piece = 'o'
    return [layout[:i] + piece + layout[i+1:] for i,p in enumerate(layout) if p == '_']

def minimax(layout, p):
    '''AI is 1, opponent is -1'''

    def max_val(layout, player):
        if is_win(layout):
            return -player
        elif '_' not in layout:
            return 0
        v = -inf
        for state in get_next_states(layout, player):
            v = max(v, min_val(state, -player))
        return v

    def min_val(layout, player):
        if is_win(layout):
            return -player
        elif '_' not in layout:
            return 0
        v = inf
        for state in get_next_states(layout, player):
            v = min(v, max_val(state, -player))
        return v

    if p == 1:
        return max(get_next_states(layout, p), key=lambda s: min_val(s, -p))
    elif p == -1:
        return min(get_next_states(layout, p), key=lambda s: max_val(s, -p))



def test():
    assert get_next_states('xxoo__xo_', 1) == ['xxoox_xo_', 'xxoo_xxo_', 'xxoo__xox']
    # horizontal
    assert is_win('ooo______') == True
    #vertical
    assert is_win('x__x__x__') == True
    #diag1 win
    assert is_win('x___x___x') == True
    #diag2 win
    assert is_win('__x__x__x') == True
    #no win
    assert is_win('o__x__o__') == False
    print('Tests passed')



def run():
    board = LAYOUT
    win = False
    while True:
        nboard = minimax(board, 1)
        print_board(nboard)
        if is_win(nboard) == True:
            break
        umove = int(input("Where would you like to move?"))
        nboard = nboard[:umove] + "o" + nboard[umove+1:]
        print_board(nboard)
        board = nboard
        if is_win(board) == True:
            break
    print("The game has ended!")



run()

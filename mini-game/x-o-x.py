import os  # for clearing screan
import platform  # for Check what OS you running on


def clear_screan():
    os.system('clear')  # on linux / os x


def print_board(board):
    print('\n' + str(board[0]), '|', str(board[1]), '|', str(board[2]))
    print('\n' + str(board[3]), '|', str(board[4]), '|', str(board[5]))
    print('\n' + str(board[6]), '|', str(board[7]), '|', str(board[8]))
    print('\n')


def is_free(board, entry):
    if board[entry - 1] == 'X' or board[entry - 1] == 'O':
        return False
    else:
        return True


def who_win(board):
    # Horizontal
    for i in range(0, 7, 3):
        if (board[i] == 'X' and board[i + 1] == 'X' and board[i + 2] == 'X') \
            or\
           (board[i] == 'O' and board[i + 1] == 'O' and board[i + 2] == 'O'):
            return board[i + 1]

    # Vertical
    for i in range(3):
        if (board[i] == 'X' and board[i + 3] == 'X' and board[i + 6] == 'X') \
            or \
           (board[i] == 'O' and board[i + 3] == 'O' and board[i + 6] == 'O'):
            return board[i + 3]

    # Cross
    if (board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or \
       (board[0] == 'O' and board[4] == 'O' and board[8] == 'O'):
        return board[4]

    if (board[2] == 'X' and board[4] == 'X' and board[6] == 'X') or \
       (board[2] == 'O' and board[4] == 'O' and board[6] == 'O'):
        return board[4]

    return 'Yet_None'


def is_finish(board):
    if who_win(board) == 'Yet_None':
        for i in range(9):
            if board[i] != 'X' and board[i] != 'O':
                return False
        return True
    else:
        return True


def create_children(board, turn):
    if is_finish(board):
        return []
    tree = []
    for i in range(0, 9):
        board_copy = list(board)
        if board_copy[i] == 'X' or board_copy[i] == 'O':
            continue
        board_copy[i] = turn
        tree.append(board_copy)
    return list(tree)


def bf_creator(root, turn):
    tree = []
    queue = [(tree, root, turn)]
    tree.append(root)
    while queue != []:
        elem = queue[0]
        queue.remove(elem)
        children = create_children(elem[1], elem[2])
        tmp_turn = 'O' if elem[2] == 'X' else 'X'
        for child in children:
            elem[0].append([child])
            queue.append((elem[0][-1], child, tmp_turn))
    return tree


def leaves(tree):
    last_children = []
    queue = [tree]
    while queue != []:
        elem = queue[0]
        queue.remove(elem)
        if len(elem) == 1:
            last_children.append(elem[0])
        elif len(elem) > 1:
            for child in elem[1:]:
                queue.append(child)
    return last_children


def probability(this_tree):
    probabilities = []
    for i in this_tree[1:]:
        all_leaves = leaves(i)
        count = 0
        for leaf in all_leaves:
            if who_win(leaf) == 'X':
                count -= 100
            elif who_win(leaf) == 'O':
                count += 1

        not_append = False
        if probabilities != []:
            for a in i[1:]:
                if who_win(a[0]) == 'X' and probabilities != []:
                    not_append = True
                    break

        if not_append == False:
            probabilities.append([count / len(all_leaves), i[0]])
    return probabilities


def play_ai(this_tree, board):
    bigger = []
    for i in probability(this_tree):
        if bigger == []:
            bigger = i
        elif i[0] > bigger[0]:
            bigger = i
    return bigger[1]


def play_game(inpt, board, tree):
    board[inpt - 1] = 'X'
    if is_finish(board) == False:
        play_len = 0
        for i in range(0, 9):
            if board[i] == 'X' or board[i] == 'O':
                play_len += 1
        if play_len <= 1:
            tree = bf_creator(board, 'O')
        else:
            for j in tree[1:]:
                for i in j[1:]:
                    if i[0] == board:
                        tree = i
                        break
        board = play_ai(tree, board)
    return board, tree


def print_try_again(board):
    clear_screan()
    print('Try Again!')
    print_board(board)


def main():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tree = [board, [], []]
    win = 'Yet_None'
    # exit_game = False
    # order = 'O'

    clear_screan()
    print('Artificial Intelligence Tic Tac Toe\n \
           =======================\n \
           Exit Game: 0')

    while win == 'Yet_None':
        print_board(board)

        while True:
            entry = int(input('X\'s turn: '))

            try:
                if entry > 0 and entry <= 9:
                    if entry == 0:
                        win = 'None'
                        break
                    elif is_free(board, entry):
                        board, tree = play_game(entry, board, tree)
                        print_board(board)
                        if is_finish(board):
                            win = who_win(board)
                        break
                    else:
                        print_try_again(board)
                else:
                    print_try_again(board)
            except:
                print_try_again(board)
        clear_screan()
        if is_finish(board) == True:
            win = who_win(board)
            if win == 'Yet_None':
                win = 'None'
            break
    clear_screan()
    print_board(board)
    print('Win: ' + win)

main()

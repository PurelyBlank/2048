from utilities import generate_piece, print_board

DEV_MODE = False


def main(game_board: [[int, ], ]) -> [[int, ], ]:
    """
    2048 main function, runs a game of 2048 in the console.

    Uses the following keys:
    w - shift up
    a - shift left
    s - shift down
    d - shift right
    q - ends the game and returns control of the console
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: returns the ending game board
    """
    # Initialize board's first cell
    # generate a random piece and location using the generate_piece function
    pos_val = generate_piece(game_board, False)  # True does not work, has "KEYERROR"

    # place the piece at the specified location
    game_board[pos_val["row"]][pos_val["column"]] = pos_val["value"]

    # Initialize game state trackers
    turn = 0  # if turn % 2 == 1, computers turn. If == 0, users turn

    # Game Loop
    while True:
        # break
        # Reset user input variable
        # Take computer's turn
        if turn % 2 == 0:
            # place a random piece on the board
            pos_val = generate_piece(game_board, False)  # True does not work, has "KEYERROR"
            game_board[pos_val["row"]][pos_val["column"]] = pos_val["value"]

            # check to see if the game is over using the game_over function
            if game_over(game_board) == True:
                break
            else:
                # Show updated board using the print_board function
                print_board(game_board)
                turn += 1
        else:
            # Take user's turn
            user_input = input()
            # Take input until the user's move is a valid key
            while user_input not in ('w', 'a', 's', 'd', 'q'):
                user_input = input()
            # if the user quits the game, print Goodbye and stop the Game Loop
            if user_input == 'q':
                print("Goodbye")
                break
            # Execute the user's move
            elif user_input == 'a':
                compare_board = game_board[:]
                for row in range(len(compare_board)):
                    for cell in range(len(compare_board[row])):
                        if cell + 1 > 3:
                            pass
                        elif compare_board[row][cell + 1] == compare_board[row][cell]:
                            compare_board[row][cell] *= 2
                            compare_board[row][cell + 1] = 0
                    for row in range(len(compare_board)):
                        tracker = 0  # keeps track how many times to append 0
                        real_list = []
                        for cell in range(len(compare_board[row])):
                            if compare_board[row][cell] == 0:
                                tracker += 1
                            else:
                                real_list.append(compare_board[row][cell])
                        for i in range(tracker):
                            real_list.append(0)
                        compare_board[row] = real_list
                if compare_board == game_board:
                    continue
                else:
                    game_board = compare_board
                turn += 1
                # if compare_board == game_board:
            elif user_input == 'd':
                for row in range(len(game_board)):
                    for cell in range(len(game_board[row]) - 1, 0, -1):
                        if game_board[row][cell - 1] == game_board[row][cell]:
                            game_board[row][cell] *= 2
                            game_board[row][cell - 1] = 0
                for row in range(len(game_board)):
                    tracker = 0
                    real_list = []
                    for cell in range(len(game_board[row])):
                        if game_board[row][cell] == 0:
                            tracker += 1
                        else:
                            real_list.append(game_board[row][cell])
                    for i in range(tracker):
                        real_list.insert(0, 0)
                    game_board[row] = real_list
                turn += 1

            elif user_input == 's':
                tracker = 0
                num = 0
                for row in range(len(game_board)):
                    for cell in range(len(game_board[row])):
                        if game_board[row][cell] == 0:
                            tracker += 1
                while num < tracker:
                    for row in range(len(game_board)):
                        for cell in range(len(game_board[row])):
                            if row + 1 > 3:
                                pass
                            else:
                                if game_board[row + 1][cell] == 0:
                                    game_board[row + 1][cell] = game_board[row][cell]
                                    game_board[row][cell] = 0
                    num += 1

                for row in range(len(game_board) - 1, 0, -1):
                    for cell in range(len(game_board[row])):
                        if game_board[row - 1][cell] == game_board[row][cell]:
                            game_board[row][cell] *= 2
                            game_board[row - 1][cell] = 0

                tracker = 0
                num = 0
                for row in range(len(game_board)):
                    for cell in range(len(game_board[row])):
                        if game_board[row][cell] == 0:
                            tracker += 1
                while num < tracker:
                    for row in range(len(game_board)):
                        for cell in range(len(game_board[row])):
                            if row + 1 > 3:
                                pass
                            else:
                                if game_board[row + 1][cell] == 0:
                                    game_board[row + 1][cell] = game_board[row][cell]
                                    game_board[row][cell] = 0
                    num += 1
                turn += 1

            elif user_input == 'w':  # shift up
                num = 0
                while num < 4:
                    for row in range(len(game_board) - 1, 0, -1):
                        for cell in range(len(game_board[row])):
                            if game_board[row - 1][cell] == 0:
                                game_board[row - 1][cell] = game_board[row][cell]
                                game_board[row][cell] = 0
                    num += 1

                for row in range(len(game_board)):
                    for cell in range(len(game_board[row])):
                        if row + 1 > 3:
                            pass
                        elif game_board[row + 1][cell] == game_board[row][cell]:
                            game_board[row][cell] *= 2
                            game_board[row + 1][cell] = 0

                num = 0
                while num < 4:
                    for row in range(len(game_board) - 1, 0, -1):
                        for cell in range(len(game_board[row])):
                            if game_board[row - 1][cell] == 0:
                                game_board[row - 1][cell] = game_board[row][cell]
                                game_board[row][cell] = 0
                    num += 1
                turn += 1
            else:
                continue

        # Check if the user wins
        for row in game_board:
            for cell in row:
                if cell == 2048:
                    print("You Win!")
                    return game_board
                else:
                    pass
    return game_board


def game_over(game_board: [[int, ], ]) -> bool:
    """
    Query the provided board's game state.

    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: Boolean indicating if the game is over (True) or not (False)
    """
    # Loop over the board and determine if the game is over
    """ Ex: game_board = [[1,2,3,0],
                          [5,0,7,4],
                          [9,10,10,0],
                          [0,14,0,16]] """
    count = 0
    for row in range(len(game_board)):
        for cell in range(len(game_board[row])):
            if game_board[row][cell] == 0:
                count += 1
            else:
                if row + 1 > 3:
                    if cell + 1 > 3:
                        pass
                    else:
                        if game_board[row][cell + 1] == game_board[row][cell]:
                            count += 1
                        else:
                            count += 0
                elif row + 1 <= 3:
                    if cell + 1 > 3:
                        pass
                    else:
                        if (game_board[row + 1][cell] == game_board[row][cell] or
                                game_board[row][cell + 1] == game_board[row][cell]):
                            count += 1
                        else:
                            count += 0
                else:
                    count += 0
    if count > 0:
        return False
    else:
        return True  # Don't always return false


if __name__ == "__main__":
    main([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])

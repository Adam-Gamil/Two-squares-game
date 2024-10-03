# Description of Game 3 (2 squares game): The game is played between 2 players each player takes a turn
# the player must choose 2 numbers from 1 to 16, but it should form a vertical or a horizontal rectangle shape
# a square cannot be covered twice, the last player who can place a card on the board is the winner.
# version: 1.0
# Date: 3/3/2024




numbers_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
# numbers_board contains all numbers from 1 to 16 and it will be used to show the user the board after every game
board = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
# board is used to check if the rest of the numbers left can form a horizontal or vertical rectangle or not
def display_board(): # function that call the board to be displayed to the player after every turn

    print("******************************")
    print(f"||  {numbers_board[0]}  ||  {numbers_board[1]}  ||  {numbers_board[2]}  ||  {numbers_board[3]}  ||")
    print(f"||  {numbers_board[4]}  ||  {numbers_board[5]}  ||  {numbers_board[6]}  ||  {numbers_board[7]}  ||")
    print(f"||  {numbers_board[8]}  ||  {numbers_board[9]} ||  {numbers_board[10]} ||  {numbers_board[11]} ||")
    print(f"||  {numbers_board[12]} ||  {numbers_board[13]} ||  {numbers_board[14]} ||  {numbers_board[15]} ||")
    print("******************************")
def check_winner_player1(board): # function that checks if player 1 is the winner or not

        # Convert strings to integers and sort the board
        board = sorted([int(num) for num in board])

        # Check if there are less than 2 squares left
        if len(board) < 2:
            return True

        # Check if any two squares are adjacent
        for i in range(len(board) - 1):
            # Check horizontal adjacency (difference is 1 and they are in the same row)
            if board[i] % 4 != 0 and board[i] + 1 == board[i + 1]:
                return False
            # Check vertical adjacency (difference is 4)
            if board[i] + 4 == board[i + 1]:
                return False

        # If no adjacent squares are found, player 1 has won
        return True
def check_winner_player2(board):
    # Convert strings to integers and sort the board
    board = sorted([int(num) for num in board])

    # Check if there are less than 2 squares left
    if len(board) < 2:
        return True

    # Check if any two squares are adjacent
    for i in range(len(board) - 1):
        # Check horizontal adjacency (difference is 1 and they are in the same row)
        if board[i] % 4 != 0 and board[i] + 1 == board[i + 1]:
            return False
        # Check vertical adjacency (difference is 4)
        if board[i] + 4 == board[i + 1]:
            return False

    # If no adjacent squares are found, player 2 has won
    return True

print("Welcome to two squares game")
print("The last player who can place a card on the board is the winner")
display_board()

def game(): # function game
    flag = True
    while flag:
        while True: # in this loop it checks if the number that player 1 entered is valid or not
            try:

                player1_1st_choice = input("Player1, please choose the first number from 1 to 16: ")
                player1_2nd_choice = input("Player1, please choose the second number from 1 to 16: ")

                # Check if the input is a positive integer
                if player1_1st_choice in numbers_board and player1_2nd_choice in numbers_board:
                    if player1_1st_choice.isdigit() and player1_2nd_choice.isdigit():
                        # Convert the input to an integer
                        num1 = int(player1_1st_choice)
                        num2 = int(player1_2nd_choice)


                        if num1 > 0 and num1 < 17 and num2 > 0 and num2 < 17:
                            break
                        else:
                            print("The number isn't in the list. Please try again.")
                else:
                    print("Invalid input. Please enter a valid integer.")

            except ValueError:
                print("Invalid input. Please enter a valid integer.")


        while True: # this loop checks the 3 conditions of player 1 first number comparing to the second number
            if (player1_1st_choice == '1' or player1_1st_choice == '2' or player1_1st_choice == '3' or
                    player1_1st_choice == '6' or player1_1st_choice == '7' or
                    player1_1st_choice == '10' or player1_1st_choice ==  '11' or
                    player1_1st_choice == '14' or player1_1st_choice == '15' or player1_1st_choice == '16'):
                if (int(player1_2nd_choice) == int(player1_1st_choice) - 1 or int(player1_2nd_choice) == int(player1_1st_choice) - 4 or
                        int(player1_2nd_choice) == int(player1_1st_choice) + 1 or
                        int(player1_2nd_choice) == int(player1_1st_choice) + 4):

                    board.remove(player1_1st_choice) # remove it from the board to use it later to check who is the winner
                    board.remove(player1_2nd_choice)

                    index1 = numbers_board.index(player1_1st_choice)
                    numbers_board[index1] = 'X'  # remove the number that the player had chosen it and replace it with X

                    index2 = numbers_board.index(player1_2nd_choice)
                    numbers_board[index2] = 'X'  # remove the number that the player had chosen it and replace it with X

                    display_board()
                    if check_winner_player1(board): # if true then announce that player 1 is the winner
                        print("Player 1 is the winner!")
                        return False
                    break

                else:
                    print("Invalid input, please try another 2 numbers")
                    while True:# in this loop it checks if the number that player 1 entered is valid or not
                        try:

                            player1_1st_choice = input("Player1, please choose the first number from 1 to 16: ")
                            player1_2nd_choice = input("Player1, please choose the second number from 1 to 16: ")

                            # Check if the input is a positive integer
                            if player1_1st_choice in numbers_board and player1_2nd_choice in numbers_board:
                                if player1_1st_choice.isdigit() and player1_2nd_choice.isdigit():
                                    # Convert the input to an integer
                                    num1 = int(player1_1st_choice)
                                    num2 = int(player1_2nd_choice)


                                    if num1 > 0 and num1 < 17 and num2 > 0 and num2 < 17:
                                        break
                                    else:
                                        print("The number isn't in the list. Please try again.")
                            else:
                                print("Invalid input. Please enter a valid integer.")

                        except ValueError:
                            print("Invalid input. Please enter a valid integer.")

                    continue

            elif player1_1st_choice == '5' or player1_1st_choice == '9' or player1_1st_choice == '13':
                if (int(player1_2nd_choice) == int(player1_1st_choice) - 4 or
                        int(player1_2nd_choice) == int(player1_1st_choice) + 1 or
                        int(player1_2nd_choice) == int(player1_1st_choice) + 4):
                    board.remove(player1_1st_choice)# remove it from the board to use it later to check who is the winner
                    board.remove(player1_2nd_choice)

                    index1 = numbers_board.index(player1_1st_choice)
                    numbers_board[index1] = 'X' # remove the number that the player had chosen it and replace it with X

                    index2 = numbers_board.index(player1_2nd_choice)
                    numbers_board[index2] = 'X' # remove the number that the player had chosen it and replace it with X

                    display_board()
                    if check_winner_player1(board):# if true then announce that player 1 is the winner
                        print("Player 1 is the winner!")
                        return False
                    break
                else:
                    print("Invalid input, please try another 2 numbers")
                    while True:
                        try:

                            player1_1st_choice = input("Player1, please choose the first number from 1 to 16: ")
                            player1_2nd_choice = input("Player1, please choose the second number from 1 to 16: ")

                            # Check if the input is a positive integer
                            if player1_1st_choice in numbers_board and player1_2nd_choice in numbers_board:
                                if player1_1st_choice.isdigit() and player1_2nd_choice.isdigit():
                                    # Convert the input to an integer
                                    num1 = int(player1_1st_choice)
                                    num2 = int(player1_2nd_choice)


                                    if num1 > 0 and num1 < 17 and num2 > 0 and num2 < 17:
                                        break
                                    else:
                                        print("The number isn't in the list. Please try again.")
                            else:
                                print("Invalid input. Please enter a valid integer.")

                        except ValueError:
                            print("Invalid input. Please enter a valid integer.")

                    continue

            elif player1_1st_choice == '4' or player1_1st_choice == '8' or player1_1st_choice ==  '12':
                if (int(player1_2nd_choice) == int(player1_1st_choice) - 4 or
                        int(player1_2nd_choice) == int(player1_1st_choice) - 1 or
                        int(player1_2nd_choice) == int(player1_1st_choice) + 4):
                    board.remove(player1_1st_choice)
                    board.remove(player1_2nd_choice)
                    index1 = numbers_board.index(player1_1st_choice)
                    numbers_board[index1] = 'X'

                    index2 = numbers_board.index(player1_2nd_choice)
                    numbers_board[index2] = 'X'

                    display_board()
                    if check_winner_player1(board):
                        print("Player 1 is the winner!")
                        return False
                    break
                else:
                    print("Invalid input, please try another 2 numbers")
                    while True:
                        try:

                            player1_1st_choice = input("Player1, please choose the first number from 1 to 16: ")
                            player1_2nd_choice = input("Player1, please choose the second number from 1 to 16: ")

                            # Check if the input is a positive integer
                            if player1_1st_choice in numbers_board and player1_2nd_choice in numbers_board:
                                if player1_1st_choice.isdigit() and player1_2nd_choice.isdigit():
                                    # Convert the input to an integer
                                    num1 = int(player1_1st_choice)
                                    num2 = int(player1_2nd_choice)


                                    if num1 > 0 and num1 < 17 and num2 > 0 and num2 < 17:
                                        break
                                    else:
                                        print("The number isn't in the list. Please try again.")
                            else:
                                print("Invalid input. Please enter a valid integer.")

                        except ValueError:
                            print("Invalid input. Please enter a valid integer.")

                    continue




                  ##############################
                  ######## Player 2 turn #######
                  ##############################


        while True:# in this loop it checks if the number that player 2 entered is valid or not
            try:

                player2_1st_choice = input("Player2, please choose the first number from 1 to 16: ")
                player2_2nd_choice = input("Player2, please choose the second number from 1 to 16: ")

                # Check if the input is a positive integer
                if player2_1st_choice in numbers_board and player2_2nd_choice in numbers_board:
                    if player2_1st_choice.isdigit() and player2_2nd_choice.isdigit():
                        # Convert the input to an integer
                        num3 = int(player2_1st_choice)
                        num4 = int(player2_2nd_choice)


                        if num3 > 0 and num3 < 17 and num4 > 0 and num4 < 17:
                            break
                        else:
                            print("The number isn't in the list. Please try again.")
                else:
                    print("Invalid input. Please enter a valid integer.")

            except ValueError:
                print("Invalid input. Please enter a valid integer.")


        while True: # this loop checks the 3 conditions of player 2 first number comparing to the second number

            if (player2_1st_choice == '1' or player2_1st_choice == '2' or player2_1st_choice == '3' or player2_1st_choice == '6' or
                    player2_1st_choice == '7' or player2_1st_choice == '10' or player2_1st_choice == '11'
                    or player2_1st_choice == '14' or player2_1st_choice == '15' or player2_1st_choice == '16'):

                if (int(player2_2nd_choice) == int(player2_1st_choice) - 1 or int(player2_2nd_choice) == int(player2_1st_choice) - 4 or
                        int(player2_2nd_choice) == int(player2_1st_choice) + 1 or int(player2_2nd_choice) == int(player2_1st_choice) + 4):
                    board.remove(player2_1st_choice)# remove it from the board to use it later to check who is the winner
                    board.remove(player2_2nd_choice)
                    index3 = numbers_board.index(player2_1st_choice)
                    numbers_board[index3] = 'X'  # remove the number that the player had chosen it and replace it with X

                    index4 = numbers_board.index(player2_2nd_choice)
                    numbers_board[index4] = 'X'  # remove the number that the player had chosen it and replace it with X

                    display_board()
                    if check_winner_player2(board):
                        print("Player 2 is the winner!") # if true then announce that player 2 is the winner
                        return False
                    break

                else:
                    print("Invalid input, please try another 2 numbers")
                    while True:
                        try:
                            # Ask the user to choose a number
                            player2_1st_choice = input("Player2, please choose the first number from 1 to 16: ")
                            player2_2nd_choice = input("Player2, please choose the second number from 1 to 16: ")

                            # Check if the input is a positive integer
                            if player2_1st_choice in numbers_board and player2_2nd_choice in numbers_board:
                                if player2_1st_choice.isdigit() and player2_2nd_choice.isdigit():
                                    # Convert the input to an integer
                                    num3 = int(player2_1st_choice)
                                    num4 = int(player2_2nd_choice)

                                    # Validate the user's choice
                                    if num3 > 0 and num3 < 17 and num4 > 0 and num4 < 17:
                                        break
                                    else:
                                        print("The number isn't in the list. Please try again.")
                            else:
                                print("Invalid input. Please enter a valid integer.")

                        except ValueError:
                            print("Invalid input. Please enter a valid integer.")

                    continue

            elif player2_1st_choice == '5' or player2_1st_choice == '9' or player2_1st_choice == '13':
                if (int(player2_2nd_choice) == int(player2_1st_choice) - 4 or
                        int(player2_2nd_choice) == int(player2_1st_choice) + 1 or
                        int(player2_2nd_choice) == int(player2_1st_choice) + 4):

                    board.remove(player2_1st_choice)
                    board.remove(player2_2nd_choice)
                    index3 = numbers_board.index(player2_1st_choice)
                    numbers_board[index3] = 'X'

                    index4 = numbers_board.index(player2_2nd_choice)
                    numbers_board[index4] = 'X'
                    display_board()
                    if check_winner_player2(board):
                        print("Player 2 is the winner!")
                        return False
                    break
                else:
                    print("Invalid input, please try another 2 numbers")
                    while True:
                        try:
                            # Ask the user to choose a number
                            player2_1st_choice = input("Player2, please choose the first number from 1 to 16: ")
                            player2_2nd_choice = input("Player2, please choose the second number from 1 to 16: ")

                            # Check if the input is a positive integer
                            if player2_1st_choice in numbers_board and player2_2nd_choice in numbers_board:
                                if player2_1st_choice.isdigit() and player2_2nd_choice.isdigit():
                                    # Convert the input to an integer
                                    num3 = int(player2_1st_choice)
                                    num4 = int(player2_2nd_choice)

                                    # Validate the user's choice
                                    if num3 > 0 and num3 < 17 and num4 > 0 and num4 < 17:
                                        break
                                    else:
                                        print("The number isn't in the list. Please try again.")
                            else:
                                print("Invalid input. Please enter a valid integer.")

                        except ValueError:
                            print("Invalid input. Please enter a valid integer.")

                    continue

            elif player2_1st_choice == '4' or player2_1st_choice == '8' or player2_1st_choice == '12':
                if (int(player2_2nd_choice) == int(player2_1st_choice) - 4 or
                        int(player2_2nd_choice) == int(player2_1st_choice) - 1 or
                        int(player2_2nd_choice) == int(player2_1st_choice) + 4):

                    board.remove(player2_1st_choice)
                    board.remove(player2_2nd_choice)
                    index3 = numbers_board.index(player2_1st_choice)
                    numbers_board[index3] = 'X'

                    index4 = numbers_board.index(player2_2nd_choice)
                    numbers_board[index4] = 'X'
                    display_board()
                    if check_winner_player2(board):
                        print("Player 2 is the winner!")
                        return False
                    break
                else:
                    print("Invalid input, please try another 2 numbers")
                    while True:
                        try:
                            # Ask the user to choose a number
                            player2_1st_choice = input("Player2, please choose the first number from 1 to 16: ")
                            player2_2nd_choice = input("Player2, please choose the second number from 1 to 16: ")

                            # Check if the input is a positive integer
                            if player2_1st_choice in numbers_board and player2_2nd_choice in numbers_board:
                                if player2_1st_choice.isdigit() and player2_2nd_choice.isdigit():
                                    # Convert the input to an integer
                                    num3 = int(player2_1st_choice)
                                    num4 = int(player2_2nd_choice)

                                    # Validate the user's choice
                                    if num3 > 0 and num3 < 17 and num4 > 0 and num4 < 17:
                                        break
                                    else:
                                        print("The number isn't in the list. Please try again.")
                            else:
                                print("Invalid input. Please enter a valid integer.")

                        except ValueError:
                            print("Invalid input. Please enter a valid integer.")

                    continue
    return True



# the game starts from here

flag = True
while flag:
    flag = game() # call the function game that contains all the steps of the game

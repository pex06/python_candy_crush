"""
Title: Candy Crush-Inspired Python Game

Description:
This Python program implements a simplified version of the popular game Candy Crush. Players can create a game board with candies, select candies to play with, and attempt to match three or more candies in a row or column to score points. The game allows players to move candies within the board and strategically plan their moves to maximize points. The program features a simple text-based interface and provides an engaging gaming experience for users.
"""

import random

BOARD_ROWS = 5
BOARD_COLUMNS = 6


def create_board():
    global BOARD_ROWS
    global BOARD_COLUMNS

    for row in range(BOARD_ROWS):
        board.append(["_" for i in range(BOARD_COLUMNS)])


def display_board(board):
    print("\n")

    for row in board:
        for cell in row:
            print(cell, end=" ")
        print("\n")


def request_player(player):
    player["name"] = input("\nPlayer name > ")
    candy = None

    print("\nAdd the candies you want to play with (MIN 3, MAX 5)\n")

    while len(player["candies"]) < 5:
        if candy == "EXIT" and len(player["candies"]) >= 3:
            break
        else:
            candy = input('Add candy ("EXIT" to finish selection) > ')
            if candy != "EXIT":
                player["candies"].append(candy)

    print(f'Candies: {player["candies"]}')


def fill_board(board):
    for row in board:
        index = 0
        for cell in row:
            if cell == "_":
                candy = random.choice(player["candies"])
                row[index] = candy
            index += 1
    display_board(board)


def break_candies(board):

    break_candies_in_rows(board)
    break_candies_in_columns(board)

    for row in board:
        if "_" in row:
            display_board(board)
            break
    else:
        pass


def break_candies_in_rows(board):
    for row in board:
        for index in range(len(row) - 2):
            if row[index] == row[index + 1] == row[index + 2]:
                row[index:index + 3] = ["_"] * 3


def break_candies_in_columns(board):
    for index_row in range(BOARD_ROWS):
        column = [row[index_row] for row in board]

        index = 0
        while index < len(column) - 2:
            if column[index] == column[index + 1] == column[index + 2]:
                for offset in range(3):
                    board[index + offset][index_row] = "_"
                index += 3  # Skip the next two candies after breaking three consecutive ones
            else:
                index += 1


def player_points(board):
    global points

    points = 0

    for row in board:
        for cell in row:
            if cell == "_":
                points += 1

    player["scores"].append(points)
    print(f"Points: {sum(player['scores'])}")


def move_candy(board):
    candy_row = int(
        input(f"What row is the candy in? [0 - {BOARD_ROWS-1}] > "))
    candy_cell = int(
        input(f"What candy do you want to move? [0 - {BOARD_COLUMNS-1}] > "))

    candy_before = board[candy_row][candy_cell]
    candy_after = None

    if candy_before == "_" or candy_after == "_":
        print("Error: Invalid cell")
        player_movement()

    if candy_row == 0:
        if candy_cell == 0:
            move = input("Where to move [R]ight, [D]own > ")
        if 0 < candy_cell < BOARD_COLUMNS - 1:
            move = input("Where to move [L]eft, [R]ight, [D]own > ")
        if candy_cell == BOARD_COLUMNS - 1:
            move = input("Where to move [L]eft, [D]own > ")
    elif candy_row == BOARD_ROWS - 1:
        if candy_cell == 0:
            move = input("Where to move [R]ight, [U]p > ")
        if 0 < candy_cell < BOARD_COLUMNS - 1:
            move = input("Where to move [L]eft, [R]ight, [U]p > ")
        if candy_cell == BOARD_COLUMNS - 1:
            move = input("Where to move [L]eft, [U]p > ")
    else:
        if candy_cell == 0:
            move = input("Where to move [R]ight, [U]p, [D]own > ")
        if 0 < candy_cell < BOARD_COLUMNS - 1:
            move = input("Where to move [L]eft, [R]ight, [U]p, [D]own > ")
        if candy_cell == BOARD_COLUMNS - 1:
            move = input("Where to move [L]eft, [U]p, [D]own > ")

    if move == "L":
        candy_after = board[candy_row][candy_cell - 1]
        board[candy_row][candy_cell - 1] = candy_before
    elif move == "R":
        candy_after = board[candy_row][candy_cell + 1]
        board[candy_row][candy_cell + 1] = candy_before
    elif move == "U":
        candy_after = board[candy_row - 1][candy_cell]
        board[candy_row - 1][candy_cell] = candy_before
    elif move == "D":
        candy_after = board[candy_row + 1][candy_cell]
        board[candy_row + 1][candy_cell] = candy_before

    board[candy_row][candy_cell] = candy_after

    break_candies(board)
    player_points(board)


def player_movement():
    option = None

    while option != "A":
        option = input(
            "\nWhat do you want to do? [S]how board, [C]hoose candy, [A]bandon round and start another > ")

        if option == "S":
            display_board(board)
        elif option == "C":
            move_candy(board)
        elif option == "A":
            main()


def main():
    global board, player, points

    board = []
    player = {
        "name": "",
        "scores": [],
        "candies": []
    }

    create_board()
    display_board(board)
    request_player(player)

    while True:
        fill_board(board)
        break_candies(board)
        player_points(board)

        if points == 0:
            player_movement()


main()

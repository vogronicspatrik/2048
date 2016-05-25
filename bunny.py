import curses
import random
import os

highscore = 0

if os.path.exists("highscore.txt"):
    score = open("highscore.txt", "r")
    highscore = score.readlines()[0].strip()
    score.close()


def border():
    win.border("+", "+", "+", "+", "+", "+", "+", "+")


screen = curses.initscr()
screen.keypad(1)
win = curses.newwin(24, 80, 0, 0)
curses.noecho()
curses.curs_set(0)

# Game Initialization

khopi_attempt = 0
points = 0

game_box = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
first_position_list = [0, 1, 2, 3]
first_row_to_begin = random.choice(first_position_list)
first_column_to_begin = random.choice(first_position_list)
game_box[first_row_to_begin][first_column_to_begin] = 2

# Up movement functions


def up_movement(game_box):
    i = 0
    for j in range(0, 4):
        if game_box[i][j] != 0 or game_box[i+1][j] != 0 or \
           game_box[i+2][j] != 0 or game_box[i+3][j] != 0:
            if game_box[i][j] == 0:
                while game_box[i][j] == 0:
                    game_box[i][j] = game_box[i+1][j]
                    game_box[i+1][j] = game_box[i+2][j]
                    game_box[i+2][j] = game_box[i+3][j]
                    game_box[i+3][j] = 0

            if game_box[i+1][j] == 0 and (game_box[i+2][j] != 0 or
               game_box[i+3][j] != 0):
                while game_box[i+1][j] == 0:
                    game_box[i+1][j] = game_box[i+2][j]
                    game_box[i+2][j] = game_box[i+3][j]
                    game_box[i+3][j] = 0
            if game_box[i+2][j] == 0 and game_box[i+3][j] != 0:
                while game_box[i+2] == 0:
                    game_box[i+2] = game_box[i+3]
                    game_box[i+3][j] = 0

# After up movements


def up_addition(game_box):
    i = 0
    global points
    for j in range(0, 4):
        if game_box[i][j] == game_box[i+1][j]:
            game_box[i][j] = game_box[i][j]+game_box[i+1][j]
            points += game_box[i][j] ** 2
            game_box[i+1][j] = game_box[i+2][j]
            game_box[i+2][j] = game_box[i+3][j]
            game_box[i+3][j] = 0

        if game_box[i+1][j] == game_box[i+2][j]:
            game_box[i+1][j] = game_box[i+1][j]+game_box[i+2][j]
            points += game_box[i+1][j] ** 2
            game_box[i+2][j] = game_box[i+3][j]
            game_box[i+3][j] = 0

        if game_box[i+2][j] == game_box[i+3][j]:
            game_box[i+2][j] = game_box[i+2][j]+game_box[i+3][j]
            points += game_box[i+2][j] ** 2
            game_box[i+3][j] = 0

# Down movement functions


def down_movement(game_box):
    i = 0
    for j in range(0, 4):
        if game_box[i][j] != 0 or game_box[i+1][j] != 0 or \
           game_box[i+2][j] != 0 or game_box[i+3][j] != 0:
            if game_box[i+3][j] == 0:
                while game_box[i+3][j] == 0:
                    game_box[i+3][j] = game_box[i+2][j]
                    game_box[i+2][j] = game_box[i+1][j]
                    game_box[i+1][j] = game_box[i][j]
                    game_box[i][j] = 0

            if game_box[i+2][j] == 0 and (game_box[i+1][j] != 0 or
               game_box[i][j] != 0):
                while game_box[i+2][j] == 0:
                    game_box[i+2][j] = game_box[i+1][j]
                    game_box[i+1][j] = game_box[i][j]
                    game_box[i][j] = 0

            if game_box[i+1][j] == 0 and game_box[i][j] != 0:
                while game_box[i+1][j] == 0:
                    game_box[i+1][j] = game_box[i][j]
                    game_box[i][j] = 0

# After down movement functions


def down_addition(game_box):
    i = 0
    global points
    for j in range(0, 4):
        if game_box[i+3][j] == game_box[i+2][j]:
            game_box[i+3][j] = game_box[i+3][j] + game_box[i+2][j]
            points += game_box[i+3][j] ** 2
            game_box[i+2][j] = game_box[i+1][j]
            game_box[i+1][j] = game_box[i][j]
            game_box[i][j] = 0

        if game_box[i+2][j] == game_box[i+1][j]:
            game_box[i+2][j] = game_box[i+2][j]+game_box[i+1][j]
            points += game_box[i+2][j] ** 2
            game_box[i+1][j] = game_box[i][j]
            game_box[i][j] = 0

        if game_box[i+1][j] == game_box[i][j]:
            game_box[i+1][j] = game_box[i+1][j]+game_box[i][j]
            points += game_box[i+1][j] ** 2
            game_box[i][j] = 0

# Left movement function


def left_movement(game_box):
    j = 0
    for i in range(0, 4):
        if game_box[i][j] != 0 or game_box[i][j+1] != 0 or \
           game_box[i][j+2] != 0 or game_box[i][j+3] != 0:
            if game_box[i][j] == 0:
                while game_box[i][j] == 0:
                    game_box[i][j] = game_box[i][j+1]
                    game_box[i][j+1] = game_box[i][j+2]
                    game_box[i][j+2] = game_box[i][j+3]
                    game_box[i][j+3] = 0

            if game_box[i][j+1] == 0 and (game_box[i][j+2] != 0 or
               game_box[i][j+3] != 0):
                while game_box[i][j+1] == 0:
                    game_box[i][j+1] = game_box[i][j+2]
                    game_box[i][j+2] = game_box[i][j+3]
                    game_box[i][j+3] = 0

            if game_box[i][j+2] == 0 and (game_box[i][j+3] != 0):
                while game_box[i][j+2] == 0:
                    game_box[i][j+2] = game_box[i][j+3]
                    game_box[i][j+3] = 0

# After left movement function


def left_addition(game_box):
    j = 0
    global points
    for i in range(0, 4):
        if game_box[i][j] == game_box[i][j+1]:
            game_box[i][j] = game_box[i][j]+game_box[i][j+1]
            points += game_box[i][j] ** 2
            game_box[i][j+1] = game_box[i][j+2]
            game_box[i][j+2] = game_box[i][j+3]
            game_box[i][j+3] = 0

        if game_box[i][j+1] == game_box[i][j+2]:
            game_box[i][j+1] = game_box[i][j+1]+game_box[i][j+2]
            points += game_box[i][j+1] ** 2
            game_box[i][j+2] = game_box[i][j+3]
            game_box[i][j+3] = 0

        if game_box[i][j+2] == game_box[i][j+3]:
            game_box[i][j+2] = game_box[i][j+2]+game_box[i][j+3]
            points += game_box[i][j+2] ** 2
            game_box[i][j+3] = 0

# Right movement function


def right_movement(game_box):
    j = 0
    for i in range(0, 4):
        if game_box[i][j] != 0 or game_box[i][j+1] != 0 or \
           game_box[i][j+2] != 0 or game_box[i][j+3] != 0:
            if game_box[i][j+3] == 0:
                while game_box[i][j+3] == 0:
                    game_box[i][j+3] = game_box[i][j+2]
                    game_box[i][j+2] = game_box[i][j+1]
                    game_box[i][j+1] = game_box[i][j]
                    game_box[i][j] = 0

            if game_box[i][j+2] == 0 and (game_box[i][j+1] != 0 or
               game_box[i][j] != 0):
                while game_box[i][j+2] == 0:
                    game_box[i][j+2] = game_box[i][j+1]
                    game_box[i][j+1] = game_box[i][j]
                    game_box[i][j] = 0

            if game_box[i][j+1] == 0 and game_box[i][j] != 0:
                while game_box[i][j+1] == 0:
                    game_box[i][j+1] = game_box[i][j]
                    game_box[i][j] = 0

# After right movement function


def right_addition(game_box):
    j = 0
    global points
    for i in range(0, 4):
        if game_box[i][j+3] == game_box[i][j+2]:
            game_box[i][j+3] = game_box[i][j+3] + game_box[i][j+2]
            points += game_box[i][j+3] ** 2
            game_box[i][j+2] = game_box[i][j+1]
            game_box[i][j+1] = game_box[i][j]
            game_box[i][j] = 0

        if game_box[i][j+2] == game_box[i][j+1]:
            game_box[i][j+2] = game_box[i][j+2]+game_box[i][j+1]
            points += game_box[i][j+2] ** 2
            game_box[i][j+1] = game_box[i][j]
            game_box[i][j] = 0

        if game_box[i][j+1] == game_box[i][j]:
            game_box[i][j+1] = game_box[i][j+1]+game_box[i][j]
            points += game_box[i][j+1] ** 2
            game_box[i][j] = 0

while True:
    win.refresh()
    border()
    win.addstr(1, 1, ("Points>>>>>>"))
    win.addstr(2, 1, (str(points)))
    win.addstr(3, 1, ("Highscore:"))
    if int(highscore) > int(points):
        win.addstr(4, 1, (str(highscore)))
    else:
        win.addstr(4, 1, "                   ")
        win.addstr(4, 1, (str(points)))
        score = open("highscore.txt", "w+")
        score.write(str(points))
        score.close()
    win.addstr(1, 55, "Press BACKSPACE to exit")
    win.addstr(22, 71, "CODECOOL")

    win.addstr(3, 18, str("    ") + "\t\t" + str("    ") + "\t\t" +
               str("    ") + "\t\t" + str("    "))
    win.addstr(9, 18, str("    ") + "\t\t" + str("    ") + "\t\t" +
               str("    ") + "\t\t" + str("    "))
    win.addstr(15, 18, str("    ") + "\t\t" + str("    ") + "\t\t" +
               str("    ") + "\t\t" + str("    "))
    win.addstr(21, 18, str("    ") + "\t\t" + str("    ") + "\t\t" +
               str("    ") + "\t\t" + str("    "))

    win.addstr(3, 18, str(game_box[0][0]) + "\t\t" + str(game_box[0][1]) +
               "\t\t" + str(game_box[0][2]) + "\t\t" + str(game_box[0][3]))
    win.addstr(9, 18, str(game_box[1][0]) + "\t\t" + str(game_box[1][1]) +
               "\t\t" + str(game_box[1][2]) + "\t\t" + str(game_box[1][3]))
    win.addstr(15, 18, str(game_box[2][0]) + "\t\t" + str(game_box[2][1]) +
               "\t\t" + str(game_box[2][2]) + "\t\t" + str(game_box[2][3]))
    win.addstr(21, 18, str(game_box[3][0]) + "\t\t" + str(game_box[3][1]) +
               "\t\t" + str(game_box[3][2]) + "\t\t" + str(game_box[3][3]))

    action = screen.getch()
    if action == curses.KEY_UP:
        up_movement(game_box)
        up_addition(game_box)
    elif action == curses.KEY_DOWN:
        down_movement(game_box)
        down_addition(game_box)
    elif action == curses.KEY_LEFT:
        left_movement(game_box)
        left_addition(game_box)
    elif action == curses.KEY_RIGHT:
        right_movement(game_box)
        right_addition(game_box)
    elif action == curses.KEY_BACKSPACE:
        curses.endwin()
        exit()
    else:
        khopi_attempt += 1
        continue
    row_indexes_with_zero = []
    column_indexes_with_zero = []
    for i in range(0, 4):
        for j in range(0, 4):
            if game_box[i][j] == 0:
                row_indexes_with_zero.append(i)
                column_indexes_with_zero.append(j)
            if game_box[i][j] == 2048:
                win.addstr(
                 "Congratulations!! You've successfully sumed up a 2048 tile")
                break
    if len(row_indexes_with_zero) > 1:
        random_index = \
          row_indexes_with_zero.index(random.choice(row_indexes_with_zero))
        row_to_place_entry = row_indexes_with_zero[random_index]
        column_to_place_entry = column_indexes_with_zero[random_index]
        game_box[row_to_place_entry][column_to_place_entry] = 2
    elif len(row_indexes_with_zero) == 1:
        row_to_place_entry = row_indexes_with_zero[0]
        column_to_place_entry = column_indexes_with_zero[0]
        game_box[row_to_place_entry][column_to_place_entry] = 2


win.addstr("Congratulations!! You scored " + str(points) + "points")

curses.endwin()

# coding: UTF-8
"""
Script: dev/game_puissance4.py
Création: Yanis Legentil, le 04/02/2022
"""


# Imports
IS_WIN_PLAYER_1 = "xxxx"
IS_WIN_PLAYER_2 = "oooo"

PLAYER_SIGN = {
    1: "x",
    2: "o"
}


# Fonctions
def create_lines():
    lines = [
        ["•", "•", "•", "•", "•", "•", "•"],
        ["•", "•", "•", "•", "•", "•", "•"],
        ["•", "•", "•", "•", "•", "•", "•"],
        ["•", "•", "•", "•", "•", "•", "•"],
        ["•", "•", "•", "•", "•", "•", "•"],
        ["•", "•", "•", "•", "•", "•", "•"]
    ]
    return lines


def create_columns():
    columns = [0, 0, 0, 0, 0, 0, 0]
    return columns


def update_lines(line_number: int, player: int, lines: list, columns: list):
    new_lines = lines
    new_columns = columns
    if player == 1:
        new_lines[columns[line_number]][line_number] = PLAYER_SIGN[1]
        columns[line_number] += 1
    elif player == 2:
        new_lines[columns[line_number]][line_number] = PLAYER_SIGN[2]
        columns[line_number] += 1
    return new_lines, new_columns


def choix_jeu(joueur: int):
    choix = input(f"Dans quelle colonne voulez-vous jouer joueur {joueur} ? --> ")
    return int(choix) - 1


def print_lines(lines: list):
    for line in lines[::-1]:
        for i in range(6):
            print(line[i], end="")
        print(line[-1])


def jeu(lines: list, columns: list):
    for game in range(42):
        if game % 2 == 0:
            get_update = update_lines(choix_jeu(1), 1, lines, columns)
            lines = get_update[0]
            columns = get_update[1]
            print_lines(lines)
            if check_win(lines) == "player1_win":
                print("Bravo joueur 1, tu as gagné !")
                exit()
            elif check_win(lines) == "player2_win":
                print("Bravo joueur 2, tu as gagné !")
                exit()
        elif game % 2 != 0:
            get_update = update_lines(choix_jeu(2), 2, lines, columns)
            lines = get_update[0]
            columns = get_update[1]
            print_lines(lines)
            if check_win(lines) == "player1_win":
                print("Bravo joueur 1, tu as gagné !")
                exit()
            elif check_win(lines) == "player2_win":
                print("Bravo joueur 2, tu as gagné !")
                exit()


def check_win(lines: list):
    # H
    for line_h in range(len(lines)):
        for h in range(4):
            current_line_h = ""
            for i_h in range(4):
                current_line_h += lines[line_h][h + i_h]
            if current_line_h == IS_WIN_PLAYER_1:
                return "player1_win"
            elif current_line_h == IS_WIN_PLAYER_2:
                return "player2_win"
    # V
    for line_v in range(len(lines)):
        for v in range(3):
            current_line_v = ""
            for i_v in range(4):
                current_line_v += lines[v + i_v][line_v]
            if current_line_v == IS_WIN_PLAYER_1:
                return "player1_win"
            elif current_line_v == IS_WIN_PLAYER_2:
                return "player2_win"

    # D RIGHT
    for line_d_r in range(3):
        for d_r in range(4):
            current_line_d_r = ""
            for i_d_r in range(4):
                current_line_d_r += lines[i_d_r + line_d_r][i_d_r + d_r]
            if current_line_d_r == IS_WIN_PLAYER_1:
                return "player1_win"
            elif current_line_d_r == IS_WIN_PLAYER_2:
                return "player2_win"

    # D LEFT
    for line_d_l in range(3):
        count = 6
        for d_l in range(4):
            current_line_d_l = ""
            for i_d_l in range(4):
                current_line_d_l += lines[i_d_l + line_d_l][count]
                if i_d_l != 3:
                    count -= 1
            if current_line_d_l == IS_WIN_PLAYER_1:
                return "player1_win"
            elif current_line_d_l == IS_WIN_PLAYER_2:
                return "player2_win"
            count += 2


# Programme principal
def main():
    print(f"================================")
    print(f"Nouvelle partie de puissance 4 ! ")
    print(f"================================")
    lines = create_lines()
    columns = create_columns()
    print_lines(lines)
    jeu(lines, columns)


if __name__ == '__main__':
    main()
# Fin

# Создайте программу для игры в ""Крестики-нолики"".

def find (matrix, player):
    if (matrix[0] == player) and (matrix[1] == player) and (matrix[2] == player):
        print(f"Игрок {player} выйграл!")
        return 1
    elif (matrix[3] == player) and (matrix[4] == player) and (matrix[5] == player):
        print(f"Игрок {player} выйграл!")
        return 1
    elif (matrix[6] == player) and (matrix[7] == player) and (matrix[8] == player):
        print(f"Игрок {player} выйграл!")
        return 1
    elif (matrix[0] == player) and (matrix[3] == player) and (matrix[6] == player):
        print(f"Игрок {player} выйграл!")
        return 1
    elif (matrix[1] == player) and (matrix[4] == player) and (matrix[7] == player):
        print(f"Игрок {player} выйграл!")
        return 1
    elif (matrix[2] == player) and (matrix[5] == player) and (matrix[8] == player):
        print(f"Игрок {player} выйграл!")
        return 1
    elif (matrix[0] == player) and (matrix[4] == player) and (matrix[8] == player):
        print(f"Игрок {player} выйграл!")
        return 1
    elif (matrix[2] == player) and (matrix[4] == player) and (matrix[6] == player):
        print(f"Игрок {player} выйграл!")
        return 1
    else:
        return 0

def correct(matrix, player_one, player_two):
    number = int(input(f"Игрок {player_one}, введите номер ячейки: "))
    if (0 < number < 10) and (matrix[number - 1] != player_two) and (matrix[number - 1] != player_one):
        matrix[number - 1] = player_one
        print(matrix[0],matrix[1],matrix[2])
        print(matrix[3],matrix[4],matrix[5])
        print(matrix[6],matrix[7],matrix[8])
    else:
        print("Введено некорректное число")
        correct(matrix, player_one, player_two)


matrix = ["1","2","3","4","5","6","7","8","9"]

print(matrix[0],matrix[1],matrix[2])
print(matrix[3],matrix[4],matrix[5])
print(matrix[6],matrix[7],matrix[8])

k=0
while k != 9:
    player_first = "X"
    player_second = "0"

    correct(matrix, player_first, player_second)

    result_one = find(matrix, player_first)

    if result_one == 1:
        break

    k = k + 1
    if k == 9:
        print("Ничья!")
        break

    correct(matrix, player_second, player_first)

    result_two = find(matrix, player_second)

    if result_two == 1:
        break 
    
    k = k + 1
    if k == 9:
        print("Ничья!")
        break

import random


def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors. 'E/e' for Exit\n")

    if user == 'E' or user == 'e':
        return user

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"

    # r > s, s > p, p > r
    if is_win(user, computer):
        return "You won!"

    return "You lost!"


def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


i = 1
while i == 1:
    output = play()
    if output == 'e' or output == 'E':
        break
    else:
        print(output + '\n')

import random
import numpy as np
import csv
import sys

sys.setrecursionlimit(1500)

file = open('rps_track.csv', 'a', newline='')

# track_length = 4
#
# a_start = 0
# b_start = track_length + 1


def turn(a_pos, b_pos, num_turns, last_winner):

    if num_turns > 1450:
        return 'recursion_limit'

    # print('a starts round at: ', a_pos)
    # print('b starts round at: ', b_pos)
    if (b_pos - a_pos) % 2 == 0:

        if last_winner == 0:
            middle_space_winner = random.choice(['a', 'b'])
        else:
            middle_space_winner = last_winner
        # middle_space_winner = random.choice(['a', 'b'])
        middle_space = int(np.mean([a_pos, b_pos]))

        if middle_space_winner == 'a':
            # print('a wins middle space')
            a_fight_pos = middle_space
            b_fight_pos = middle_space + 1
        else:
            # print('b wins middle space')
            a_fight_pos = middle_space - 1
            b_fight_pos = middle_space

        # print('a fights at: ', a_fight_pos)
        # print('b fights at: ', b_fight_pos)
        winner = random.choice(['a', 'b'])

    else:
        a_fight_pos = int(np.mean([a_pos, b_pos]))
        b_fight_pos = a_fight_pos + 1
        # print('a fights at: ', a_fight_pos)
        # print('b fights at: ', b_fight_pos)
        winner = random.choice(['a', 'b'])
    # print('round winner: ', winner)
    if winner == 'a':
        if a_fight_pos == track_length:
            # return "a_wins", num_turns
            return num_turns
        else:
            b_new_pos = b_start
            a_new_pos = a_fight_pos
            return turn(a_new_pos, b_new_pos, num_turns + 1, 'a')
    elif winner == 'b':
        if b_fight_pos == 1:
            # return 'b_wins', num_turns
            return num_turns
        else:
            a_new_pos = a_start
            b_new_pos = b_fight_pos
            return turn(a_new_pos, b_new_pos, num_turns + 1, 'b')


# print(turn(a_start, b_start, 0))


with file:
    write = csv.writer(file)

    # overall_results = []

    for i in range(1, 65):
        print(i)
        track_length = i
        a_start = 0
        b_start = track_length + 1

        results = []
        for game in range(1, 1000):
            game_result = turn(a_start, b_start, 0, 0)
            if game_result == 'recursion_limit':
                print(game_result)
                results.append(1750)
            else:
                results.append(game_result)

        average_game = np.mean(results)

        write.writerow([i, average_game])

        # overall_results.append([i, average_game])

# with file:
#     write = csv.writer(file)
#     write.writerows(overall_results)

file.close()

sys.setrecursionlimit(1000)

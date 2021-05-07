import random
import statistics

scratch_order = [
    'full_house',
    'large_straight',
    'small_straight',
    '4_of_a_kind',
    '3_of_a_kind']


def sublist(l1, l2):
    flag = True
    for item in l1:
        if item in l2:
            pass
        else:
            flag = False
    return flag


def roll(roll_num, keep, current_score):

    if len(keep) == 5:
        return keep
    else:
        new_roll = [random.randint(1, 6) for x in range(5 - len(keep))]
        new_roll_modes = statistics.multimode(new_roll)

        if len(new_roll_modes) == 2:
            num_a = new_roll_modes[0]
            num_b = new_roll_modes[1]
            if current_score['nums'][num_a - 1] == 0:
                new_roll_mode = num_a
            elif current_score['nums'][num_b - 1] == 0:
                new_roll_mode = num_b
            else:
                new_roll_mode = max(new_roll_modes)
        else:
            new_roll_mode = statistics.mode(new_roll)

        new_roll_mode_count = new_roll.count(new_roll_mode)
        # print("roll: ", roll_num)
        # print("roll: ", new_roll)
        # # print(new_roll_mode)
        # print("keep: ", keep)

        if roll_num == 2:
            # print(sorted(keep + new_roll))
            return keep + new_roll

        else:
            if sorted(new_roll) == [1, 2, 3, 4, 5] or sorted(new_roll) == [2, 3, 4, 5, 6]:
                return new_roll

            if new_roll_mode_count > len(keep) and new_roll_mode_count > 1:
                keep = [new_roll_mode for x in range(new_roll_mode_count)]
            elif len(keep) > 0:
                if keep[1] in new_roll:
                    keep_1_count = new_roll.count(keep[1])
                    for i in range(keep_1_count):
                        keep.append(keep[1])

            roll_num += 1
            return roll(roll_num, keep, scores)


results = []

games = 10000

for game in range(games):

    scratches = 0

    scores = {
        "nums": [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        "upper_bonus": [0, 0],
        'full_house': [0, 0],
        "3_of_a_kind": [0, 0],
        "4_of_a_kind": [0, 0],
        "small_straight": [0, 0],
        "large_straight": [0, 0],
        "yahtzee": [0, 0],
        "chance": [0, 0]
        }

    for i in range(13):
        # print("********** turn **********")
        # print(i)
        turn = roll(0, [], scores)
        turn_mode = statistics.mode(turn)
        turn_mode_count = turn.count(turn_mode)
        if turn_mode_count == 5:
            # print('***** Yahtzee *****')
            if scores["yahtzee"][0] == 0 and scores["yahtzee"][1] != 1:
                scores["yahtzee"][0] = 50
            else:
                scores["yahtzee"][0] += 100
                if scores["nums"][turn_mode - 1][0] == 0 and scores["nums"][turn_mode - 1][1] != 1:
                    scores["nums"][turn_mode - 1][0] = turn_mode * turn_mode_count
                    # print('***** ', turn_mode_count, ' ', turn_mode, 's *****')
                elif scores['4_of_a_kind'][0] == 0 and scores['4_of_a_kind'][1] != 1:
                    scores['4_of_a_kind'][0] = turn_mode * turn_mode_count
                elif scores['3_of_a_kind'][0] == 0 and scores['3_of_a_kind'][1] != 1:
                    scores['3_of_a_kind'][0] = turn_mode * turn_mode_count
                elif scores['full_house'][0] == 0 and scores['full_house'][1] != 1:
                    scores['full_house'][0] = 25

        elif sorted(turn) == [1, 2, 3, 4, 5] or sorted(turn) == [2, 3, 4, 5, 6]:
            if scores["large_straight"][0] == 0 and scores["large_straight"][1] != 1:
                scores["large_straight"][0] = 40
                # print('***** Large Straight *****')
            elif scores["small_straight"][0] == 0 and scores["small_straight"][1] != 1:
                scores["small_straight"][0] = 30
                # print('***** Small Straight *****')

        elif sublist([1, 2, 3, 4], turn) or sublist([2, 3, 4, 5], turn) or sublist([3, 4, 5, 6], turn):
            if scores["small_straight"][0] == 0 and scores["small_straight"][1] != 1:
                scores["small_straight"][0] = 30
                # print('***** Small Straight *****')

        elif turn_mode_count > 2:
            if scores["nums"][turn_mode - 1][0] == 0 and scores["nums"][turn_mode - 1][1] != 1:
                scores["nums"][turn_mode - 1][0] = turn_mode * turn_mode_count
                # print('***** ', turn_mode_count, ' ', turn_mode, 's *****')
            elif turn_mode_count == 4:
                if scores['4_of_a_kind'][0] == 0 and scores['4_of_a_kind'][1] != 1:
                    scores['4_of_a_kind'][0] = sum(turn)
                    # print('***** 4_of_a_kind *****')
                elif scores['3_of_a_kind'][0] == 0 and scores['3_of_a_kind'][1] != 1:
                    scores['3_of_a_kind'][0] = sum(turn)
                    # print('***** 3_of_a_kind *****')
            elif scores['full_house'][0] == 0 and scores['full_house'][1] != 1:
                scores['full_house'][0] = 25
            elif scores["chance"][0] == 0 and scores["chance"][0] != 1:
                scores["chance"][0] = sum(turn)
                # print('***** chance *****')
            else:
                scratched = False
                while scratched == False:
                    # print(scratch_order[scratches])
                    if scores[scratch_order[scratches]][0] == 0 and scores[scratch_order[scratches]][1] == 0:
                        scores[scratch_order[scratches]][1] = 1
                        if scratches < 3:
                            scratches += 1
                        scratched = True
                    elif scratches < 3:
                        scratches += 1
                    else:
                        scratched = True

    game_total = 0
    top = sum([x[0] for x in scores['nums']])
    if top >= 63:
        scores["upper_bonus"][0] = 35

    # print(scores)

    score_raw = scores.copy()

    scores["nums"] = [top, 0]

    for key in scores.keys():
        game_total += scores[key][0]


    # print(game_total)

    results.append([game_total, score_raw])

    if game % 1000 == 0:
        print(game)

total_scores = [game[0] for game in results]

max_game = results[total_scores.index(max(total_scores))]
min_game = results[total_scores.index(min(total_scores))]
mean = statistics.mean(total_scores)
std_dev = statistics.stdev(total_scores)

print('mean: ', mean)
print('std_dev', std_dev)
print('max: ', max_game)
print('min: ', min_game)

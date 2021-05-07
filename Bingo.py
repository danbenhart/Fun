import numpy


def check(card):
    # check rows
    for i in range(0, 5):
        if card[i][0] == 'x' and card[i][1] == 'x' and card[i][2] == 'x' and card[i][3] == 'x' and card[i][4] == 'x':
            return 'winner'
    # check columns
    for i in range(0, 5):
        if card[0][i] == 'x' and card[1][i] == 'x' and card[2][i] == 'x' and card[3][i] == 'x' and card[4][i] == 'x':
            return 'winner'
    if card[0][0] == 'x' and card[1][1] == 'x' and card[2][2] == 'x' and card[3][3] == 'x' and card[4][4] == 'x':
        return 'winner'
    if card[4][0] == 'x' and card[3][1] == 'x' and card[2][2] == 'x' and card[1][3] == 'x' and card[0][4] == 'x':
        return 'winner'


num_cards = 10

results = []
for i in range(1000):
    remaining_spaces = list(range(1, 76))
# region generate cards
    all_cards = []
    for z in range(num_cards):
        b_col = list(range(1, 16))
        i_col = list(range(16, 31))
        n_col = list(range(31, 46))
        g_col = list(range(46, 61))
        o_col = list(range(61, 76))

        possible_cards = [b_col, i_col, n_col, g_col, o_col]
        blank_card = [[[], [], [], [], []],
                      [[], [], [], [], []],
                      [[], [], [], [], []],
                      [[], [], [], [], []],
                      [[], [], [], [], []]]

        for row in range(0, 5):
            for col in range(0, 5):
                choice = numpy.random.choice(possible_cards[col])
                blank_card[row][col] = choice
                possible_cards[col].remove(choice)

        blank_card[2][2] = 'x'
        all_cards.append(blank_card)
# endregion

    x = 0
    a = 1
    while a:
        x += 1
        pick = numpy.random.choice(remaining_spaces)
        # print(pick)
        remaining_spaces.remove(pick)
        for card in all_cards:
            for i in range(0, 5):
                if pick in card[i]:
                    index = card[i].index(pick)
                    card[i][index] = 'x'
            if check(card) == 'winner':
                a = 0
    # for sub in blank_card:
    #     print(sub)
    # print("")
    results.append(x)
print(sum(results)/len(results))
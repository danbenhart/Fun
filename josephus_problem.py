def next_death(index, remaining_players):
    # print(remaining_players)
    if len(remaining_players) == 1:
        print('winner: ' + str(remaining_players[0]))
        return 'winner: ' + str(remaining_players[0])
    else:
        if index == len(remaining_players) - 1:
            remaining_players.pop(0)
            index = 0
            next_death(index, remaining_players)
        elif index == len(remaining_players) - 2:
            remaining_players.pop(index + 1)
            index = 0
            next_death(index, remaining_players)
        else:
            remaining_players.pop(index + 1)
            index += 1
            next_death(index, remaining_players)


for i in range(1, 100):
    players = list(range(1, i+1))
    print("starting players: ", str(i))
    next_death(0, players)



# for i in range(1, 10):
#     players = list(range(1, i+1))
#     print("starting players: ", str(players))
#     current_index = 0
#     while len(players) > 1:
#         # print("current index: " + str(current_index))
#         print("remaining players: " + str(players))
#         if current_index == len(players)-1:
#             players.pop(0)
#             current_index = 0
#         else:
#             players.pop(current_index+1)
#             if current_index == len(players):
#                 current_index = 0
#             else:
#                 current_index += 1
#
#     print("winner: ", str(players[0]))

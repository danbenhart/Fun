tiles = {
    '_': [0, 2],
    'a': [1, 9],
    'b': [3, 2],
    'c': [3, 2],
    'd': [2, 4],
    'e': [1, 12],
    'f': [4, 2],
    'g': [2, 3],
    'h': [4, 2],
    'i': [1, 9],
    'j': [8, 1],
    'k': [5, 1],
    'l': [1, 4],
    'm': [3, 2],
    'n': [1, 6],
    'o': [1, 8],
    'p': [3, 2],
    'q': [10, 1],
    'r': [1, 6],
    's': [1, 4],
    't': [1, 6],
    'u': [1, 4],
    'v': [4, 2],
    'w': [4, 2],
    'x': [8, 1],
    'y': [4, 2],
    'z': [10, 1]
}


def word_value(test_word):
    value = 0
    tile_list = list(test_word)
    for tile in tile_list:
        value += tiles[tile][0]
    return value


def word_possible(test_word):
    tile_list = list(test_word)
    unique_tiles = set(tile_list)
    for char in unique_tiles:
        tile_count = tile_list.count(char)
        if tile_count > tiles[char][1]:
            return False
    return True


start_word = 'jqxz'
success = []

chars = '_abcdefghiklmnoprstuvwy'

target_value = 46

for first in range(23):
    first_new_char = chars[first]
    first_word = start_word + first_new_char
    # print(word)
    for second in range(23):
        second_new_char = chars[second]
        second_word = first_word + second_new_char
        if word_possible(second_word):
            if word_value(second_word) < target_value:
                for third in range(23):
                    third_new_char = chars[third]
                    third_word = second_word + third_new_char
                    if word_possible(third_word):
                        if word_value(third_word) == target_value:
                            sorted_word = ''.join(sorted(list(third_word)))
                            if sorted_word not in success:
                                success.append(sorted_word)
                            # for fourth in range(23):
                            #     fourth_new_char = chars[fourth]
                            #     fourth_word = third_word + fourth_new_char
                            #     if word_possible(fourth_word):
                            #         if word_value(fourth_word) == target_value:
                            #             sorted_word = ''.join(sorted(list(fourth_word)))
                            #             if sorted_word not in success:
                            #                 success.append(sorted_word)
    print(first)
print(len(success))

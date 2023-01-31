input_file = open(r'C:\Users\benhartd\PycharmProjects\Fun\english-words-master\words_alpha.txt', 'r')

input_words = []


def check_duplicates(word):
    chars = len(word)
    # print(chars)
    for i in range(1, chars):
        if word[i] == word[i - 1]:
            return False
    return True


for word in input_file.readlines():
    if len(word) >= 3:
        if check_duplicates(word):
            input_words.append(word)

input_file.close()

output_file = open(r'C:\Users\benhartd\PycharmProjects\Fun\english-words-master\words_alpha_deduped.txt', 'w')

for word in input_words:
    output_file.write(word)

output_file.close()
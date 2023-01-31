import networkx as nx
import progressbar
from datetime import datetime

widgets = [' [', progressbar.Timer(format='elapsed time: %(elapsed)s'), '] ', progressbar.Bar('*'),
           ' (', progressbar.AdaptiveETA(), ') ', ]

f = open(r'C:\Users\benhartd\PycharmProjects\Fun\english-words-master\words_alpha_deduped.txt', "r")
words = f.read().strip().split("\n")
words = [word.lower() for word in words if len(word) > 2]
f.close()

print(words[:10])


class Trie(object):

    def __init__(self, words=None):
        self.trie = dict()
        if words is not None:
            for word in words:
                self.add(word)

    def add(self, word):
        current_position = self.trie
        for c in word:
            if c not in current_position:
                current_position[c] = dict()
            current_position = current_position[c]
        current_position["done"] = True

    def query(self, word):
        current_position = self.trie
        for c in word:
            if c in current_position:
                current_position = current_position[c]
            else:
                return -1
        if "done" in current_position:
            return 1
        else:
            return 0


trie = Trie(words)


def do_search(current_face, current_word):

    for face in range(4):
        if face != current_face:
            for c in faces[face]:
                val = trie.query(current_word+c)
                if val == 1:
                    possible_words.append(current_word+c)
                    do_search(face, current_word+c)
                elif val == 0:
                    do_search(face, current_word+c)


faces = [
    ["u", "s", "y"],
    ["g", "a", "e"],
    ["v", "h", "l"],
    ["n", "i", "q"]
]

limit = 6

all_letters = set([letter for face in faces for letter in face])

possible_words = []
for i in range(4):
    for c in faces[i]:
        print("Searching for", c)
        do_search(i, c)

G = nx.DiGraph()

bar = progressbar.ProgressBar(max_value=len(possible_words)**2, widgets=widgets).start()

bar_val = 0
solutions = []

for u in possible_words:
    for v in possible_words:
        if u != v:
            if u[-1] == v[0]:
                G.add_edge(u, v)


today = datetime.today()
month = str(today.month)
day = str(today.day)
year = str(today.year)
output_file = open(r'C:\Users\benhartd\PycharmProjects\Fun\letter_boxed_results_'
                   + month + '-' + day + '-' + year + '.txt', 'w')

for u in possible_words:
    for v in possible_words:
        bar_val += 1
        bar.update(bar_val)
        if u != v:
            for path in nx.all_simple_paths(G, u, v, 3):
                if len(all_letters - set(''.join(path))) == 0:
                    if len(path) < limit:
                        solutions.append(path)
                        output_file.write(str(path)[1:-1])
                        output_file.write('\n')

output_file.close()

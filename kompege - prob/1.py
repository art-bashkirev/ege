from itertools import permutations

table = "12 16 21 24 27 34 35 36 42 43 47 53 57 61 63 72 74 75"
graph = "ac ae bd bg ca cf cg db de ea ed ef fc fe fg gc gf gb"

for p in permutations(set(graph.replace(" ", ""))):
    new_graph = table
    for i in range(1, 8):
        new_graph = new_graph.replace(str(i), p[i-1])
    if set(new_graph.split()) == set(graph.split()):
        print(*range(1, 8))
        print(*p)
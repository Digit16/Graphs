import sys
sys.setrecursionlimit(100000)

from graph import Graph
from fromFile import save_graph, graph_from_file


graph = graph_from_file("matrix.txt")
save_graph(graph, "matrix2.txt")



euler_cycle = graph.get_euler_cycle()

gen = graph.get_hamilton_cycles()
try:
    hamilton_cycle = next(gen)
except StopIteration:
    hamilton_cycle = None

print("Euler cycle:", euler_cycle)
print("Hamilton cycle:", hamilton_cycle)

# #  _______
# # /       \
# # 0 - 1 - 2
# # | \   / |
# # 3 - 4 - 5
# #



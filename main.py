import sys
sys.setrecursionlimit(100000)

from graph import *
from fromFile import *
import multiprocessing
import time


# graph = graph_from_file("matrix.txt")
# save_graph(graph, "matrix2.txt")


# cycle = graph.get_euler_cycle()

# print("-"*25)
# print(cycle)

# #  _______
# # /       \
# # 0 - 1 - 2
# # | \   / |
# # 3 - 4 - 5
# #



def foo(i,dens):
    while True:
        node_number = i
        density = dens

        ideal = int(node_number*(node_number-1) // 2 * density)

        while True:
            graph = get_random_eulerian_graph(node_number)
            edges = sum(len(e) for e in graph.edges.values()) // 2
            if (ideal - edges) % 2 != 0:
                continue
            if edges <= ideal:
                break

        if ideal != edges:
            graph = add_edges_to_graph(graph, ideal - edges)

        # for i in graph.edges.items():
        #     print(i)

        print("get_hamilton_cycles")
        gen = graph.get_hamilton_cycles()
        try:
            a = next(gen)
            print(a)
            save_graph(graph, f"./graphs/graph{node_number}_{str(density)}.txt")
            break
        except StopIteration as e:
            print("Graph doesn't have hamilton cycle")


from pathlib import Path

for i in range(10, 160, 10):
    while True:
        print(i)

        file = f"./graphs/graph{i}_{str(0.3)}.txt"
        try:
            with open(file) as f:
                pass
            break
        except:
            pass
            
        p = multiprocessing.Process(target=foo, name="foo", args=(i,0.3))
        p.start()

        p.join(300)



import pandas as pd

df = pd.DataFrame(["nodes", "density", "time_euler", "time_hamilton"])

for density in ["0.7", "0.3"]:
    for nodes in range(10, 160, 10):
        file = f"./graphs/graph{nodes}_{density}.txt"
        graph = graph_from_file(file)

        start = time.time()
        graph.get_euler_cycle()
        end = time.time()
        euler_time = end - start

        
        gen = graph.get_hamilton_cycles()
        start = time.time()
        a = next(gen)
        end = time.time()
        hamilton_time = end - start
        
        row = {
            "nodes": nodes,
            "density": density,
            "time_euler": euler_time,
            "time_hamilton": hamilton_time
        }
        df.append(row, ignore_index=True)

df.to_csv("graphs_time.csv")




# graph = graph_from_file("graphs/graph10_0.7.txt")

# # from drawing import draw_graph
# # draw_graph(graph)
# gen = graph.get_hamilton_cycles()
# a = next(gen)

# [2, 9, 0, 1, 3, 5, 4, 6, 8, 7, 2\


# print("DONE")
# print("-"*25)
# print(a)

# draw_graph(graph)
# DONE
# -------------------------
# [11, 2, 0, 1, 10, 6, 4, 12, 8, 14, 5, 13, 7, 9, 3, 11]


# (2, {3, 6})
# (3, {8, 2, 4, 7})
# (4, {1, 3, 5, 9})
# (1, {4, 7})
# (9, {8, 4})
# (8, {9, 3})
# (6, {2, 5})
# (7, {1, 3})
# (5, {4, 6})
from graph import *
from fromFile import *
import multiprocessing
import time


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

for i in list(range(7, 25, 1)):
    while True:
        print(i)

        file = f"./graphs/graph{i}_{str(0.5)}.txt"

        p = multiprocessing.Process(target=foo, name="foo", args=(i,0.5))
        p.start()
        p.join(300)

        try:
            with open(file) as f:
                pass
            break
        except:
            pass
            
print("DONE "*20)

import pandas as pd


rows = []
for density in ["0.5"]:
    for nodes in list(range(7, 160, 1)):
        print(nodes)
        file = f"./graphs/graph{nodes}_{density}.txt"
        graph = graph_from_file(file)

        start = time.time()
        gen = graph.get_hamilton_cycles()
        a = 0
        for i in gen:
            a += 1
            print(nodes, a)
        end = time.time()
        hamilton_time = end - start
        
        row = {
            "nodes": nodes,
            "density": density,
            "time_hamilton": hamilton_time,
            "count": a
        }
        rows.append(row)

        pd.DataFrame(rows).to_csv("graphs_time.csv")


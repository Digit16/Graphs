import networkx
import os
import matplotlib.pyplot as plt
os.environ['MPLCONFIGDIR'] = '/Matplotlib/'
               
        
def draw_graph(graph):
    g = networkx.Graph()

    for a, edges in graph.edges.items():
        g.add_node(a)
        for b in edges:
            g.add_edge(a,b, color="black", weight=2)

    edges = g.edges()
    colors = [g[u][v]["color"] for u, v in edges]
    weights = [g[u][v]["weight"] for u, v in edges]


    networkx.draw_spring(g, edge_color=colors, width=list(weights), with_labels=True, node_color="orange")


    plt.tight_layout()
    plt.show()
    plt.savefig("Graph.png", format="PNG")

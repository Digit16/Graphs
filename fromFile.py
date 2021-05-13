from graph import Graph

def graph_from_file(file):
    with open(file, "r") as f:
        content = f.read()

    lines = content.split("\n")

    for i in range(len(lines)):
        lines[i] = lines[i].split()


    g = Graph()

    for i, line in enumerate(lines):
        for j, digit in enumerate(line):
            if digit == "1":
                g.add_edge(i, j)

    return g

def save_graph(graph, file):
    lines = []
    keys = sorted(list(graph.edges.keys()))
    for _, e in sorted(graph.edges.items()):
        line = []
        for key in keys:
            line.append("1" if key in e else "0")
        lines.append(" ".join(line))
    text = "\n".join(lines)
    with open(file, "w") as f:
        f.write(text)

from collections import defaultdict
import random

class Graph:
    
    def __init__(self):
        self.edges = defaultdict(set)
        
    def add_edge(self, a, b):
        self.edges[a].add(b)
        self.edges[b].add(a)
        
    def remove_edge(self, a, b):
        self.edges[a].remove(b)
        self.edges[b].remove(a)

    def travel(self, a, v=None):
        if v == None:
            v = defaultdict(lambda: False)
        v[a] = True
        count = 1
        for e in self.edges[a]:
            if v[e] == False:
                count += self.travel(e, v)
        return count
        
    def is_valid_edge(self, a, b):
        if len(self.edges[a]) == 1:
            return True
        
        c1 = self.travel(a)
        self.remove_edge(a, b)
        c2 = self.travel(a)
        self.add_edge(a, b)
        
        return c1 == c2
    
    def get_euler_cycle(self, head=None):
        if head == None:
            head = list(self.edges.keys())[-1]
        path = [head]
        
        for e in list(self.edges[head]):
            if self.is_valid_edge(head, e):
                self.remove_edge(head, e)
                path.extend(self.get_euler_cycle(e))
                self.add_edge(head, e)
                break
        return path

    def get_hamilton_cycles(self, head=None, visited=None, path=None):
        path = path or []
        visited = visited or defaultdict(lambda: False)
        head = list(self.edges.keys())[-1] if head == None else head

        visited[head] = True
        path.append(head)
        for e in list(self.edges[head]):
            if visited[e] == False:
                yield from self.get_hamilton_cycles(e, visited, path)
            elif len(path) == len(self.edges) and path[0] == e:
                yield path + [path[0]]

        visited[head] = False
        path.pop()


def get_random_eulerian_graph(nodes):
    graph = Graph()
    nodes = list(range(nodes))
    r1 = random.choice(nodes)
    r2 = random.choice(list(set(nodes) - set([r1])))
    graph.add_edge(r1, r2)

    while len(connected := [n for n, e in graph.edges.items() if len(e)]) != len(nodes):
        rand_connected = random.choice([c for c in connected if len(graph.edges[c]) != (len(nodes)-1) >> 1 << 1])
        random_alone = random.choice(list(set(nodes) - set(connected)))
        graph.add_edge(rand_connected, random_alone)

    odd_edged = [n for n, e in graph.edges.items() if len(e) % 2]

    while len(odd_edged):
        first = odd_edged[0]
        other = odd_edged[1:]
        random.shuffle(other)

        for o in other:
            if o not in graph.edges[first]:
                graph.add_edge(o, first)
                odd_edged.remove(o)
                break
        odd_edged.remove(first)

    odd_edged = [n for n, e in graph.edges.items() if len(e) % 2]

    while len(odd_edged):
        first = odd_edged[0]
        other = odd_edged[1:]
        random.shuffle(other)

        for o in other:
            random_alone = random.choice(list(set(nodes) - (graph.edges[first] | graph.edges[o])))
            graph.add_edge(first, random_alone)
            graph.add_edge(o, random_alone)
            odd_edged.remove(o)
            break
        odd_edged.remove(first)
    return graph

# def add_edges_to_graph(graph, edges):
#     nodes = [n for n, e in graph.edges.items() if len(e) != len(graph.edges.keys())-1]
#     random.shuffle(nodes)
#     if edges == 0:
#         return graph
    
#     for node in nodes[1:]:
#         if node not in graph.edges[nodes[0]]:
#             graph.add_edge(node, nodes[0])
#             val = add_edges_to_graph(graph, edges-1)
#             if val != None:
#                 return val
#             print("going back")
                
#             graph.remove_edge(node, nodes[0])
            
#     return None

def add_edges_to_graph(graph, edges):
    keys = graph.edges.keys()
    nodes = [n for n, e in graph.edges.items() if not ((len(e) == (len(keys)-1) and len(keys)%2))]
    random.shuffle(nodes)
    odd_nodes = [n for n in nodes if len(graph.edges[n]) % 2]
    

    if edges == 0 and len(odd_nodes) == 0:
        return graph


    if edges == 1 and len(odd_nodes) == 2 and (odd_nodes[0] not in graph.edges[odd_nodes[1]]):
        graph.add_edge(odd_nodes[0], odd_nodes[1])
        return graph

    if edges > 1:
        if len(odd_nodes) > 0:
            first = odd_nodes[0]
        else:
            first = nodes[0]

        other_nodes = list(set(nodes) - set([first]))
        random.shuffle(other_nodes)
        for node in other_nodes:
            if node not in graph.edges[first]:
                graph.add_edge(node, first)
                val = add_edges_to_graph(graph, edges-1)
                if val != None:
                    return val
                
                graph.remove_edge(node, first)

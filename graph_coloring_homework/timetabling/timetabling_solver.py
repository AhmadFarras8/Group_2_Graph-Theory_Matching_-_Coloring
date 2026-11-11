# Part 2: Timetabling Problem Using Welsh-Powell Graph Coloring
import networkx as nx
import matplotlib.pyplot as plt
import os

def load_graph_from_file(filename):
    graph = {}
    with open(filename, 'r') as f:
        for line in f:
            if ':' in line:
                parts = line.split(':')
                node = parts[0].strip()
                neighbors = [n.strip() for n in parts[1].split(',') if n.strip()]
                graph[node] = neighbors
    return graph

def welsh_powell_coloring(graph):
    degrees = {v: len(neighbors) for v, neighbors in graph.items()}
    sorted_vertices = sorted(degrees, key=degrees.get, reverse=True)
    
    coloring = {}
    current_color = 0
    uncolored = set(sorted_vertices)
    
    while uncolored:
        current_color += 1
        colored_in_pass = set()
        for v in sorted_vertices:
            if v in uncolored:
                if not any(neighbor in colored_in_pass for neighbor in graph[v]):
                    coloring[v] = current_color
                    colored_in_pass.add(v)
        uncolored -= colored_in_pass
        
    return coloring

def visualize_timetabling(graph, coloring, title):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for n in neighbors:
            G.add_edge(node, n)
            
    plt.figure(figsize=(7, 5))
    pos = nx.spring_layout(G, seed=42)
    color_map = [coloring.get(node, 1) for node in G.nodes()]
    
    nx.draw(G, pos, with_labels=True, node_color=color_map, cmap=plt.cm.Set2, 
            node_size=2200, font_size=10, font_weight='bold', edge_color='gray', width=2)
    plt.title(title, fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig('timetabling_coloring.png')
    print("Timetabling visualization saved as 'timetabling_coloring.png'")
    plt.show()

if __name__ == "__main__":
    timetabling_file = 'input_timetabling.txt'
    if os.path.exists(timetabling_file):
        graph = load_graph_from_file(timetabling_file)
        print(f"Loaded Timetabling graph from {timetabling_file}")
    else:
        print("Input file not found. Using default conflict graph.")
        graph = {
            'Math 101': ['Physics 101', 'CS 101'],
            'Physics 101': ['Math 101', 'CS 101', 'Chemistry 101'],
            'CS 101': ['Math 101', 'Physics 101'],
            'Chemistry 101': ['Physics 101', 'English 101'],
            'English 101': ['Chemistry 101']
        }

    assigned_slots = welsh_powell_coloring(graph)
    print("\nTimetabling Slot Assignments (Colors = Time Slots):")
    for course, slot in assigned_slots.items():
        print(f"  {course} -> Time Slot {slot}")

    visualize_timetabling(graph, assigned_slots, "Timetabling Conflict Graph Coloring")
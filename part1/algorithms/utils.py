import pandas as pd
from math import inf

def h(node, heuristic):
    """Returns the heuristic value for a node."""
    return heuristic.get(node, float('inf'))  # Default to infinity if not found

def neighbors(node, graph):
    """Returns the neighbors of a given node from the graph."""
    return graph.get(node, [])

# Hàm tính chi phí từ node hiện tại đến các láng giềng
def cost(current, neighbor, graph):
    for neighbor_node, edge_cost in graph[current]:
        if neighbor_node == neighbor:
            return edge_cost
    return inf  # Nếu không có cạnh, trả về vô cùng


def reconstruct_path(came_from, current):
    """Reconstruct the path from start to goal using the came_from dictionary."""
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()  # Reverse to get the path from start to goal
    return path

def print_table(graph, heuristic, open_set):
    """Prints the current state of the open set."""
    data = []
    for _, node in open_set.queue:  # `queue` is the internal list of the PriorityQueue
        # Get neighbors and heuristic for each node in open_set
        node_neighbors = ', '.join([neighbor for neighbor, _ in graph.get(node, [])])
        node_heuristic = ', '.join([f"{neighbor}:{h(neighbor, heuristic)}" for neighbor, _ in graph.get(node, [])])
        data.append([node, node_neighbors, node_heuristic])
    
    # Create DataFrame and print the table
    df = pd.DataFrame(data, columns=['u', 'Neighbour of u', 'L'])
    print(df.to_string(index=False))  # Print the table without index

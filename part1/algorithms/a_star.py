import heapq
from math import inf
from algorithms.utils import h, neighbors, reconstruct_path, print_table


def cost(node1, node2, graph):
    """Calculate the cost of moving from node1 to node2 in the graph."""
    for neighbor, weight in graph[node1]:
        if neighbor == node2:
            return weight
    return float('inf')  # If nodes are not connected


def a_star(graph, heuristic, start, goal):
    """Implement A* search algorithm."""
    # Priority Queue to store the nodes to be explored, ordered by f(n) = g(n) + h(n)
    open_set = []
    heapq.heappush(open_set, (0 + h(start, heuristic), start))  # (f(n), node)
    
    # Dictionaries to store the cost from the start node to each node (g(n)) and the node's predecessor
    g_score = {node: inf for node in graph}
    g_score[start] = 0
    came_from = {}

    while open_set:
        # Get the node with the lowest f(n) value
        current_f, current_node = heapq.heappop(open_set)

        # Print current node being processed
        print(f"\n================================================")
        print(f"\nNode đang xét: {current_node}")
        
        # Print neighbors of current node with their scores
        neighbors_list = neighbors(current_node, graph)
        
        neighbor_data = []
        for neighbor, _ in neighbors_list:
            # Calculate the g-score for this neighbor
            neighbor_g = g_score[current_node] + cost(current_node, neighbor, graph)
            # Calculate the f-score for this neighbor
            neighbor_f = neighbor_g + h(neighbor, heuristic)
            # Add tuple (g(B), 'B', f(B)) to the list
            neighbor_data.append((neighbor_g, neighbor, neighbor_f))
        print(f"Neighbors của {current_node}: {neighbor_data}")
        
        # Print current open_set
        print("Danh sách L: ")
        if open_set:
            sorted_open = sorted(open_set, key=lambda x: x[0])
            for f_val, node in sorted_open:
                # Print the node and its f(n) and its g(n) value
                g_val = g_score[node]
                print(f"  - Đỉnh: {node}, g(n): {g_val}, f(n): {f_val}")
        else:
            print("[Empty]")
        
        # If we reached the goal, reconstruct the path and return it
        if current_node == goal:
            print(f"\nGoal reached: {goal}")
            return reconstruct_path(came_from, current_node)
        
        # Explore neighbors
        for neighbor, _ in neighbors_list:
            tentative_g_score = g_score[current_node] + cost(current_node, neighbor, graph)
            
            if tentative_g_score < g_score[neighbor]:
                # Update the came_from and g_score for this neighbor
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                
                # Add the neighbor to the open set with the updated f(n)
                f_score = tentative_g_score + h(neighbor, heuristic)
                heapq.heappush(open_set, (f_score, neighbor))
                print(f"Neighbor của {current_node}: {neighbor}   g(n)={tentative_g_score}, h(n)={h(neighbor, heuristic)}, f(n)={f_score}")

    # If the goal is unreachable, return an empty list
    print("\nGoal is unreachable!")
    return []
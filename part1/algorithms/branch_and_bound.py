import heapq
from math import inf
from collections import defaultdict
from algorithms.utils import h, cost, reconstruct_path

def branch_and_bound(graph, heuristic, start, goal):
    """Implement Branch and Bound search algorithm."""
    open_set = []  # This will act as a stack
    open_set.append((h(start, heuristic), start))  # (f(n), node)

    came_from = {}  # To reconstruct the path
    g_score = defaultdict(lambda: inf)  # Cost from start to node
    g_score[start] = 0

    best_cost = inf  # Store the best cost found so far
    best_path = None

    while open_set:
        # Pop the last node added to the stack
        current_f, current_node = open_set.pop()  # Remove the last inserted node (like a stack)
        current_cost = g_score[current_node]

        # Print current node being processed
        print(f"\n================================================")
        print(f"Node đang xét: {current_node}")
        
        # Print neighbors of current node with their scores
        neighbors_list = graph.get(current_node, [])
        
        neighbor_data = []
        for neighbor, _ in neighbors_list:
            neighbor_g = g_score[current_node] + cost(current_node, neighbor, graph)
            neighbor_f = neighbor_g + h(neighbor, heuristic)
            neighbor_data.append((neighbor_g, neighbor, neighbor_f))
        
        print(f"Neighbors của {current_node}: {neighbor_data}")
        
        # If we reached the goal, update best path if better
        if current_node == goal:
            if current_cost < best_cost:
                best_cost = current_cost
                best_path = reconstruct_path(came_from, current_node)
                
            print(f"\nGoal reached: {goal}, with cost {current_cost}")
            # Don't return yet - continue exploring for a better path

        # Sort neighbors by f(n) - highest f(n) first so lowest is popped last
        neighbor_data.sort(key=lambda x: x[2], reverse=True)

        # Explore neighbors
        for neighbor_g, neighbor, neighbor_f in neighbor_data:
            tentative_g_score = g_score[current_node] + cost(current_node, neighbor, graph)
            
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                open_set.append((neighbor_f, neighbor))
                print(f"Neighbor của {current_node}: {neighbor}   g(n)={tentative_g_score}, h(n)={h(neighbor, heuristic)}, f(n)={neighbor_f}")

    # Return the best path found
    if best_path:
        print(f"\nBest path found with cost {best_cost}")
        return best_path
    else:
        print("\nGoal is unreachable!")
        return []

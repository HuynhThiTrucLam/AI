from algorithms.utils import h, neighbors, reconstruct_path

def hill_climbing(graph, heuristic, start, goal):
    current = start
    came_from = {}  # Dictionary to reconstruct the path
    L = []  # List to store neighbors (stack)
    visited = set([current])  # Start by marking the initial node as visited

    while True:
        print(f"\nNode đang xét: {current}")  # Debugging: Show current node being processed
        
        # Find neighbors of the current node and include heuristic value in the output
        neighbors_with_heuristics = [(neighbor, h(neighbor, heuristic)) 
                                     for neighbor, _ in neighbors(current, graph) 
                                     if neighbor not in visited]

        # Print neighbors with their heuristic values
        print(f"Neighbors của {current}: {neighbors_with_heuristics}")
        
        if not neighbors_with_heuristics:
            print("❌ Không còn láng giềng để tiếp tục, kết thúc.")
            return None
        
        # Sort neighbors by their heuristic values in descending order
        neighbors_with_heuristics.sort(key=lambda x: x[1], reverse=True)  # Sort neighbors by heuristic value (desc)

        # Add sorted neighbors into the stack L (push at the end)
        for neighbor, _ in neighbors_with_heuristics:
            L.append(neighbor)
        
        # Print the stack L
        print(f"Danh sách L: {L}")
        
        # If L is not empty, take the last element (pop from the stack)
        best_neighbor = L.pop()  # Take the last element of the stack

        print(f"Neighbor tốt nhất được chọn: {best_neighbor} với heuristic h({best_neighbor}) = {h(best_neighbor, heuristic)}")
        
        # If the best neighbor is the goal, we found the solution
        if best_neighbor == goal:
            came_from[best_neighbor] = current
            return reconstruct_path(came_from, best_neighbor)
        
        # Move to the best neighbor
        visited.add(best_neighbor)  # Mark the best neighbor as visited
        came_from[best_neighbor] = current
        current = best_neighbor

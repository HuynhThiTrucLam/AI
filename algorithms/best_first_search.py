from queue import PriorityQueue
from algorithms.utils import h, neighbors, reconstruct_path, print_table

def best_first_search(graph, heuristic, start, goal):
    open_set = PriorityQueue() 
    open_set.put((h(start, heuristic), start)) 
    came_from = {}  

    while not open_set.empty():
        _, current = open_set.get()  # Mặc dù khi PriorityQueue get thì sẽ lấy min item nhưng khi in thì sẽ không in đúng thứ tự đã được sắp xếp
        
        print(f"\n=============================")
        print(f"Node đang xét: {current}")  
        
        # Sắp xếp lại open_set để in đúng thứ tự từ thấp đến cao
        open_set_list = sorted(open_set.queue, key=lambda x: x[0])  
        print(f"Danh sách L: {open_set_list}")  # Print the list with heuristic values
        
        # Find neighbors and print each neighbor with its heuristic value
        neighbors_with_heuristics = [(neighbor, h(neighbor, heuristic)) for neighbor, _ in neighbors(current, graph)]
        print(f"Neighbors của {current}: {neighbors_with_heuristics}")  # In neighbors with heuristic values

        if current == goal:
            return reconstruct_path(came_from, current)  # Return the reconstructed path to the goal
        
        for neighbor, _ in neighbors(current, graph):
            if neighbor not in came_from:
                came_from[neighbor] = current  # Mark the current node as the predecessor of the neighbor
                open_set.put((h(neighbor, heuristic), neighbor))  # Add neighbor to the open_set

    return None  # If no path is found

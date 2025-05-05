from queue import PriorityQueue
from collections import defaultdict
from algorithms.utils import h, neighbors, reconstruct_path


def AStar(start, goal, graph, heuristic):
    open_set = PriorityQueue()  # Tập các đỉnh cần xét
    open_set.put((h(start, heuristic), start))  # Thêm node start vào open_set với f(start)
    
    came_from = {}  # Để lưu lại lộ trình
    g_score = defaultdict(lambda: inf)  # Chi phí thực từ start đến node
    g_score[start] = 0  # Gán chi phí từ start đến chính nó là 0
    
    f_score = defaultdict(lambda: inf)  # f(n) = g(n) + h(n)
    f_score[start] = h(start, heuristic)  # Tính f(start)

    while not open_set.empty():
        _, current = open_set.get()  # Lấy node có f(n) thấp nhất
        
        if current == goal:
            return reconstruct_path(came_from, current)  # Nếu đã đến đích, trả về đường đi

        for neighbor in neighbors(current, graph):
            tentative_g = g_score[current] + cost(current, neighbor, graph)  # Tính chi phí tạm thời

            if tentative_g < g_score[neighbor]:  # Nếu tìm được đường tốt hơn
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + h(neighbor, heuristic)  # Cập nhật f(n)

                if neighbor not in [i[1] for i in open_set.queue]:  # Nếu chưa có trong open_set
                    open_set.put((f_score[neighbor], neighbor))  # Thêm vào open_set với f(n)
    
    return None  # Nếu không tìm được đường đi
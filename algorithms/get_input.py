def get_input():
    n = int(input("Nhập số lượng đỉnh: "))
    
    # Input the list of nodes
    nodes = []
    print("==== Nhập danh sách các đỉnh ====")
    for i in range(n):
        node = input(f"Nhập đỉnh {i + 1}: ").strip().upper()  # Convert to uppercase
        nodes.append(node)

    # Input the edges and costs between nodes
    graph = {node: [] for node in nodes}
    print("=== Nhập danh sách các cạnh (dạng: đỉnh1 đỉnh2 chi_phí), kết thúc bằng 'done' ===")
    while True:
        line = input().strip()
        if line.lower() == 'done':
            break
        u, v, cost = line.split()
        cost = int(cost)
        u, v = u.upper(), v.upper()  # Ensure case consistency for node names
        if u in graph and v in graph:
            graph[u].append((v, cost))  # Add directed edge from u to v

    # Input heuristic values for nodes
    heuristic = {}
    print("=== Nhập heuristic h(n) cho mỗi đỉnh (dạng: đỉnh giá_trị), kết thúc bằng 'done' ===")
    while True:
        line = input().strip()
        if line.lower() == 'done':
            break
        node, h_value = line.split()
        node = node.upper()  # Ensure case consistency
        if node in heuristic:
            print(f"Cảnh báo: Heuristic cho đỉnh {node} đã được định nghĩa. Bỏ qua mục này")
        else:
            heuristic[node] = int(h_value)

    # Input start and goal nodes
    start = input("=== Nhập đỉnh bắt đầu (start): ").strip().upper()
    goal = input("=== Nhập đỉnh kết thúc (goal): ").strip().upper()

    # Validate that start and goal exist in the nodes
    if start not in nodes or goal not in nodes:
        print("Lỗi: Đỉnh bắt đầu hoặc đỉnh kết thúc không hợp lệ!")
        return None, None, None, None

    return graph, heuristic, start, goal
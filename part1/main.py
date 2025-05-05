# main.py

from algorithms.get_input import get_input
from algorithms.best_first_search import best_first_search
from algorithms.hill_climbing import hill_climbing

def choose_algorithm():
    """Display algorithm options and get user input."""
    print("\n=========================== Chọn Thuật Toán ===========================")
    print("1. Best First Search")
    print("2. Hill Climbing")
    print("3. A* Search (Chưa triển khai)")
    print("4. Branch and Bound (Chưa triển khai)")
    print("5. Thoát chương trình")
    print("=======================================================================")

    # Handle user input and choice validation
    try:
        choice = int(input("Nhập số tương ứng với thuật toán bạn muốn chọn: "))
        if choice == 1:
            return best_first_search
        elif choice == 2:
            return hill_climbing
        elif choice == 5:
            return None  # Return None to exit the program
        else:
            print("⚠️ Lựa chọn này chưa được triển khai. Vui lòng chọn lại.")
            return None
    except ValueError:
        print("❌ Vui lòng nhập một số hợp lệ.")
        return None

def display_path(path):
    """Display the path found by the algorithm."""
    if path:
        print("\n🚶‍♂️ Đường đi tìm được:")
        print(" -> ".join(path))
    else:
        print("\n❌ Không tìm được đường đi.")

def main():
    # Get input data only once at the start
    graph, heuristic, start, goal = get_input()

    if not graph or not heuristic:  # Check if input data is valid
        print("⚠️ Dữ liệu đầu vào không hợp lệ. Vui lòng thử lại.")
        return

    print(f"\n🚀 Đang thực hiện tìm đường từ {start} đến {goal}...")

    while True:
        # Choose the algorithm to use
        algorithm = choose_algorithm()

        if algorithm:
            # Perform the selected algorithm
            path = algorithm(graph, heuristic, start, goal)

            # Output the result
            display_path(path)
        else:
            print("💤 Kết thúc chương trình.")
            break  # Exit the loop and end the program

if __name__ == "__main__":
    main()

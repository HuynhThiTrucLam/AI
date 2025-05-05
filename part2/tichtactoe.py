import random

# Khởi tạo bàn cờ 3x3
board = [[' ' for _ in range(3)] for _ in range(3)]

# Hàm kiểm tra nếu một người chơi thắng
def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

# Hàm kiểm tra xem người chơi X có thể thắng trong lượt tiếp theo không
def check_if_x_can_win(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                if check_winner(board) == 'X':
                    board[i][j] = ' '  # Hoàn tác
                    return (i, j)
                board[i][j] = ' '  # Hoàn tác
    return None

# Hàm đánh giá (Minimax)
def expectiminimax(board, depth, isMaximizingPlayer):
    winner = check_winner(board)
    if winner == 'O':  # AI thắng
        return 10 - depth
    elif winner == 'X':  # Người chơi thắng
        return 10 + depth
    elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):  # Hòa
        return 0

    if isMaximizingPlayer:  # Lượt của AI (O)
        bestScore = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = expectiminimax(board, depth + 1, False)
                    board[i][j] = ' '  # Hoàn tác nước đi
                    bestScore = max(score, bestScore)
        return bestScore
    else:  # Lượt của người chơi (X)
        bestScore = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = expectiminimax(board, depth + 1, True)
                    board[i][j] = ' '  # Hoàn tác nước đi
                    bestScore = min(score, bestScore)
        return bestScore

# Hàm tìm nước đi tốt nhất cho AI
def find_best_move(board):
    # Kiểm tra nếu X có thể thắng, nếu có, AI sẽ ngăn chặn ngay lập tức
    x_win_move = check_if_x_can_win(board)
    if x_win_move:
        return x_win_move

    # Nếu không có ai thắng, AI sẽ tìm kiếm nước đi tốt nhất cho mình
    bestScore = -float('inf')
    bestMove = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = expectiminimax(board, 0, False)
                board[i][j] = ' '  # Hoàn tác nước đi
                if score > bestScore:
                    bestScore = score
                    bestMove = (i, j)
    return bestMove

# Hàm in bàn cờ
def print_board(board):
    print("\n")
    print("Bàn cờ:")
    print("==============================")
    for i in range(3):
        print(" | ".join(board[i]))  # In từng hàng với dấu '|' phân cách
        if i < 2:  # Chỉ in dòng ngang giữa các hàng nếu không phải hàng cuối
            print("---------")
    print("==============================")
    print("\n")

# Chơi trò chơi
def play_game():
    while True:
        # In bàn cờ trước mỗi lượt đi
        print_board(board)

        # Người chơi X (ngẫu nhiên)
        row, col = random.choice([(i, j) for i in range(3) for j in range(3) if board[i][j] == ' '])
        board[row][col] = 'X'
        print(f"Người chơi X đánh vào ({row}, {col})")

        if check_winner(board) == 'X':
            print_board(board)
            print("Người chơi X thắng!")
            break

        # AI chơi O
        best_move = find_best_move(board)
        if best_move:
            row, col = best_move
            board[row][col] = 'O'
            print(f"AI đánh vào ({row}, {col})")

        if check_winner(board) == 'O':
            print_board(board)
            print("AI thắng!")
            break

        if all(board[i][j] != ' ' for i in range(3) for j in range(3)):  # Hòa
            print_board(board)
            print("Hòa!")
            break

# Chạy trò chơi
play_game()
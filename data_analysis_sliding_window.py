from collections import deque

def calculate_moving_average(data, window_size):
    """スライディングウィンドウを用いて移動平均を計算する (O(N))"""
    result = []
    window = deque()
    current_sum = 0.0

    for i, value in enumerate(data):
        # 1. 新しい値を窓に追加
        window.append(value)
        current_sum += value

        # 2. 窓のサイズを超えたら、一番古い値を捨てる
        if len(window) > window_size:
            old_value = window.popleft()
            current_sum -= old_value

        # 3. 窓が一杯になったら平均値を記録
        if len(window) == window_size:
            result.append(current_sum / window_size)
    
    return result

if __name__ == '__main__':
    # テストデータ：30日分の売上
    sales_data = [100, 120, 110, 150, 130, 140, 160, 150, 170, 180, 
                  160, 150, 140, 130, 120, 110, 100, 90, 110, 120,
                  130, 140, 150, 160, 170, 180, 190, 200, 210, 220]
    
    window_size = 7
    averages = calculate_moving_average(sales_data, window_size)

    print(f"データ数: {len(sales_data)}, 窓サイズ: {window_size}")
    print(f"移動平均の数: {len(averages)}")
    print(f"最初の5つの移動平均: {[round(a, 2) for a in averages[:5]]}")
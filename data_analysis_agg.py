import time
import random

def count_with_dict(data):
    """辞書（ハッシュマップ）を使った集計 (O(N))"""
    counts = {}
    for item in data:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

# from collections import Counter
# counts = Counter(order_logs) # これだけで O(N) の集計が完了


if __name__ == '__main__':
    # 1. 膨大なテストデータの生成 (100万件の注文)
    # 1000種類の商品IDがランダムに並んでいると仮定
    order_logs = [random.randint(1, 1000) for _ in range(1000000)]

    # 2. 計測
    start = time.time()
    result = count_with_dict(order_logs)
    end = time.time()

    print(f"100万件の集計時間: {end - start:.4f} 秒")
    
    # 3. 集計結果の確認（一部）
    # 商品ID '1' の注文数を表示
    print(f"商品ID 1 の注文数: {result.get(1, 0)}")
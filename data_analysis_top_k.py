import heapq
import time
import random

def get_top_k_with_heap(data_dict, k):
    """辞書データから売上（値）のトップKを抽出する (O(N log K))"""
    # 辞書のアイテム (商品ID, 注文数) を、注文数を基準にトップK件抽出
    # key=lambda x: x[1] は「注文数」を見て比較するという意味
    return heapq.nlargest(k, data_dict.items(), key=lambda x: x[1])

if __name__ == '__main__':
    # 1. 10万種類の商品がバラバラに売れている集計データを作成
    # 商品ID: 注文数
    product_counts = {i: random.randint(1, 100000) for i in range(100000)}

    # 2. トップ10を抽出する時間を計測
    k = 10
    start = time.time()
    top_k = get_top_k_with_heap(product_counts, k)
    end = time.time()

    print(f"{len(product_counts)}種類の商品からトップ{k}を抽出する時間: {end - start:.6f} 秒")
    
    print("--- 売上トップ10 ---")
    for rank, (product_id, count) in enumerate(top_k, 1):
        print(f"{rank}位: 商品ID {product_id} ({count}件)")
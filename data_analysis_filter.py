import time

def filter_with_list(all_ids, target_ids):
    """リストのまま検索する手法 (O(N * M))"""
    return [user_id for user_id in all_ids if user_id in target_ids]

def filter_with_set(all_ids, target_ids):
    """集合(set)に変換して検索する手法 (O(N + M))"""
    # 検索対象をハッシュテーブルに変換（ここがポイント！）
    target_set = set(target_ids)
    return [user_id for user_id in all_ids if user_id in target_set]

if __name__ == '__main__':
    # 1. テストデータの作成（数万件規模にすると差がはっきり出ます）
    all_user_ids = list(range(100000))        # 10万人のユーザー
    target_user_ids = list(range(50000, 60000)) # 1万人のキャンペーン対象者

    # --- 手法Aの計測 ---
    start = time.time()
    res_a = filter_with_list(all_user_ids, target_user_ids)
    end = time.time()
    print(f"リスト検索の時間: {end - start:.4f} 秒")

    # --- 手法Bの計測 ---
    start = time.time()
    res_b = filter_with_set(all_user_ids, target_user_ids)
    end = time.time()
    print(f"セット検索の時間: {end - start:.4f} 秒")

    # 結果の検証
    assert res_a == res_b
    print("✅ 両方の手法で同じ結果が得られました。")
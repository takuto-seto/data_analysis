def quick_sort(data):
    if len(data) <= 1:
        return data
    
    pivot = data[0]
    less = [i for i in data[1:] if i <= pivot]
    greater = [i for i in data[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)



def clean_and_rank_data(raw_data):
    
    cleaned_data = [i for i in raw_data if i > 0]

    if not cleaned_data:
        return []
    
    #ソートを実行
    sorted_data = quick_sort(cleaned_data)
    #　"[::-1]"で降順に並び替え
    sorted_data_desc = sorted_data[::-1]

    #重複の削除
    unique_data = []

    if sorted_data_desc:
        unique_data.append(sorted_data_desc[0])

        for i in range(1, len(sorted_data_desc)):
            if sorted_data_desc[i] != sorted_data_desc[i - 1]:
                unique_data.append(sorted_data_desc[i])
    
    return unique_data


if __name__ == '__main__':
    # テスト用：Eコマースの売上データ（異常値・重複あり）
    sales_data = [1200, 500, -100, 1200, 3000, 500, 800, 0, 3000]
    
    result = clean_and_rank_data(sales_data)
    
    # 期待される結果: [3000, 1200, 800, 500]
    print(f"元のデータ: {sales_data}")
    print(f"クリーン後のランキング: {result}")
    
    # 検証
    expected = [3000, 1200, 800, 500]
    assert result == expected, f"テスト失敗: {result} != {expected}"
    print("✅ データ分析前処理テスト成功！")
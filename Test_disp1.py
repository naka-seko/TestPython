# コレクション Test2 (6/19)
# 人数を入れる(0～9999)
def input_kensu():
    while True:
        try:
            in_kensu = int(input("(End:9999) "))
            if (in_kensu < 0) or (in_kensu > 9999):
                continue
            else:
                return (in_kensu)
        except ValueError:
            print("数字（整数）を入れて下さい。")

# 合計値, 平均値, 件数の算出
def total_and_average_and_number(values):
    total = 0
    for value in values:
        total = total + value

    # データの件数を求める
    num = len(values)

    # 合計値 ÷ 件数 で平均値を求める
    average = total / num

    # 戻り値として (合計値, 平均値, 件数) のタプルを返す
    return (total, average, num)

# メインルーチン
# 初期設定
values = []
index = 0
max_index = 6 # 日付数は1週間(7日)

# リストに出力
while index <= max_index :
    print(index + 1,"日目は何件ですか？")
    in_kensu = input_kensu()

    if(in_kensu == 9999):
        if(index == 0):
            values = [0]
        break

# リストへ追加、カウントアップ
    values.insert(index, in_kensu)
    index = index + 1

# 算出＆出力
total,average,number = total_and_average_and_number(values)
print(values, "の", "合計は", total, "平均は", average, "件数は", number, "です。")

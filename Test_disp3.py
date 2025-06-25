import pandas as pd
# 年齢を入れる
def input_nenrei():
  while True:
    try:
      in_nenrei = int(input("対象年齢（20～35）以上は？"))
      if (in_nenrei < 20) or (in_nenrei > 35):
        continue
      else:
        return (in_nenrei)

    except ValueError:
      print("数字（整数）を入れて下さい。")

# データを作成
data = {'名前': ['田中', '佐藤', '鈴木', '山田'],
        '年齢': [25, 30, 28, 27],
        '職業': ['エンジニア', 'デザイナー', '営業', '人事']}
# DataFrameという形式に変換
df = pd.DataFrame(data)

# 年齢が、入力年齢以上の人を抽出
m_nenrei = input_nenrei()
older_than = df[df['年齢'] >= m_nenrei]

# 結果を表示
if older_than.empty:
  print("該当データなし")
else:
  print(older_than)

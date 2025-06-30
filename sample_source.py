# ループ(while)　Test Source
text = ""
end_text = "finish"

while text != end_text:
    # 文字を入力する
    print(end_text)
    text = input("と入力してください:")

    print(text, "と入力されました。")
print("終了しました。")

# リストオブジェクト anc --> ABC
list_obj = ["apple", "orange", "banana"]
for fruit_name in list_obj:

    upper_name = fruit_name.upper()
    print(upper_name)

# タプルオブジェクト anc --> ABC
tuple_obj = ("apple", "orange", "banana")
for fruit_name in tuple_obj:

    upper_name = fruit_name.upper()
    print(upper_name)

# 文字列オブジェクト hello --> HELLO
str_obj = "hello"
for letter in str_obj:

    upper_letter = letter.upper()
    print(upper_letter)

# 辞書オブジェクト English --> Japanese
# テキストファイルから辞書を作成
animal_words = {}
try:
    with open("jisyo_animal.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or "," not in line:
                continue
            english, japanese = line.split(",", 1)
            animal_words[english.strip()] = japanese.strip()
except FileNotFoundError:
    print("jisyo_animal.txt が見つかりません。空の辞書で開始します。")

# 辞書の単語数、内容を表示
print("動物の辞書の単語数:", len(animal_words))

for english in animal_words:
    # 辞書から日本語を取得
    # 辞書のキーを使って値を取得
    japanese = animal_words[english]
    print(english, "は", japanese, "です。")

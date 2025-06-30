# (2025/06/19 Added)

# 辞書オブジェクト　Test Source
def disp_english_words():
    print(len(english_words))

    for english in english_words:
        dic_word = english_words[english]
        print(english, ":", dic_word)

# 辞書オブジェクトメイン
# テキストファイルから辞書を作成
english_words = {}
try:
    with open("jisyo_fruit.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or "," not in line:
                continue
            english, japanese = line.split(",", 1)
            english_words[english.strip()] = japanese.strip()
except FileNotFoundError:
    print("words.txt が見つかりません。空の辞書で開始します。")

disp_english_words()

# 辞書を追加
english_words ["banana"] = "バナナ"
disp_english_words()

# 辞書を置換
english_words ["banana"] = "スイートバナナ"
disp_english_words()

# 辞書を削除
del english_words ["orange"]
disp_english_words()

# 該当辞書を出力
key = input("英単語を入力してください：")
if(key in english_words) :
    print("日本語：", english_words[key])
else :
    print("その英単語に対する辞書は有りません。")

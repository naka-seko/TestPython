# (2025/06/19 Added)
# ループ(while)　Test Source
text = ""
end_text = "finish"

while text != end_text:
    # 文字を入力する
    print(end_text)
    text = input("と入力してください:")

    print(text, "と入力されました。")

print("終了しました。")

# 辞書オブジェクト　Test Source
def disp_english_words():
    print(len(english_words))

    for english in english_words:
        dic_word = english_words[english]
        print(english, ":", dic_word)

# 辞書オブジェクトメイン
english_words = {"apple": "りんご", "orange": "みかん", "peach": "もも"}
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

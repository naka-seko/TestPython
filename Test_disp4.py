# Test Source
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
dict_obj = {"dog": "犬", "cat": "猫", "parrot": "オウム"}
for english in dict_obj:

    japanese = dict_obj[english]
    print(english, "は", japanese, "です。")

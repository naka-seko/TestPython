# 年齢を入れる
def input_nenrei():

    while True:
        try:
            in_age = int(input("年齢はいくつですか？(0～120) "))
            if (in_age < 0) or (in_age > 120):
                continue
            else:
                return (in_age)
        except ValueError:
            print("数字（整数）を入れて下さい。")

# 身長を入れる
def input_height():

    while True:
        try:
            in_height = float(input("身長は何センチ？(100～300) "))
            if (in_height < 100) or (in_height > 300):
                continue
            else:
                return (in_height)
        except ValueError:
            print("数字（小数点１桁迄）を入れて下さい。")

# 年齢と身長の初期値を入れる
min_age = 10
min_height = 110.0

# 年齢と身長を入れる
age = input_nenrei()
height = input_height()

# 判定処理
if (min_age <= age) and (min_height <= height):
    print("お乗りいただけます")
else:
    print("ご遠慮ください")

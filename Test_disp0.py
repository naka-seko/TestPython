# 年齢を入れる
def input_nenrei():
    # 0以下や120以上の値は再入力を促す
    # 数字以外の値は再入力を促す
    # 入力値は整数値として返す
    min_inage = 0
    max_inage = 120

    while True:
        try:
            range_disp = f"年齢はいくつですか？({min_inage}～{max_inage}):"
            in_age = int(input(range_disp))
            if (in_age < min_inage) or (in_age > max_inage):
                continue
            else:
                return (in_age)
        except ValueError:
            print("数字（整数）を入れて下さい。")

# 身長を入れる
def input_height():
    # 100以下や300以上の値は再入力を促す
    # 数字以外の値は再入力を促す
    # 入力値は小数点１桁までの浮動小数点数として返す
    min_inheight = 100.0
    max_inheight = 300.0

    while True:
        try:
            range_disp = f"身長は何センチ？({min_inheight}～{max_inheight}):"
            in_height = float(input(range_disp))
            if (in_height < min_inheight) or (in_height > max_inheight):
                continue
            else:
                return (in_height)
        except ValueError:
            print("数字（小数点１桁迄）を入れて下さい。")

# 最低年齢と身長
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

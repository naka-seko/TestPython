# カレンダー表示(6/24)
import calendar
min_nen = 2000
max_nen = 2099

# 対象年入力
while True:
    try:
        in_nen = int(input("対象年(2000～2099)"))
        if (in_nen < min_nen) or (in_nen > max_nen):
            continue
        break

    except ValueError:
        print("数字を入れて下さい。")
# 対象月入力
while True:
    try:
        in_tuki = int(input("対象月(01～12)"))
        if (in_tuki < 1) or (in_tuki > 12):
            continue
        break

    except ValueError:
        print("数字を入れて下さい。")

# カレンダー表示
calendar.prmonth(in_nen,in_tuki)

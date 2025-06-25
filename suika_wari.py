# Pythonでスイカ割ゲーム作成
import random
import math

BOARD_SIZE = 5  # ボードの初期サイズ

# x座標とy座標の生成(generate_position)
def generate_position(size):
    # 0以上size未満の範囲で、x座標とy座標を生成する
    x = random.randrange(0, size)  # x座標
    y = random.randrange(0, size)  # y座標

    return (x, y)

# ２点間の距離算出(calc_distance)
def calc_distance(pos1, pos2):

    diff_x = pos1[0] - pos2[0]
    diff_y = pos1[1] - pos2[1]

    return math.sqrt(diff_x**2 + diff_y**2)

# プレイヤーを移動(move_position)
def move_position(direction, pos):
    # direction にしたがって、posを移動する
    current_x, current_y = pos

    if direction == "n":
        current_y = current_y - 1
    elif direction == "s":
        current_y = current_y + 1
    elif direction == "w":
        current_x = current_x - 1
    elif direction == "e":
        current_x = current_x + 1

    return (current_x, current_y)

# スイカ割ゲーム(suika_wari)
def suika_wari():
    suika_pos = generate_position(BOARD_SIZE) # スイカの位置を決める
    player_pos = generate_position(BOARD_SIZE) # プレイヤーの位置を決める

    while suika_pos != player_pos:
        # スイカとプレイヤーの距離を求める
        distance = calc_distance(suika_pos, player_pos)
        print("スイカへの距離:", distance)

        # プレイヤーを移動させる
        c = input("n:北に移動 s:南に移動 e:東に移動 w:西に移動")
        player_pos = move_position(c, player_pos)

# スイカ割ゲーム終了
    print("スイカを割りました！")

# スイカ割ゲームStart
suika_wari()
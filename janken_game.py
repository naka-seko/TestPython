# じゃんけんゲーム
import random
# じゃんけんの手を定義
# グーは0、チョキは1、パーは2
HANDS = ["グー", "チョキ", "パー"]
ROCK = 0
SCISSORS = 1
PAPER = 2

# ゲームのメッセージを定義
WELCOME_MESSAGE = "じゃんけん勝負"
INSTRUCTION_MESSAGE = "グーチョキパーを数字で入力してください"
# じゃんけんの手の選択肢を表示するメッセージ
HAND_OPTIONS_MESSAGE = "{}:{}"
PLAYER_INPUT_MESSAGE = "\n最初はぐー、じゃんけん："
# コンピュータとプレイヤーの選択を表示するメッセージ
COMPUTER_CHOICE_MESSAGE = "コンピュータ：{}"
PLAYER_CHOICE_MESSAGE = "プレイヤー　：{}"
# じゃんけんの結果を表示するメッセージ
DRAW_MESSAGE = "引き分けです！"
WIN_MESSAGE = "あなたの勝ち！"
LOSE_MESSAGE = "あなたの負け..."

# じゃんけんゲームのロジックを実行する関数
def main():
    print(WELCOME_MESSAGE)
    print(INSTRUCTION_MESSAGE)
    for idx, hand in enumerate(HANDS):
        print(HAND_OPTIONS_MESSAGE.format(idx, hand))

    # プレイヤーの入力を受け取る
    player_choice = int(input(PLAYER_INPUT_MESSAGE))
    computer_choice = random.randint(0, len(HANDS) - 1)

    print(COMPUTER_CHOICE_MESSAGE.format(HANDS[computer_choice]))
    print(PLAYER_CHOICE_MESSAGE.format(HANDS[player_choice]))

    # じゃんけんの結果を判定
    # プレイヤーの選択とコンピュータの選択が同じ場合は引き分け
    if player_choice == computer_choice:
        print(DRAW_MESSAGE)
    # グーがチョキに勝つ、チョキがパーに勝つ、パーがグーに勝つ
    elif (player_choice == ROCK and computer_choice == SCISSORS) or \
        (player_choice == SCISSORS and computer_choice == PAPER) or \
        (player_choice == PAPER and computer_choice == ROCK):
        print(WIN_MESSAGE)
    # それ以外は負け
    else:
        print(LOSE_MESSAGE)

# このスクリプトを直接実行した場合にのみ、main()を呼び出す
if __name__ == "__main__":
    main()
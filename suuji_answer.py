import random

def main():
    print("ようこそ。数字当てゲームへ！")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("１から１００の間で入力してね: "))
            attempts += 1

            if guess < number_to_guess:
                print("小さいです！")
            elif guess > number_to_guess:
                print("大きいです！")
            else:
                print(f"🎊ございます！ 入力された回数は {attempts} です。")
                break
        except ValueError:
            print("数字（整数）を入れてください。")

if __name__ == "__main__":
    main()

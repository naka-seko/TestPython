import mysql.connector

# 接続定義
sql_host = 'localhost'
sql_user = 'root'
sql_password = '************'
sql_database = 'mysql'

# テーブル名とカラム名（例: Name, Time_zone_id）
table_name = 'time_zone_name'
columns = ['Name', 'Time_zone_id']
# テキストファイルパス
text_file_path = 'time_zone_data.txt'

# テーブルのカラム名を使用して、SQLクエリを定義
col_str = ','.join(columns)
# SQLクエリの定義
sql_sel1 = f"SELECT {col_str} FROM {table_name} ORDER BY {columns[0]}"
sql_sel2 = f"SELECT {col_str} FROM {table_name} WHERE {columns[0]}=%s"
sql_upd1 = f"UPDATE {table_name} SET {columns[1]}=%s WHERE {columns[0]}=%s"
sql_del1 = f"DELETE FROM {table_name} WHERE {columns[0]}=%s"
sql_ins1 = f"INSERT INTO {table_name}({col_str}) VALUES(%s,%s)"

def input_upd_del():
    while True:
        try:
            # ここでは削除と更新の選択を促すメッセージを表示
            in_upd_del = input("削除する場合は d を、更新する場合は u を入力して下さい：")
            if (in_upd_del == 'd') or (in_upd_del == 'u'):
                # 入力が 'd' 又は 'u' の場合はそのまま返す
                return (in_upd_del)
            else:
                # それ以外の入力はエラーメッセージを表示して再入力を促す
                print("d 又は u を入力して下さい。")
                continue
        except ValueError:
            print("u 又は d を入力して下さい。")

# タイムゾーン名とIDの入力を促すメッセージ
while True:
    try:
        where_name = input("タイムゾーン名を入力して下さい(例: Korea): ")
        # 入力が空でないことを確認
        # 空の文字列は許可しない
        if not where_name.strip():
            print("空の文字列は入力出来ません。")
            continue
        # 入力が文字列であることを確認
        if not isinstance(where_name, str):
            print("文字列を入れて下さい。")
            continue
        break

    except ValueError:
        print("文字列を入れて下さい。")

# タイムゾーンIDの入力を促すメッセージ
while True:
    try:
        data_tmid = int(input("タイムゾーンIDを入力して下さい(例: 8): "))
        if (data_tmid < 0) or (data_tmid > 23):
            print("0から23の数字を入れて下さい。")
            continue
        break

    except ValueError:
        print("数字を入れて下さい。")

# MySQLに接続
conn = mysql.connector.connect(
    host=sql_host,
    user=sql_user,
    password=sql_password,
    database=sql_database
)
# カーソルを作成
cursor = conn.cursor()

# データ取得クエリ（WHERE句あり）
# cursor.execute(sql_sel2, (where_name,))
# row = cursor.fetchone()
# if not row:
#     result_list = []
# else:
#     result_list = [row]

# データ削除、更新、挿入クエリ
cursor.execute(sql_sel2, (where_name,))
row = cursor.fetchone()
if row:
    # タイムゾーン名が存在する場合、更新または削除の選択を促す
    in_upd_del = input_upd_del()
    if in_upd_del == 'u':
        # 更新を行う
        print(f"Name'{where_name}'は存在します。更新を行います。")
        cursor.execute(sql_upd1, (data_tmid, where_name))
        conn.commit()  # 更新を反映
    elif in_upd_del == 'd':
        # 削除を行う
        print(f"Name'{where_name}'は存在します。削除を行います。")
        cursor.execute(sql_del1, (where_name,))
        conn.commit()  # 削除を反映
else:
    # タイムゾーン名が存在しない場合、挿入を行う
    print(f"Name'{where_name}'は存在しません。挿入を行います。")
    cursor.execute(sql_ins1, (where_name, data_tmid))
    conn.commit()  # 挿入を反映

# データ取得クエリ（WHERE句なし）
cursor.execute(sql_sel1)
result_list = cursor.fetchall()

# カーソルと接続を閉じる
cursor.close()
conn.close()

# データ出力処理(コンソール出力)
for row in result_list:
    print(', '.join(f"{col}: {val}" for col, val in zip(columns, row)))

# ファイル出力処理(csv形式)
with open(text_file_path, "w", encoding="utf-8") as f_file:
    for row in result_list:
        f_file.write(','.join(str(val) for val in row) + "\n")

# ファイル出力完了メッセージ
print(f"MySQLのテーブル情報を{text_file_path}に出力しました。")

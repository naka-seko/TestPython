import mysql.connector

# 接続定義
sql_host = 'localhost'
sql_user = 'root'
sql_password = '************'
sql_database = 'mysql'

# テーブル名とカラム名
table_name = 'time_zone_name'
columns = ['Name', 'Time_zone_id']
# テキストファイルパス
text_file_path = 'time_zone_data_out.txt'

# テーブルのカラム名を使用して、SQLクエリを定義
col_str = ','.join(columns)
# SQLクエリの定義
sql_sel1 = f"SELECT {col_str} FROM {table_name} ORDER BY {columns[0]}"
sql_sel2 = f"SELECT {col_str} FROM {table_name} WHERE {columns[0]}=%s"
sql_upd1 = f"UPDATE {table_name} SET {columns[1]}=%s WHERE {columns[0]}=%s"
sql_del1 = f"DELETE FROM {table_name} WHERE {columns[0]}=%s"
sql_ins1 = f"INSERT INTO {table_name}({col_str}) VALUES(%s,%s)"

# タイムゾーン名を入力する関数
def input_time_zone_name():
    while True:
        try:
            where_name = input("タイムゾーン名を入力して下さい(例: japan): ")
            # 入力が空でないことを確認
            # 空の文字列は許可しない
            if not where_name.strip():
                print("空の文字列は入力出来ません。")
                continue
            # 入力が文字列であることを確認
            if not isinstance(where_name, str):
                print("文字列を入れて下さい。")
                continue
            return where_name

        except ValueError:
            print("文字列を入れて下さい。")

# タイムゾーンIDを入力する関数
def input_time_zone_id():
    while True:
        try:
            data_tmid = int(input("タイムゾーンIDを入力して下さい(例: 9): "))
            if (data_tmid < 0) or (data_tmid > 23):
                print("0から23の数字を入れて下さい。")
                continue
            return data_tmid

        except ValueError:
            print("タイムゾーンIDの入力が無いか、数字以外です。")
            data_tmid = None
            return data_tmid

# データ操作（検索、更新、削除、挿入）する関数
def select_udi_sql(conn):
    # カーソル定義
    cursor = conn.cursor()

    # タイムゾーン名の入力を促すメッセージ
    where_name = input_time_zone_name()
    # データ取得クエリ（WHERE句あり）
    cursor.execute(sql_sel2, (where_name,))
    row = cursor.fetchone()
    upd_del = '' # 更新削除フラグ初期化

    if not row:
        result_list = []
        data_tmid = input_time_zone_id()
        if data_tmid is None:
            data_tmid = 0 # 挿入時で数字以外は０とする

        # タイムゾーン名が存在しない場合、挿入を行う
        print(f"Name'{where_name}'は存在しません。挿入を行います。")
        cursor.execute(sql_ins1, (where_name, data_tmid))
        conn.commit()  # 挿入を反映
    else:
        result_list = [row]
        # タイムゾーンIDの入力を促すメッセージ
        data_tmid = input_time_zone_id()
        if data_tmid is not None and int(data_tmid) == row[1]:
            pass # タイムゾーンIDが同じ場合は何もしない
        elif data_tmid is None:
            upd_del = 'd' # タイムゾーンID未入力なら削除
        else:
            upd_del = 'u' # タイムゾーンIDが異なる場合は更新

        # データ削除、更新クエリ
        if upd_del == 'u':
            # 更新を行う
            print(f"Name'{where_name}'は存在します。更新を行います。")
            cursor.execute(sql_upd1, (data_tmid, where_name))
            conn.commit()  # 更新を反映
        elif upd_del == 'd':
            # 削除を行う
            print(f"Name'{where_name}'は存在します。削除を行います。")
            cursor.execute(sql_del1, (where_name,))
            conn.commit()  # 削除を反映

    # データ取得クエリ（WHERE句なし）
    cursor.execute(sql_sel1)
    result_list = cursor.fetchall()

    # カーソルを閉じる
    cursor.close()
    return result_list

# 出力（コンソール＆ファイル）する関数
def output_display_file(file_path, result_list, columns):

    # 件数出力
    print(f"件数: {len(result_list)} 件")

    # データ出力処理(コンソール出力)
    if result_list:
        for row in result_list:
            print(', '.join(f"{col}: {val}" for col, val in zip(columns, row)))
    else:
        print("該当データはありません。")

    # ファイル出力処理(csv形式)
    with open(file_path, "w", encoding="utf-8") as f_file:
        for row in result_list:
            f_file.write(','.join(str(val) for val in row) + "\n")

    # ファイル出力完了メッセージ
    print(f"MySQLのテーブル情報を{file_path}に{len(result_list)}件出力しました。")

# MySQLに接続
conn = mysql.connector.connect(
    host=sql_host,
    user=sql_user,
    password=sql_password,
    database=sql_database
)

# データ操作（検索、更新、削除、挿入）処理
result_list = select_udi_sql(conn)

conn.close() # 接続を閉じる

# 出力処理（コンソール＆ファイル）
output_display_file(text_file_path, result_list, columns)

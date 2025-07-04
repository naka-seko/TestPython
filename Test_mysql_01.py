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
sql_sel2 = f"SELECT {col_str} FROM {table_name} WHERE {columns[0]} = %s"

# データ取得する関数
def select_data_sql(conn):
    # カーソル定義
    cursor = conn.cursor()

    # タイムゾーン名の入力を促すメッセージ
    where_name = input("対象タイムゾーン名を入力して下さい(例: japan): ")
    if not where_name.strip():
        print("入力が空です。全件取得します。")
        where_name = None
    else:
        print(f"入力されたタイムゾーン名: {where_name}")

    # データ取得クエリの実行
    # WHERE句がない場合は全件取得、ある場合は指定されたタイムゾーン名で取得
    if where_name is None:
        # データ取得クエリ（WHERE句なし）
        cursor.execute(sql_sel1)
        result_list = cursor.fetchall()
    else:
        # データ取得クエリ（WHERE句あり）
        cursor.execute(sql_sel2, (where_name,))
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

# データ取得処理
result_list = select_data_sql(conn)

conn.close() # 接続を閉じる

# 出力処理（コンソール＆ファイル）
output_display_file(text_file_path, result_list, columns)

import mysql.connector

# 接続定義
sql_host = 'localhost'
sql_user = 'root'
sql_password = '************'
sql_database = 'mysql'

# テーブル名とテキストファイルパス
table_name = 'time_zone_name'
text_file_path = 'time_zone_data_in.txt'

# テーブルのカラム名
columns = ['Name', 'Time_zone_id']

# SQLクエリの定義
# initial load クエリ（"で括られたデータ、,区切り、Windowsは\r\nで行終わり）
sql_rep = f"REPLACE INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s']*len(columns))})"

# テーブルの全データを別テーブルに一括挿入する関数
def replace_all_data_from_file(conn, table, file_path, columns):

    # カーソル定義
    cursor = conn.cursor()

    # ファイルを開いてデータを読み込み、テーブルに挿入
    with open(file_path, encoding='utf-8') as f_file:
        for line in f_file:
            # 空白文字を取り除き、行が空（空文字列）になった場合、
            # 以降の処理をスキップし、次の行の処理に移ります。
            line = line.strip()
            if not line:
                continue

            # 先頭と末尾のダブルクォートを除去し、カンマで分割
            if line.startswith('"') and line.endswith('"'):
                line = line[1:-1]
            values = [values.strip().strip('"') for values in line.split(',')]

            # 要素数とテーブルのカラム数が一致しているかを確認し、
            # 一致しない場合はスキップし、次の行の処理に移ります。
            if len(values) != len(columns):
                continue

            cursor.execute(sql_rep, values) # データファイルから、replaceする

    conn.commit()  # 変更をコミット
    cursor.close() # カーソルを閉じる

# MySQLに接続
conn = mysql.connector.connect(
    host=sql_host,
    user=sql_user,
    password=sql_password,
    database=sql_database
)

# ファイルからデータを読み込み、テーブルに挿入する関数
replace_all_data_from_file(conn, table_name, text_file_path, columns)

conn.close() # 接続を閉じる

# データ挿入完了メッセージ
print(f"{text_file_path} のデータを {table_name} テーブルに置換（挿入）しました。")

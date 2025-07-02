import mysql.connector

# 接続定義
sql_host = 'localhost'
sql_user = 'root'
sql_password = 'Seko19670614'
sql_database = 'mysql'

# MySQLに接続
conn = mysql.connector.connect(
    host=sql_host,
    user=sql_user,
    password=sql_password,
    database=sql_database
)

# テーブル名とテキストファイルパス
table_name = 'time_zone_name'
text_file_path = 'time_zone_data.txt'

# テーブルのカラム名（例: id, name, age）
columns = ['Name', 'Time_zone_id']

# ファイルからデータを読み込み、テーブルに挿入する関数
def insert_data_from_file(conn, file_path, table, columns):

    cursor = conn.cursor() # カーソルを作成

    # ファイルを開いてデータを読み込み、テーブルに挿入
    with open(file_path, encoding='utf-8') as f_file:
        for line in f_file:
            values = line.strip().split(',')  # カンマ区切りの場合
            if not line.strip() or len(values) != len(columns):
                continue
            sql = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['%s']*len(columns))})"
            cursor.execute(sql, values)
    conn.commit()  # 変更をコミット
    cursor.close() # カーソルを閉じる

# データ挿入
insert_data_from_file(conn, text_file_path, table_name, columns)

conn.close() # 接続を閉じる
# データ挿入完了メッセージ
print(f"Data from {text_file_path} has been inserted into the {table_name} table.")

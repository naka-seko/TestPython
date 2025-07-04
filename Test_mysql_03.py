import mysql.connector

# 接続定義
sql_host = 'localhost'
sql_user = 'root'
sql_password = '************'
sql_database = 'mysql'

# テーブル名とテキストファイルパス
table_name = 'time_zone_name'
text_file_path = 'time_zone_data_in.txt'

# SQLクエリの定義
# initial load クエリ（"で括られたデータ、,区切り、Windowsは\r\nで行終わり）
sql_load = f"""LOAD DATA LOCAL INFILE '{text_file_path}'
INTO TABLE {table_name}
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
"""

# MySQLに接続（テキストファイル true)
conn = mysql.connector.connect(
    host=sql_host,
    user=sql_user,
    password=sql_password,
    database=sql_database,
    allow_local_infile=True
)

# カーソル定義
cursor = conn.cursor()
# データファイルから、MySQLに初期ロードする
try:
    cursor.execute(sql_load)
    conn.commit() # 変更をコミット
finally:
    cursor.close()

conn.close() # 接続を閉じる

# データ挿入完了メッセージ
print(f"{text_file_path} のデータを {table_name} テーブルに初期ロードしました。")

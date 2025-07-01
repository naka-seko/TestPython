import mysql.connector

# Mysqlのクエリを実行して、データベースのテーブル権限を取得するスクリプト
# 接続定義
sql_host = 'localhost'
sql_user = 'root'
sql_password = '************'
sql_database = 'mysql'
# SQLクエリの定義
sql_sel1 = "SELECT Database_name,Table_name FROM innodb_table_stats"

# MySQLに接続
conn = mysql.connector.connect(
    host=sql_host,
    user=sql_user,
    password=sql_password,
    database=sql_database
)
# カーソルを作成
cursor = conn.cursor()

# データ取得クエリ
cursor.execute(sql_sel1)
# 結果を取得
# innodb_table_statsテーブルからデータベース名とテーブル名を取得
# ここでは、データベースのテーブル権限を表示するためのクエリを実行
result_list = cursor.fetchall()

# カーソルと接続を閉じる
cursor.close()
conn.close()

# 結果を表示
# データベースのテーブル権限を表示
for row in result_list:
    print(f"Database: {row[0]}, Table: {row[1]}")

# ファイル出力処理(csv形式)
with open("mysql_tables.txt", "w", encoding="utf-8") as f:
    for row in result_list:
        f.write(f"{row[0]},{row[1]}\n")

import pymysql

#dbServerName    = "127.0.0.1"
dbUser          = "root"
dbPassword      = ""
dbName          = "test"
charSet         = "utf8mb4"
cusrorType      = pymysql.cursors.DictCursor
connection   = pymysql.connect(user=dbUser, password=dbPassword,
                                     db=dbName, charset=charSet,cursorclass=cusrorType)
id_num = 0

with connection.cursor() as cursor:
    sqlQuery = "TRUNCATE TABLE user"
    cursor.execute(sqlQuery)
    sqlQuery = "TRUNCATE TABLE user_teaching_item"
    cursor.execute(sqlQuery)

#登録
def register(itemIds):
    with connection.cursor() as cursor:
        sql = "INSERT INTO user_teaching_item (id, tag) VALUES (%s, %s)"
        sql2 = "INSERT INTO user (id, push_key) VALUES (%s, %s)"
        global id_num
        print(id_num)
        id_num += 1
        for i in itemIds:
            r = cursor.execute(sql, (id_num, i))
        r2 = cursor.execute(sql2, (id_num, 0))
        # autocommitではないので、明示的にコミットする
        connection.commit()
        sql = "SELECT * FROM user_teaching_item"
        cursor.execute(sql)
        #sql2 = "SELECT * FROM user"
        #cursor.execute(sql2)
        results = cursor.fetchall()
        print(results)



#教えたい側のid引っ張る
def get_uids(itemId):
    with connection.cursor() as cursor:
        sql = "SELECT id FROM user_teaching_item WHERE tag = %s"
        cursor.execute(sql, itemId)

        # Select結果を取り出す
        results = cursor.fetchall()
        results = set(list(map(lambda dic: list(dic.values())[0], results)))
        return results

import pymysql

#dbServerName    = "127.0.0.1"
dbUser          = "root"
dbPassword      = ""
dbName          = "test"
charSet         = "utf8mb4"
cusrorType      = pymysql.cursors.DictCursor
connection   = pymysql.connect(user=dbUser, password=dbPassword,
                                     db=dbName, charset=charSet,cursorclass=cusrorType)
user_id = 0

with connection.cursor() as cursor:
    sqlQuery = "TRUNCATE TABLE user"
    cursor.execute(sqlQuery)
    sqlQuery = "TRUNCATE TABLE user_teaching_item"
    cursor.execute(sqlQuery)

class Item():
    def __init__(self, id, name):
        self.id = id
        self.name = name

#登録
def register(itemIds):
    with connection.cursor() as cursor:
        sql = "INSERT INTO user_teaching_item (id, tag) VALUES (%s, %s)"
        sql2 = "INSERT INTO user (id, push_key) VALUES (%s, %s)"
        global user_id
        print(user_id)
        user_id += 1
        for i in itemIds:
            r = cursor.execute(sql, (user_id, i))
        r2 = cursor.execute(sql2, (user_id, 0))

        connection.commit()
        sql = "SELECT * FROM user_teaching_item"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        return user_id


#教えたい側のid引っ張る
def get_uids(itemId):
    with connection.cursor() as cursor:
        sql = "SELECT id FROM user_teaching_item WHERE tag = %s"
        cursor.execute(sql, itemId)

        results = cursor.fetchall()
        results = set(list(map(lambda dic: dic['id'], results)))
        return results

#teaching_itemからidとname持ってくる
def get_items():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM teaching_item"
        cursor.execute(sql)

        results = cursor.fetchall()
        results = list(map(lambda items: Item(items['id'], items['name']), results))
        return results

def get_item_name(itemId):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM teaching_item WHERE id = %s"
        cursor.execute(sql, itemId)

        results = cursor.fetchall()
        name = results[0]['name']
        return name

def get_item_names(itemIds):
    names = []
    for itemId in itemIds:
        names.append(get_item_name(itemId))
    return names

import pymssql

conny = {
    "host": "(local)",
    "user": "sa",
    "passwd": "123",
    "db": "NHMFDServerDB",
    "charset": "utf8",
}

# 连接数据库
try:
    conn = pymssql.connect(
        host=conny["host"],
        user=conny["user"],
        password=conny["passwd"],
        database=conny["db"],
        charset=conny["charset"],
    )
    cur = conn.cursor()
    sql = "select * from DetLog"
    # ===========================
    # retrieve 查询
    # 注意：游标执行多次查询只会保留最后一次执行结果
    # ===========================
    # fetchall 所有结果
    # fetchone 单个结果
    cur.execute(sql)
    data = cur.fetchall()
    print(data)
except pymssql.Error as e:
    print("数据库连接失败:", e)

from pymysql import Connection

conn = Connection(
    host="localhost", #主机名
    port=3306,  #端口
    user="root",  #账户
    passwd="Hyh070106",  #密码
    autocommit=True #自动确认
)

# print(conn.get_server_info())


cursor = conn.cursor()  #获取游标对象
conn.select_db("DML_demo")  #选择数据库
# cursor.execute("create table test_pymysql(id int)")  #创建表格

# cursor.execute("select * from student2") #查询表格
# results = cursor.fetchall()
# for r in results:
#     print(r)

#数据插入
cursor.execute("insert into student values(10002, '林俊杰', 33)")
#通过commit手动确认
# conn.commit()
conn.close()
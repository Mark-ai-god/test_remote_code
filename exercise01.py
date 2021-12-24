"""
create database Test;
use Test;
create table index_test (
id int primary key auto_increment,
name varchar(30));
"""
import pymysql
#host与port可以不写的  但是写的话别写错  如port是整数！！！
db = pymysql.connect(host='localhost',port=3306,user='root',password="123",database='Test',charset='utf8')
# 负责调用执行sql语句，操作数据，得到结果
cur = db.cursor()

sql = "insert into index_test (name) values (%s);"
exe = []
s = "Tom"
for i in range(2000000):
    name = s + str(i)
    exe.append(name)


try:
    cur.executemany(sql,exe)
    db.commit()
except:
    db.rollback()

db.close()

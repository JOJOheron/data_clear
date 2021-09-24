import pymysql
#打开数据库连接
"""
a class to query data from databases,it returns a datalist from each row
eg. read1=QuerymySql("localhost", "root","123456","recall","utf8","select distinct 制造商 from Recall")
"""
def QuerymySql(host, user, password, database, charset,sqlrequset):
    conn = pymysql.connect(host=host, user=user, password=password, database=database, charset=charset)
    #获取游标
    cur=conn.cursor()
    cur.execute(sqlrequset)
    readlist=[]
    while 1:
        res=cur.fetchone()
        if res is None:
            #表示已经取完结果集
            break
        readlist.append(res)
    cur.close()
    conn.commit()
    conn.close()
    return readlist
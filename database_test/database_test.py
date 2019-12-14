import pymysql

connect = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    passwd = 'wang99119.',
    db='test',
    port = 3306,
    charset = 'utf8'
)
cursor = connect.cursor()
cursor.execute('select * from pet;')
data = cursor.fetchone()
print (data)
connect.close()
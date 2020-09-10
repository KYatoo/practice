import pymysql

def get_connection():
    # 连接数据库
    connect = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='wang99119.',
        db='test',
        port=3306,
        charset='utf8'
    )
    # 获取游标(指定获取的数据格式，这里设定返回dict格式)
    return connect, connect.cursor(cursor=pymysql.cursors.DictCursor)

def select_all(sql, args=None):
    """查询所有"""
    conn, cursor = get_connection()
    cursor.execute(sql, args)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results


def select_one(sql, args):
    """查询一个"""
    conn, cursor = get_connection()
    cursor.execute(sql, args)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


def update(sql, args):
    """修改数据"""
    conn, cursor = get_connection()
    cursor.execute(sql, args)
    conn.commit()
    cursor.close()
    conn.close()


def create(sql, args):
    """新增数据"""
    conn, cursor = get_connection()
    cursor.execute(sql, args)
    conn.commit()
    cursor.close()
    conn.close()


def delete(sql, args):
    """删除数据"""
    conn, cursor = get_connection()
    cursor.execute(sql, args)
    conn.commit()
    cursor.close()


if __name__ == "__main__":
    [connect,cursor]=get_connection()
    cursor.execute('select * from pet;')
    data = cursor.fetchone()
    print(data)
    print(type(cursor))
    print(connect)
    print(cursor)
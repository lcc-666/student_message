import pymysql

def insert(tu):
    valuse=tu
    db = pymysql.connect(host='www.chaogezuishuai.top',
                           user="root",
                           port=3306,
                           db="student",
                           password="NRAHbsqt941",
                           charset="utf8")
    cursor=db.cursor()
    sql="INSERT INTO student(id,name,sex,adress,phone,major) values('%s','%s','%s','%s','%s','%s')"%valuse
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    return 1

def selects(id):
    db = pymysql.connect(host='www.chaogezuishuai.top',
                           user="root",
                           port=3306,
                           db="student",
                           password="NRAHbsqt941",
                           charset="utf8")
    cursor=db.cursor()
    sql="SELECT * FROM student WHERE id='%s';"%id
    cursor.execute(sql)
    result=list(cursor.fetchall()[0])
    result.remove(id)
    db.commit()
    cursor.close()
    db.close()
    return result

def updata(tu):
    valuse=list(tu)[1:]
    id=list(tu)[0]
    valuse.append(id)
    valuse=tuple(valuse)
    db = pymysql.connect(host='www.chaogezuishuai.top',
                           user="root",
                           port=3306,
                           db="student",
                           password="NRAHbsqt941",
                           charset="utf8")
    cursor=db.cursor()
    sql="UPDATE student set name='%s',sex='%s',adress='%s',phone='%s',major='%s' where id='%s';"%valuse
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    return 1

def delete(id):
    db = pymysql.connect(host='www.chaogezuishuai.top',
                         user="root",
                         port=3306,
                         db="student",
                         password="NRAHbsqt941",
                         charset="utf8")
    cursor = db.cursor()
    sql = "DELETE FROM student WHERE id='%s';" % id
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    return 1




if __name__=="__main__":
    # tu=('20190100702', '李畅超', '男', '山西省太原市', '17635684495', '大数据')
    # insert(tu)
    #updata(tu)
    delete('20190100702')
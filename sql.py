import pymysql

class insert(list):
    db = pymysql.connect(host='www.chaogezuishuai.top',
                           user="root",
                           port=3306,
                           db="student",
                           password="NRAHbsqt941",
                           charset="utf8")
    cursor=db.cursor()
    sql=''


if __name__=="__main__":
    tu=(45641, 'dwa', 'fes', 'hdhr', 'sefd', 'sefg')
    insert(tu)
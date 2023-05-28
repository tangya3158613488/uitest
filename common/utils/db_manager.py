#!/usr/bin/python
# coding=utf-8

import pymysql.cursors


class DatabaseManager:
    def __init__(self):
        self.db = pymysql.connect(host="192.168.15.166", port=3306, user="tester", passwd="changba123",
                                  db="ktv_monitor",
                                  charset='utf8', cursorclass=pymysql.cursors.DictCursor)

    def insert(self, sql):
        global cursor
        try:
            cursor = self.db.cursor()
            effect_row = cursor.execute(sql)
            self.db.commit()
            if effect_row > 0:
                print("添加成功!!!")
            else:
                print("添加失败!!!")
        except Exception as e:
            print(e)
            self.db.rollback()

    def query(self, sql):
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
            return data
        except Exception as e:
            print(e)
        self.db.close()

    def update(self, sql):
        global cursor
        try:
            cursor = self.db.cursor()
            effect_row = cursor.execute(sql)
            self.db.commit()
            if effect_row > 0:
                print("更新成功!!!")
            else:
                print("更新失败!!!")
        except Exception as e:
            print(e)
            self.db.rollback()

    def delete(self, sql):
        global cursor
        try:
            cursor = self.db.cursor()
            effect_row = cursor.execute(sql)
            self.db.commit()
            if effect_row > 0:
                print("删除成功!!!")
            else:
                print("删除失败!!!")
        except Exception as e:
            print(e)
            self.db.rollback()

# if __name__ == "__main__":
# DatabaseManager = DatabaseManager()
# print(DatabaseManager.query("select * from java_logs"))

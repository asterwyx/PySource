import sqlite3
from sys import stderr

# 初始化
conn = sqlite3.connect("stardict.db")
cursor = conn.cursor()


def get_info(word):
    sql = "SELECT * FROM stardict WHERE sw=\"%s\";" % word
    result = cursor.execute(sql)
    return result

result = get_info("swear")
print(result.fetchone())
result = get_info("swipe")
print(result.fetchone())

# 善后模块
cursor.close()
try:
    conn.commit()
except:
    conn.rollback()
    print("提交失败！")
finally:
    conn.close()

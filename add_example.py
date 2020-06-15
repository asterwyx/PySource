import sqlite3
from sys import stderr

# 初始化
conn = sqlite3.connect("stardict.db")
cursor = conn.cursor()
fp = open("ODE_Trimed.txt", mode="r", encoding="utf-8")
fp.readline()
end = False


def getone(file):
    detail = ""
    word = file.readline()
    if word != "----------example\n":
        word = word[0:-1]
        tmp = file.readline()
    else:
        word = None
    tmp = file.readline()
    while tmp != "----------word\n":
        if tmp != "----------example\n":
            detail += tmp
        tmp = file.readline()
        if tmp == "":
            global end # 这里一定要有，不然Python会将下面的变量当作一个新定义的局部变量
            end = True
            break
    if detail != "":
        detail = detail[0:-1]
    return (word, detail)

def update_detail(word, new_value):
    sql = "UPDATE stardict SET detail=\"%s\" WHERE sw=\"%s\";" % (new_value, word)
    # print(sql)
    try:
        result = cursor.execute(sql)
    except sqlite3.OperationalError:
        new_value = str(new_value).replace('"', '\'', -1)
        sql = "UPDATE stardict SET detail=\"%s\" WHERE sw=\"%s\";" % (new_value, word)
        # print(sql)
        result = cursor.execute(sql)
    if cursor.rowcount == 1:
        print("成功")
    else:
        print("失败")
    return result


def get_info(word):
    sql = "SELECT * FROM stardict WHERE sw=\"%s\";" % word
    result = cursor.execute(sql)
    return result

while not end:
    word_entry = getone(fp)
    # print(word_entry)
    update_detail(word_entry[0], word_entry[1])
# result = get_info("expert")
# msg = result.fetchone()
# print(msg)
print("Done!")


# 善后模块
cursor.close()
try:
    conn.commit()
except:
    conn.rollback()
    print("提交失败！")
finally:
    conn.close()
fp.close()


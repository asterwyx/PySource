from datetime import datetime
now = datetime.now()
print(now)
print(type(now))

# 使用datetime类传入参数创建一个时间日期对象
dt = datetime(2015, 4, 19, 12, 20)
print(dt)
print(type(dt))

# datetime转换成timestamp
new_dt = dt.timestamp()
print(new_dt)
print(type(new_dt))

# 使用datetime提供的fromtimestamp()方法将timestamp转换成datetime
t = 1429417200.0
dt1 = datetime.fromtimestamp(t)
print(dt1)
print(type(dt1))

# str转换成datetime，使用strptime()函数
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S') #给strptime()函数一个日期和时间的格式化字符串，后面的的参数再详细注明格式
print(cday)
# 转换后的datetime没有时区信息


# datetime转换成str，使用strftime()函数
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

# datetime相加减，直接使用+-号，不过需要导入timedelta这个类
from datetime import timedelta
now = datetime.now()
print(now)
timedelta1 = timedelta(hours=10)
print(now + timedelta1)
timedelta2 = timedelta(days=-1)
print(now + timedelta2)
timedelta3 =timedelta(seconds=60)
print(now + timedelta3)

print('Divider...')

# 使用timezone这个类直接设置一个时区，然后将本地时间转换为utc时间
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8)
print(dt)

# 转换时区
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc) # 先用utcnow()函数得到当前的utc时间，然后将它转换为任意时区的时间
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)

# 将北京时间转换成东京时间
toyko_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(toyko_dt2)

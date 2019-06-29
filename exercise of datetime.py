import re
from datetime import datetime, timezone, timedelta


def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    re_utc = re.compile(r'^UTC([\+\-]*)(\d+)\:(\d+)$')
    utc = re_utc.match(tz_str)
    dt_utc = dt.replace(tzinfo=timezone(timedelta(hours=int(utc.group(1) + utc.group(2)), minutes=int(utc.group(1) + utc.group(3)))))
    dt_timestamp = dt_utc.timestamp()
    return dt_timestamp


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
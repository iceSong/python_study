# -*- coding:utf8 -*-
from datetime import datetime, timedelta, timezone
# python 处理时间 datatime是python处理时间的标准库

now = datetime.now()  # 当前日期
print(now)
print(type(now))

dt = datetime(2015, 4, 19, 12, 20)  # 构造指定日期
print(dt)

# datetime转化为timestamp
dt = datetime.now()
print(dt.timestamp())  # 将datetime转化为时间戳，小数位为毫秒

# timestamp转化为datatime
t = 14239417200.0121
ldt = datetime.fromtimestamp(t)  # 将timestamp转化为datetime
print(ldt)
udt = datetime.utcfromtimestamp(t)  # 转化为格林时间
print(udt)

# 将字符串转化为datatime
cday = datetime.strptime('2016-12-29 19:18:11', '%Y-%m-%d %H:%M:%S')
print(cday)
# datetime转化为字符串
print(cday.strftime('%a %Y-%m-%d %H:%M'))  # a表示周

# datatime的加减
now = datetime.now()
print(now)
now = now + timedelta(days=10)
print(now)


# datetime时区转化
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)  # 获取utc时间并设置为utc+0:00
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))  # 转化时区
print(bj_dt)
# astimezone()将时间转化为东京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# astimezone()将北京时间转化为东京时间
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))  # 也是只要设置时区就ok
print(tokyo_dt2)


# 作业 将2015-1-21 9:01:30 UTC+5:00 字符串转化为timestamp
def to_timestamp(dt_str, tz_str):
    dt0 = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    dt1 = dt0.replace(tzinfo=timezone(timedelta(hours=int(tz_str[4:5]))))  # replace函数可以强行设置日期的时区
    print(dt0.timestamp())
    print(dt1.timestamp())


to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')

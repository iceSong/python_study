# -*- coding:utf8 -*-

import os
import datetime, time


# 统计付费用户平均每天的登录次数

data_list = list()


def read_data_file(path):
    with open(path, 'r', encoding='utf-8') as rf:
    # with open(path, 'r') as rf:
        for line in rf.readlines():
            data_list.append(line.rstrip('\n').split('\t'))


def read_log_file(path):
    with open(path, 'r', encoding='utf8') as rf:
    # with open(path, 'r') as rf:
        for line in rf.readlines():
            if line.__contains__('GetUserBasicInfo'):
                for val in data_list:
                    if line.__contains__(val[5]):  # 应为有重复所以不能够break
                        if len(val) == 9:
                            val.append(1.0)
                        else:
                            val[9] += 1


def read_dir(path):
    files = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]
    for f in files:
        read_log_file(os.path.join(path, f))


def calculate_avg():
    for val in data_list:
        d1 = datetime.datetime.now()
        d2 = datetime.datetime.fromtimestamp(time.mktime(time.strptime(val[8], "%Y-%m-%d %H:%M:%S")))
        day = (d1 - d2).days
        if len(val) == 10:
            val[9] = round(val[9] / day, 3)  # 保留三位小数


def generate_ans(path):
    with open(path, 'w+', encoding='utf8') as wf:
    # with open(path, 'w+') as wf:
        for val in data_list:
            for field in val:
                wf.write(str(field))
                wf.write('\t')
            wf.write('\n')


if __name__ == '__main__':
    read_data_file('order')
    read_dir('./log1')
    read_dir('./log2')
    calculate_avg()
    generate_ans('ans')

    flag = 0
    for d in data_list:
        if len(d) == 10:
            flag += 1
    print('Total number %d, processed number %d' % (len(data_list), flag))




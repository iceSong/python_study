# -*- coding:utf-8 -*-

'''
统计最近一个月，用户选择科目的数据，格式：
省份  专业  科目  选择人数

基于上表，统计下选某个科目的人数比例，格式：
科目  人数比例

以及选某个专业的人数比例，格式：
专业  人数比例
'''

__author__ = 'song liu'


def readfile(path):
    with open(path, 'r') as rf:
        with open('tmp.sql', 'w+') as wf:
            for line in rf.readlines():
                data = line.split()
                subject = data[2].rstrip(';')
                for rec in subject.split(';'):
                    # wf.write('%s %s %s\n' % (data[0], data[1], record))
                    wf.write('INSERT INTO song_22(`pro`, `maj`, `sub`) VALUE ("%s", "%s", "%s");\n' % (data[0], data[1], rec))


if __name__ == '__main__':
    readfile('sta.txt')


# -*- coding:utf8 -*-
# 正则表达式

表示字符
\d  # 数字
\w  # 字母或数字
例子：00\d 可以表示007、005
例子：\d\d\d 可以表示123、432
例子：\w\w\d 可以表示ad4、235、w24
.  # 匹配任意字符 py. 表示py1  pyg  py@
\s  #表示空格或者tab

表个数
* 表示任意个字符
+ 至少一个字符
？0或1个字符
{n} 表示n个字符
{n,m} 表示n-m个字符


表示字符范围
[]  #例如：[0-9a-zA-Z\_]则表示数字、字母以及下滑线_
    [0-9a-zA-Z\_]+  表示至少有一个字母、数字或下滑线组成的字符串

[A|B] 匹配A或者B

表位置
^  # 表示行的开头  ^\d 表示以数字开头
$  # 表示结尾      \d$ 表示以数字结尾







表达式为字符+个数
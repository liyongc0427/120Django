"""
正则：是一种字符串的处理方式，用于字符串匹配

字符串的匹配分为两种方式：
    内容匹配：
        例如：
            python中的re模块（re模块含义:处理正则的一个模块）
            js中匹配
        通过要匹配的内容类型，长度进行匹配
    结构匹配：
        xpath（获取到某个内容的标签进行匹配），通过获取内容在整个文档中的结构 进行匹配
            html    div     p       img

    内容匹配讲解：
        类型匹配
            原样匹配 . \d \D \w \W [] | ()
        长度匹配
            * + ? {}
        特殊匹配
            ^ $
"""
import re
# re.findall() 尽可能 以列表的形式 返回结果
#原样匹配 . \d \D \w \W [] | ()
# str = "hello \n \t wORld ___ 123"
#原样匹配 在str中匹配前面的内容
# res = re.findall("ll",str)
# print(res)

#. 匹配除了\n 的所有内容
# res = re.findall(".",str)
# print(res)

#\d 匹配数字


#\D 匹配除了数字的所有内容


# \w 匹配字母 数字 下划线

# \W 匹配除了字母 数字 下划线的内容

#[] 返回符合 括号 中的内容
# res = re.findall("[a-zA-Z1-9]",str)
# print(res)

# | 返回任意一边符合的内容 （在str中存在的内容）
# res = re.findall("hello|wORld",str)
# print(res)

# 组匹配   # () 组      含义：先以 将括号外面的内容当做条件进行匹配
# str = "hllo \n \t wORld ___ 123"
# res = re.findall("(\w)l",str)
# #先将str中内容 以\w为条件进行匹配后，并且满足后面字母为l。 注意明白ll re.findall()  匹配所有的不重叠的匹配成功的部分
# print(res)

# str = "123 444 554"
# res = re.findall("(\d)4",str)
# print(res)


# 组匹配    起 组名
#(?P<id>\d):起组名  组名叫id； 不会影响结果与上面结果相同
# str = "123 444 554"
# res = re.findall("(?P<id>\d)4",str)
# print(res)  # 4 5

##调用组名的内容
##(?P=id)：使用 前面的匹配结果  \d44   \d45
# str = "123 444 554"
# res = re.findall("(?P<id>\d)4(?P=id)",str)
# print(res)


#长度匹配
str = "hllo \n \t wORld ___ 123"
# # *  匹配 0个：（0个所以打印""） 或 多个 满足条件的
# res = re.findall("\d*",str)
# # +  匹配1个或者多个 （：不存在0个 所以没有""）
# res = re.findall("\d+",str)
# #？ 匹配0个 或者 1个
# res = re.findall("\d?",str)
# #{} 匹配多次，匹配{}内指定的次数
# res = re.findall("\d{1}",str)
# # print(res)



#特殊匹配
#^ 匹配以什么开头
res = re.findall("^hl",str)
print(res)
# $ 匹配以什么结束
res = re.findall("3$",str)
print(res)

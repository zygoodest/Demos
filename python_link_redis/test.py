# !/usr/bin/env python3

import redis



"""
********************建立连接池***********************
使用connection pool来管理对一个redis server的所有连接
避免每次建立、释放连接的开销
(默认每个Redis实力都会维护一个自己的连接池)
"""
pool = redis.ConnectionPool(host="my_redis", port=6379)


"""
*******************实现redis协议*********************
"""
r = redis.Redis(connection_pool = pool)


"""
***********************设置值**********************
(不存在则创建，存在则修改)
set(name, value, ex=None, px=None, nx=False, xx=False)
ex  过期时间（秒）
px  过期时间（毫秒）
nx  若为True,则只有name不存在时，才执行set
xx  若为True,则只有name存在时，才执行set
"""
r.set("name", "zy")
r.setnx("name", "zy")               # 相当于r.set("name", "zy", nx=True)
r.setex("name", "zy", 5)            # 相当于r.set("name", "zy", ex=5)
r.psetex("name", "zy", 1000, "zy")  # 相当于r.set("name", "zy", px=1000)
r.mset({"k1": "v1", "k2": "v2"})    # 批量设置值


"""
***********************获取值*********************
"""
value = get("name")                 # 获取单个值
values = mget(["name1", "name2"])   # 批量获取多个值


"""
******************获取或设置子序列****************
获取部分子序列（根据字节获取，而非字符）
    getrange(name, start, end)     start:起始位置，end:结束位置
替换序列部分内容
    setrange(name, offset, value)   offset:开始替换的位置， value:要替换的内容
"""
value = getrange("name", 0, 3)


"""
*******************获取旧值并设置新值**************
old_value = getset(name, new_value)
"""
old_value = getset("name", "zygoodest")


"""
*********************二进制方式操作****************
"""
r.setbit(name, offset, value)           # 对name对应的二进制位进行操作
    # offset: 位的索引(将值变换成二进制后再进行索引)
    # value:  值只能是1或0
r.getbit(name, offset)                  # 获取name对应的二进制位的值
r.bitcount(name, start=None, end=None)  # 获取name对应的二进制值中1的个数
r.bitop(operation, dest, *keys)         # 获取多个值，将值做位运算，然后将值保存到新name
    # operation: AND并、OR或、NOT非、XOR异或
    # dest: 新的name
    # *keys: 要查找的name集
l = r.strlen(name)                      # 返回name对应值的字节长度(1个汉字占3字节，1个字母占1字节)


"""
*****************自增key*****************
"""



https://www.cnblogs.com/zhaohuhu/p/9140673.html#_label2















# 项目介绍

对原生list的二次封装

# 作者资料

昵称: jutooy

邮箱: jutooy@qq.com

# 语法

    from hyperlist import hyperlist


    a = hyperlist('123456789')

    print(a)
    # >>> ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    b = a.cut(4)
    print(b)
    # >>> [['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9']]
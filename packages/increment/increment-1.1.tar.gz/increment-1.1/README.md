# 项目介绍

主键生成器, 支持多机器|多进程|多线程高并发生成.

# 关于作者

许灿标，一个90后程序员。爱思考，爱钻研，善归纳。

# 资源彩蛋

GitHub: https://github.com/jutooy  
PyPi: https://pypi.org/user/jutooy  
语雀: https://www.yuque.com/jutooy  

# 与我联系

邮箱: jutooy@qq.com  
微信: Tony-Xu-  

# 语法

## 导入
    
    from increment import Increment

## 创建ID生成器

    inc = Increment()

## 使用创建进程时的时间

    inc.pk1()
    >>> lbiyib19-cd4-vearp9gt-0-1
    # lbiyib19是创建进程时的时间

    inc.pk1()
    >>> lbiyib19-cd4-vearp9gt-0-2

## 使用当前时间

    inc.pk2()
    >>> lbiyib1a-cd4-vearp9gt-0-3
    # lbiyib1a是当前时间

    inc.pk2()
    >>> lbiyib1b-cd4-vearp9gt-0-4
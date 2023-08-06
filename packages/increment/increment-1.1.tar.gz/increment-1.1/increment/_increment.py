import time, os
from collections import deque
from random import choices


Characters = ''.join(sorted('0123456789abcdefghijklmnopqrstuvwxyz'))
LenChars = len(Characters)

def EncodeNum(num:int):
    if num > 0:
        rn = deque()
        while num:
            num, i = divmod(num, LenChars)
            rn.appendleft(Characters[i])
        return ''.join(rn)
    return Characters[0]


tid = EncodeNum(int(time.time() * 1000))  # 一般毫秒后面的数值没有分辨率
pid = EncodeNum(os.getpid())


class IncBase:
    def __init__(self):
        self.Groups = []
        self.ContPool = deque()
    
    def getid(self):
        try:
            cont = self.ContPool.popleft()
        except:
            group = []
            self.Groups.append(group)
            cont = [EncodeNum(self.Groups.index(group)), 0]
        cont[1] += 1
        x, y = cont
        self.ContPool.append(cont)
        return f"{x}-{y}"

incbase = IncBase()


class Increment():

    def __init__(self, macid=None, macidSize=8):
        if macid:
            self.macid = macid
        else:
            self.macid = ''.join(choices(Characters, k=macidSize))
        self.TPM = f"{tid}-{pid}-{self.macid}"

    def pk1(self):
        # 顺序统一按: T-P-M-A
        # 使用创建进程时的时间
        incid = incbase.getid()
        pk = f"{self.TPM}-{incid}"
        return pk
    
    def pk2(self):
        # 顺序统一按: T-P-M-A
        # 使用当前时间
        tid = EncodeNum(int(time.time() * 1000))  # 一般毫秒后面的数值没有分辨率
        incid = incbase.getid()
        pk = f"{tid}-{pid}-{self.macid}-{incid}"
        return pk

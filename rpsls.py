#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：刘渝捷
日期：2021.12.1
"""

import random
answer=random.randint(0,5)

print("欢迎使用RPSLS游戏")
print("----------------")
i=input("请输入您的选择")


# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀


def name_to_number(name):
    if name=="石头":
        r=0
    elif name=="史波克":
        r=1
    elif name=="纸":
        r=2
    elif name=="蜥蜴":
        r=3
    elif name=="剪刀":
        r=4
    return r



def number_to_name(number):
    if number==0:
        t="石头"
    elif number==1:
        t="史波克"
    elif number==2:
        t="纸"
    elif number==3:
        t="蜥蜴"
    else:
        t="剪刀"
    return t


def rpsls(m):
    if m>=2 and answer==m-1 or answer==m-2:
        print("您赢了")
    elif m==1 and answer==0 or answer==4:
        print("您赢了")
    elif m==0 and answer==3 or answer==4:
        print("您赢了")
    elif m==answer:
        print("平局")
    else:
        print("计算机赢了")

q=name_to_number(i)
w=number_to_name(answer)
print("计算机输入了"+(w))
e=rpsls(q)


#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ������
���ڣ�2021.12.1
"""

import random
answer=random.randint(0,5)

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
i=input("����������ѡ��")


# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����


def name_to_number(name):
    if name=="ʯͷ":
        r=0
    elif name=="ʷ����":
        r=1
    elif name=="ֽ":
        r=2
    elif name=="����":
        r=3
    elif name=="����":
        r=4
    return r



def number_to_name(number):
    if number==0:
        t="ʯͷ"
    elif number==1:
        t="ʷ����"
    elif number==2:
        t="ֽ"
    elif number==3:
        t="����"
    else:
        t="����"
    return t


def rpsls(m):
    if m>=2 and answer==m-1 or answer==m-2:
        print("��Ӯ��")
    elif m==1 and answer==0 or answer==4:
        print("��Ӯ��")
    elif m==0 and answer==3 or answer==4:
        print("��Ӯ��")
    elif m==answer:
        print("ƽ��")
    else:
        print("�����Ӯ��")

q=name_to_number(i)
w=number_to_name(answer)
print("�����������"+(w))
e=rpsls(q)


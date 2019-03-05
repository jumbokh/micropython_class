# -*- coding: utf-8 -*-

"""
   程式說明請參閱14-8頁
"""

def A():
    print("It's A.")
    print('Name:', __name__)

def B():
    print("It's B.")
    print('Name:', __name__)

if __name__ == '__main__':
    A()
else:
    B()
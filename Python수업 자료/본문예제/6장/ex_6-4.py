#!/usr/bin/env python
# coding: utf-8

"""
6.4 데이터형 객체의 개념
(p.117 ~ p.119)
"""

# In[1]: p.117
def func(x):
    x = 5
    print('x(함수):', x)
x = 3
func(x)
print('x(메인):', x)


# In[2]: p.118
def swap(aa, bb):
    print('2: id(aa)', id(aa), 'id(bb)', id(bb))
    return bb, aa
a=3
b=5
print('a=', a, 'b=', b)
print('1: id(a)', id(a), 'id(b)', id(b))
a, b = swap(a, b)
print('3: id(a)', id(a), 'id(b)', id(b))
print('a=', a, 'b=', b)


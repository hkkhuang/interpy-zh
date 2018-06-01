#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 1_args_kwargs.py
# Author        : huangkeke
# Time          : 2018/4/17 21:52
# Contact       : hkkhuang@163.com
# Description	:


# *args 发送一个非键值对的可变数量的参数列表给函数
def test_var_args(f_arg, *argv):
    print('first normal arg:', f_arg)
    for arg in argv:
        print('another arg though *argv:', arg)


# **kwargs 将不定长度的键值对,作为参数传递给函数。
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print('{0} == {1}'.format(key, value))


def main():
    test_var_args('yasoob', 'python', 'eggs', 'test')
    greet_me(name='yasoob')


if __name__ == '__main__':
    main()

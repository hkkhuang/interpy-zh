#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 03_generators.py
# Author        : huangkeke
# Time          : 2018/6/2 11:39
# Contact       : hkkhuang@163.com
# Description	: 迭代器和生成器

def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def fibonacci():
    for x in fibon(1000000):
        print(x)


def generator_function():
    for i in range(3):
        yield i


def main():
    fibonacci()


if __name__ == '__main__':
    main()


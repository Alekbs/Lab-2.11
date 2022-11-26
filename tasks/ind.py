#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_func(tag):
    def func(string):
        string = ['<', tag, ">", string, "</", tag, ">"]
        return "".join(string)

    return func


if __name__ == "__main__":
    print("Результат работы функции: ", get_func("title")("текст"))

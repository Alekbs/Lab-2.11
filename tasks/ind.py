#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_func(tag):
    def func(string):
        return tag[0] + string + tag[1]

    return func


if __name__ == "__main__":
    print("Результат работы функции: ", get_func("<>")("обычный текст"))

# coding:utf-8
__author__ = 'rk.feng'

import logging  # noqa
import os  # noqa
import typing  # noqa
import unittest  # noqa
import time
import jieba


def main(count: int = 10):
    input_file = "./hlm.txt"
    with open(input_file, 'r') as f:
        content = f.read()

    _ = jieba.lcut("warm-up!")
    time_list = []
    for i in range(count):
        start = time.time()
        word_list = jieba.lcut(content)
        time_cost = time.time() - start
        time_list.append(time_cost)
        if i == 0:
            print("word_list:", word_list[:20])
        print(f"[iter {i + 1}]time cost {time_cost:.3f}s")

    # output time cost
    print(f"[total iter {count}][time_cost]avg {sum(time_list) / len(time_list):.3f}s, "
          f"max {max(time_list):.3f}s, min {min(time_list):.3f}s!")


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     util
   Description :
   Author :       qiangyanwen
   date：          2021/4/8
-------------------------------------------------
"""


def get_name_from_url(url):
    name = url.rsplit('/', 1)[-1]
    if name:
        name = name.rsplit(".")[0]
    return name


if __name__ == "__main__":
    fp = "/Users/yangzhixiang/Downloads/automation/移动端校验.jmx"
    print(get_name_from_url(fp))

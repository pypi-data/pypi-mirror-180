# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     cli
   Description :
   Author :       qiangyanwen
   date：          2021/4/6
-------------------------------------------------
"""

import sys
import os
import time
import yaml
from jmx2yaml.parser import parse_jmx_file


def get_absolute_path(path):
    fp, fn = os.path.split(path)
    if not fp:
        fp = os.getcwd()
    fp = os.path.abspath(os.path.expanduser(fp))
    return os.path.join(fp, fn)


def current_time() -> str:
    return time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())


def cli_main():
    if len(sys.argv) <= 1:
        print("please specify a jmx file full path")
        sys.exit(0)
    fn = sys.argv[1]
    if not fn.endswith('jmx'):
        print('error ext format of jmx file')
        sys.exit(0)
    fn = get_absolute_path(fn)
    if not os.path.isfile(fn):
        print('file not found', fn)
        sys.exit(0)
    new_path = fn[:-4] + "_" + current_time() + '.yaml'
    with open(new_path, 'w', encoding='utf-8') as f:
        f.write(yaml.dump(parse_jmx_file(fn), allow_unicode=True, sort_keys=False))
    print('jmx to yaml completed')


if __name__ == "__main__":
    cli_main()

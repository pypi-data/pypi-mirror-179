#!/usr/bin/env python
# coding=utf8

import os, random


def load_to_list(paths, deduplicate=False, appendix=None, recurse=False):
    """
    将指定路径下的文件，按行读入到list中。
    注意：不会进一步递归处理子文件夹!即，如果p是paths中的一个路径，p是一个文件夹，那么只会处理p里面的文件，而p里的文件夹会被忽略。
    :param recurse: 是否递归读取, 默认为不递归
    :param paths: 单个路径、或是可迭代的路径集合
    :param deduplicate: 元素是否去重, 默认不去重
    :param appendix: 识别的文件后缀, 仅读取指定后缀的文件
    :return:
    """
    if isinstance(paths, str):
        t = [paths]
        paths = t

    content_lst = []
    already_set = set()

    while paths:
        p = paths.pop(0)
        if os.path.isdir(p):
            for fn in os.listdir(p):
                fn_full = os.path.join(p, fn)
                if os.path.isfile(fn_full):
                    if (appendix is not None and fn.endswith(appendix)) or appendix is None:
                        with open(fn_full, 'r') as ifile:
                            for line in ifile:
                                content = line.strip()
                                if deduplicate:
                                    if content not in already_set:
                                        content_lst.append(content)
                                        already_set.add(content)
                                else:
                                    content_lst.append(content)
                else:
                    if recurse:
                        paths.append(fn_full)
        else:
            if (appendix is not None and p.endswith(appendix)) or appendix is None:
                with open(p, 'r') as ifile:
                    for line in ifile:
                        content = line.strip()
                        if deduplicate:
                            if content not in already_set:
                                content_lst.append(content)
                                already_set.add(content)
                        else:
                            content_lst.append(content)

    return content_lst


def load_to_set(paths, appendix=None, recurse=False):
    """
    将指定路径下的文件，按行读入到list中。
    注意：不会进一步递归处理子文件夹!即，如果p是paths中的一个路径，p是一个文件夹，那么只会处理p里面的文件，而p里的文件夹会被忽略。
    :param recurse: 是否递归读取，默认为不递归
    :param paths: 单个路径、或是可迭代的路径集合
    :param appendix: 识别的文件后缀, 仅读取指定后缀的文件
    :return:
    """
    if isinstance(paths, str):
        t = [paths]
        paths = t

    content_set = set()
    while paths:
        p = paths.pop(0)
        if os.path.isdir(p):
            for fn in os.listdir(p):
                fn_full = os.path.join(p, fn)
                if os.path.isfile(fn_full):
                    if (appendix is not None and fn.endswith(appendix)) or appendix is None:
                        with open(fn_full, 'r') as ifile:
                            for line in ifile:
                                content = line.strip()
                                content_set.add(content)
                else:
                    if recurse:
                        paths.append(fn_full)
        else:
            if (appendix is not None and p.endswith(appendix)) or appendix is None:
                with open(p, 'r') as ifile:
                    for line in ifile:
                        content = line.strip()
                        content_set.add(content)

    return content_set


def save_from_list(records, file_path, deduplicate=False):
    '''
    将list内容存至文件
    :param records: 待存储的lst
    :param file_path: 待存储的文件路径
    :param deduplicate: 元素是否去重, 默认不去重
    :return:
    '''

    if deduplicate is False:
        with open(file_path, 'w') as ofile:
            for r in records:
                print(r, file=ofile)
    else:
        s = set()
        with open(file_path, 'w') as ofile:
            for r in records:
                if r not in s:
                    print(r, file=ofile)
                    s.add(r)


def save_from_set(records, file_path):
    '''
    将set内容存至文件
    :param records:
    :param file_path:
    :return:
    '''
    lst = list(records)
    random.shuffle(lst)
    save_from_list(lst, file_path, deduplicate=False)

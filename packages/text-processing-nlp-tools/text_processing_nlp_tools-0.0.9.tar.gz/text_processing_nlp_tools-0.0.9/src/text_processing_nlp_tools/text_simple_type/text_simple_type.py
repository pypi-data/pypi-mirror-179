# -*- coding: utf-8 -*-
# @Time    : 11/1/22 5:33 PM
# @Author  : LIANYONGXING
# @FileName: text_simple_type.py
# @Software: PyCharm
# @Repo    : https://github.com/lianyongxing/text-processing-nlp-tools


def is_contain_chinese(raw_text):
    '''判断字符串是否包含中文'''
    for char in raw_text:
        if is_chinese(char):
            return True
    return False


def is_contain_english(raw_text):
    '''判断字符串是否包含英文字符'''
    for char in raw_text:
        if is_english(char):
            return True
    return False


def is_all_chinese(raw_text):
    '''判断字符串是否全为中文'''
    for char in raw_text:
        if not is_chinese(char):
            return False
    return True


def is_all_english(raw_text):
    '''判断字符串是否全为英文'''
    for char in raw_text:
        if not is_english(char):
            return False
    return True


def is_all_numbers(raw_text):
    '''判断字符串是否全为数字'''
    for char in raw_text:
        if not is_number(char):
            return False
    return True


def is_number(char):
    '''判断单个字符是否为阿拉伯数字'''
    if not '0' <= char <= '9':
        return False
    return True


def is_english(char):
    '''判断单个字符是否为英文字母'''
    if not 'A' <= char <= 'Z' and not 'a' <= char <= 'z':
        return False
    return True


def is_chinese(char):
    '''判断单个字符是否为中文'''
    if u'\u4e00' <= char and char <= u'\u9fa5':
        return True
    return False


if __name__ == "__main__":

    print(is_chinese("好啊"))
    print(is_contain_chinese("sadasds1212我"))
    print(is_contain_english("1212我"))
    print(is_all_numbers("212121"))
    print(is_all_english("sadasass111"))
    print(is_all_chinese("我今天吃了"))

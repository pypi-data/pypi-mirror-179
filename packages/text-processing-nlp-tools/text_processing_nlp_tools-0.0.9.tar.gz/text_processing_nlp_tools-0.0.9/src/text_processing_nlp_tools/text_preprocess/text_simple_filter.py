# -*- coding: utf-8 -*-
# @Time    : 11/14/22 2:28 PM
# @Author  : LIANYONGXING
# @FileName: text_simple_filter.py
# @Software: PyCharm
# @Repo    : https://github.com/lianyongxing/text-processing-nlp-tools

def str_only_keep_ch(s):
    """
    字符串只保留中文
    """
    return re.sub(r'[^\u4e00-\u9fa5]', '', s).lower()

def str_keep_ch_en_num(s, lowercase=True):
    """
    字符串只保留中文和英文字母、数字
    """
    if lowercase:
        return re.sub(r'[^0-9a-zA-Z\u4e00-\u9fa5]', '', s).lower()  # 去除除了汉字大小写
    else:
        return re.sub(r'[^0-9a-zA-Z\u4e00-\u9fa5]', '', s)  # 去除除了汉字大小写

def get_minsubstring(s):
    """
        获取字符串最小字串
    """
    try:
        idx = (s+s).index(s, 1)
        if idx == len(s):
            return s
        else: 
            return s[:idx]
    except:
        return s
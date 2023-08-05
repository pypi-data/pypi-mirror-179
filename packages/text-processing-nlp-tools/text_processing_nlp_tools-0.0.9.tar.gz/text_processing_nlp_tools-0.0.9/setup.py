# -*- coding: utf-8 -*-
# @Time    : 11/5/22 3:52 PM
# @Author  : LIANYONGXING
# @FileName: setup.py
# @Software: PyCharm
# @Repo    : https://github.com/lianyongxing/

#!/usr/bin/env python
# coding: utf-8

from setuptools import setup
import setuptools

setup(
    name='text_processing_nlp_tools',
    version='0.0.9',
    author='tianran',
    author_email='512796933@qq.com',
    url='https://github.com/lianyongxing/',
    description=u'文本处理',
    install_requires=['flashtext', 'jieba-fast', 'tqdm'],
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},  # 必填
    include_package_data=True
)
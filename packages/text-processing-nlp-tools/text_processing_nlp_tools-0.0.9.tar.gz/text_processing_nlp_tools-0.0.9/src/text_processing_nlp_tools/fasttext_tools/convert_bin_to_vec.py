# -*- coding: utf-8 -*-
# @Time    : 11/30/22 2:37 PM
# @Author  : LIANYONGXING
# @FileName: fasttext_tools.py
# @Software: PyCharm
# @Repo    : https://github.com/lianyongxing/text-processing-nlp-tools
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division, absolute_import, print_function

from fasttext import load_model
import argparse
import errno

if __name__ == "__main__":

    # python bin_to_vec.py unsupervised_data.bin > unsupervised_data.vec

    parser = argparse.ArgumentParser(
        description=("Print fasttext .vec file to stdout from .bin file")
    )
    parser.add_argument(
        "model",
        help="Model to use",
    )
    args = parser.parse_args()

    f = load_model(args.model)
    words = f.get_words()
    print(str(len(words)) + " " + str(f.get_dimension()))
    for w in words:
        v = f.get_word_vector(w)
        vstr = ""
        for vi in v:
            vstr += " " + str(vi)
        try:
            print(w + vstr)
        except IOError as e:
            if e.errno == errno.EPIPE:
                pass
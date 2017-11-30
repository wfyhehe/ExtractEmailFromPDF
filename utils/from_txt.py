#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def extract_email_from_txt(txt):
    """
    txt='xxx.txt'
    return a list of emails
    :param txt:
    :return list['xxx@xxx.xxx'...]:
    """
    with open(txt, 'r') as f:
        block_text = f.read()

    email_regex = u'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
    return re.findall(email_regex, block_text)


def extract_cellphone_from_txt(txt):
    """
    txt='xxx.txt'
    return a list of cellphone numbers
    :param txt:
    :return list['xxxxxxxxxx'...]:
    """
    with open(txt, 'r') as f:
        block_text = f.read()

    phone_regex = u'\D([1][3,4,5,7,8][0-9]{9})\D'
    return re.findall(phone_regex, block_text)
